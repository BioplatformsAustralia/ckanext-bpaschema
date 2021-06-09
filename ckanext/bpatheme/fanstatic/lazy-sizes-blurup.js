/*! lazysizes - v5.3.2 */

!function(e,t){var a;e&&(a=function(){t(e.lazySizes),e.removeEventListener("lazyunveilread",a,!0)},t=t.bind(null,e,e.document),"object"==typeof module&&module.exports?t(require("lazysizes")):"function"==typeof define&&define.amd?define(["lazysizes"],t):e.lazySizes?a():e.addEventListener("lazyunveilread",a,!0))}("undefined"!=typeof window?window:0,function(l,b,A){"use strict";var a;!function(){var e,t={blurUpClass:"ls-blur-up-img",blurUpLoadingClass:"ls-blur-up-is-loading",blurUpInviewClass:"ls-inview",blurUpLoadedClass:"ls-blur-up-loaded",blurUpLoadedOriginalClass:"ls-original-loaded"};for(e in a=A.cfg||{},t)e in a||(a[e]=t[e])}();function r(e,t){var i;return(e?n.call(e.querySelectorAll("source, img")):[t]).forEach(function(e){var t,a,n,r;i||(!(t=e.getAttribute("data-lowsrc"))||(n=(a=e).getAttribute("data-media")||a.getAttribute("media"),(r=a.getAttribute("type"))&&!o.test(r)||n&&!l.matchMedia(A.cfg.customMedia[n]||n).matches)||(i=t))}),i}function i(e,t,a,n){function r(){l&&A.rAF(function(){A.rC(t,A.cfg.blurUpLoadingClass);try{l.parentNode.removeChild(l)}catch(e){}l=null})}function i(e){c++,u=e||u,e?r():1<c&&setTimeout(r,5e3)}var l,s,o=!1,u=!1,d="always"==n?0:Date.now(),c=0,f=(e||t).parentNode,v=function(){t.removeEventListener("load",v),t.removeEventListener("error",v),l&&A.rAF(function(){l&&A.aC(l,A.cfg.blurUpLoadedOriginalClass)}),A.fire(t,"blurUpLoaded"),"always"!=n&&(!o||Date.now()-d<66)?i(!0):i()};a&&(s=function(e){o=!0,l=l||e.target,A.rAF(function(){A.rC(t,A.cfg.blurUpLoadingClass),l&&A.aC(l,A.cfg.blurUpLoadedClass)}),l&&(l.removeEventListener("load",s),l.removeEventListener("error",s))},(l=b.createElement("img")).addEventListener("load",s),l.addEventListener("error",s),l.className=A.cfg.blurUpClass,l.cssText=t.cssText,l.src=a,l.alt="",l.setAttribute("aria-hidden","true"),f.insertBefore(l,(e||t).nextSibling),"always"!=n&&(l.style.visibility="hidden",A.rAF(function(){l&&setTimeout(function(){l&&A.rAF(function(){!u&&l&&(l.style.visibility="")})},A.cfg.blurupCacheDelay||33)}))),t.addEventListener("load",v),t.addEventListener("error",v),A.aC(t,A.cfg.blurUpLoadingClass);var g=function(e){f==e.target&&(A.aC(l||t,A.cfg.blurUpInviewClass),i(),f.removeEventListener("lazybeforeunveil",g))};f.getAttribute("data-expand")||f.setAttribute("data-expand",-1),f.addEventListener("lazybeforeunveil",g),A.aC(f,A.cfg.lazyClass)}var n=[].slice,s=/blur-up["']*\s*:\s*["']*(always|auto)/,o=/image\/(jpeg|png|gif|svg\+xml)/;l.addEventListener("lazybeforeunveil",function(e){var t,a,n=e.detail;n.instance==A&&n.blurUp&&("PICTURE"!=(a=(t=e.target).parentNode).nodeName&&(a=null),i(a,t,r(a,t)||"data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",n.blurUp))}),l.addEventListener("lazyunveilread",function(e){var t,a,n=e.detail;n.instance==A&&(t=e.target,((a=(getComputedStyle(t,null)||{fontFamily:""}).fontFamily.match(s))||t.getAttribute("data-lowsrc"))&&(n.blurUp=a&&a[1]||A.cfg.blurupMode||"always"))})});