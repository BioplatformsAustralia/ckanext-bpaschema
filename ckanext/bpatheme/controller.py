# encoding: utf-8
import json
import os
import re
import urllib
from logging import getLogger
from urlparse import urlsplit

import ckan.lib.helpers as h
import pydevd_pycharm
pydevd_pycharm.settrace('host.docker.internal', port=57892, stdoutToServer=True, stderrToServer=True, suspend=False)

import ckan.lib.base as base
import pandas as pd

log = getLogger(__name__)

summary_table_data_path = os.environ.get('SUMMARY_TABLE_DATA_PATH')
link_marker = '<i class="fa fa-circle" aria-hidden="true"></i>'
link_format = '<a target="_blank" rel="noopener noreferrer" href="{0}">{1}</a>'
search_patterns = {
    "yes": r"^[\s]*yes.*",
    "http": r"^[\s]*http[s]?:\/\/data.bioplatforms.com.*$",
}


def replace_df_header_with_row(df, row):
    df.drop(0, inplace=True)
    df.columns = row


def search_and_replace_once(text):
    for search_keyword, replace_fn in {"yes": replace_yes, "http": replace_http}.items():

        if re.search(search_patterns[search_keyword], text):
            return replace_fn(text)
    return None


def replace_yes(text):
    return re.sub(search_patterns["yes"], link_marker, text)


def replace_http(text):
    text = text.strip()
    separated = [not_empty for not_empty in re.split(r',|\s', text) if not_empty]
    return replace_multi_urls(separated)


def replace_multi_urls(urls):
    ids_text = create_query_parameter("id", urls.pop(0))
    for next_id in urls:
        ids_text += create_query_parameter(" OR id", next_id)
    return (
        '<a target="_blank" rel="noopener noreferrer" href="https://data.bioplatforms.com/dataset?q={0}">{1}</a>'.format(
            ids_text, link_marker))


def create_query_parameter(query_format, url):
    # get url final path component only and ensure trailing backslash is handled
    last_path = [not_empty for not_empty in urlsplit(url).path.split('/') if not_empty][-1]
    return urllib.quote("{0}:{1}".format(query_format, last_path))


class SummaryController(base.BaseController):

    def index(self):
        if not os.path.exists(summary_table_data_path):
            log.error("Could not find path to summary table data: {0}".format(summary_table_data_path))
        df = pd.read_json(summary_table_data_path)
        first_row = df.iloc[0]
        replace_df_header_with_row(df, first_row)
        bt_header = json.loads(first_row.to_json(orient="records"))
        indexed_json = json.loads(df.to_json(orient="index"))
        bt_json = []
        for (index, next_row) in indexed_json.items():
            bt_json.append(next_row)
            for (k, v) in next_row.items():
                if index not in ["0", "1", "2"]:
                    replaced = search_and_replace_once(v)
                    if replaced:
                        # // ensure any quotes are escaped before passing 'python' JSON into front-end
                        next_row[k] = h.escape_js(replaced)
        return base.render('summary/index.html',
                           extra_vars={'spreadsheet_data': json.dumps(bt_json), 'spreadsheet_columns': bt_header})
