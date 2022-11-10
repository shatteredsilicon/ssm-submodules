| id | path | title | desc | cvss | ref |
| --- | --- | --- | --- | --- | --- |
| 1069642 | remarkable | Cross-site Scripting in remarkable | In remarkable 1.7.1, lib/parser_inline.js mishandles URL filtering, which allows attackers to trigger XSS via unprintable characters, as demonstrated by a \x0ejavascript: URL. | 6.1 | https://github.com/advisories/GHSA-36m4-6v6m-4vpr |
| 1069585 | remarkable | Regular Expression Denial of Service in remarkable | lib/common/html_re.js in remarkable 1.7.1 allows Regular Expression Denial of Service (ReDoS) via a CDATA section. | 7.5 | https://github.com/advisories/GHSA-q22g-8fr4-qpj4 |
| 1082469 | webpack-dev-server>http-proxy-middleware>http-proxy | Denial of Service in http-proxy | Versions of `http-proxy` prior to 1.18.1 are vulnerable to Denial of Service. An HTTP request with a long body triggers an `ERR_HTTP_HEADERS_SENT` unhandled exception that crashes the proxy server. This is only possible when the proxy server sets headers in the proxy request using the `proxyReq.setHeader` function.   <br /><br />For a proxy server running on `http://localhost:3000`, the following curl request triggers the unhandled exception:  <br />```curl -XPOST http://localhost:3000 -d "$(python -c 'print("x"*1025)')"```<br /><br /><br />## Recommendation<br /><br />Upgrade to version 1.18.1 or later | 0 | https://github.com/advisories/GHSA-6x33-pw7p-hmpq |
| 1082455 | npm>npm-user-validate | Regular Expression Denial of Service in npm-user-validate | `npm-user-validate` before version `1.0.1` is vulnerable to a Regular Expression Denial of Service (REDos). The regex that validates user emails took exponentially longer to process long input strings beginning with `@` characters.<br /><br />### Impact<br />The issue affects the `email` function. If you use this function to process arbitrary user input with no character limit the application may be susceptible to Denial of Service.<br /><br />### Patches<br />The issue is patched in version 1.0.1 by improving the regular expression used and also enforcing a 254 character limit.<br /><br />### Workarounds<br />Restrict the character length to a reasonable degree before passing a value to `.emal()`; Also, consider doing a more rigorous sanitizing/validation beforehand. | 0 | https://github.com/advisories/GHSA-xgh6-85xh-479p |
| 1082254 | npm>npm-user-validate | Regular expression denial of service in npm-user-validate | This affects the package npm-user-validate before 1.0.1. The regex that validates user emails took exponentially longer to process long input strings beginning with @ characters. | 7.5 | https://github.com/advisories/GHSA-pw54-mh39-w3hc |
| 1082117 | webpack-dev-server>bonjour>multicast-dns>dns-packet | Potential memory exposure in dns-packet | This affects the package dns-packet before versions 1.3.2 and 5.2.2. It creates buffers with allocUnsafe and does not always fill them before forming network packets. This can expose internal application memory over unencrypted network when querying crafted invalid domain names. | 7.7 | https://github.com/advisories/GHSA-3wcq-x3mq-6r9p |
| 1082010 | npm>update-notifier>configstore>dot-prop | dot-prop Prototype Pollution vulnerability | Prototype pollution vulnerability in dot-prop npm package versions before 4.2.1 and versions 5.x before 5.1.1 allows an attacker to add arbitrary properties to JavaScript language constructs such as objects. | 7.3 | https://github.com/advisories/GHSA-ff7x-qrg7-qggm |
| 1070428 | grunt-contrib-compress>archiver>tar-stream>bl | Remote Memory Exposure in bl | A buffer over-read vulnerability exists in bl <4.0.3, <3.0.1, <2.2.1, and <1.2.3 which could allow an attacker to supply user input (even typed) that if it ends up in consume() argument and can become negative, the BufferList state can be corrupted, tricking it into exposing uninitialized memory via regular .slice() calls. | 6.5 | https://github.com/advisories/GHSA-pp7h-53gx-mx7r |
| 1081827 | jquery | Potential XSS vulnerability in jQuery | ### Impact<br />Passing HTML containing `<option>` elements from untrusted sources - even after sanitizing them - to one of jQuery's DOM manipulation methods (i.e. `.html()`, `.append()`, and others) may execute untrusted code.<br /><br />### Patches<br />This problem is patched in jQuery 3.5.0.<br /><br />### Workarounds<br />To workaround this issue without upgrading, use [DOMPurify](https://github.com/cure53/DOMPurify) with its `SAFE_FOR_JQUERY` option to sanitize the HTML string before passing it to a jQuery method.<br /><br />### References<br />https://blog.jquery.com/2020/04/10/jquery-3-5-0-released/<br /><br />### For more information<br />If you have any questions or comments about this advisory, search for a relevant issue in [the jQuery repo](https://github.com/jquery/jquery/issues). If you don't find an answer, open a new issue. | 6.9 | https://github.com/advisories/GHSA-jpcq-cgw6-v4j6 |
| 1081826 | jquery | Potential XSS vulnerability in jQuery | ### Impact<br />Passing HTML from untrusted sources - even after sanitizing it - to one of jQuery's DOM manipulation methods (i.e. `.html()`, `.append()`, and others) may execute untrusted code.<br /><br />### Patches<br />This problem is patched in jQuery 3.5.0.<br /><br />### Workarounds<br />To workaround the issue without upgrading, adding the following to your code:<br /><br />```js<br />jQuery.htmlPrefilter = function( html ) {<br />	return html;<br />};<br />```<br /><br />You need to use at least jQuery 1.12/2.2 or newer to be able to apply this workaround.<br /><br />### References<br />https://blog.jquery.com/2020/04/10/jquery-3-5-0-released/<br />https://jquery.com/upgrade-guide/3.5/<br /><br />### For more information<br />If you have any questions or comments about this advisory, search for a relevant issue in [the jQuery repo](https://github.com/jquery/jquery/issues). If you don't find an answer, open a new issue. | 6.9 | https://github.com/advisories/GHSA-gxr4-xjj5-5px2 |
| 1069969 | jquery | XSS in jQuery as used in Drupal, Backdrop CMS, and other products | jQuery before 3.4.0, as used in Drupal, Backdrop CMS, and other products, mishandles jQuery.extend(true, {}, ...) because of Object.prototype pollution. If an unsanitized source object contained an enumerable __proto__ property, it could extend the native Object.prototype. | 6.1 | https://github.com/advisories/GHSA-6c3j-c64m-qhgq |
| 1069420 | npm>npm-profile>make-fetch-happen>https-proxy-agent | Machine-In-The-Middle in https-proxy-agent | Versions of `https-proxy-agent` prior to 2.2.3 are vulnerable to Machine-In-The-Middle. The package fails to enforce TLS on the socket if the proxy server responds the to the request with a HTTP status different than 200. This allows an attacker with access to the proxy server to intercept unencrypted communications, which may include sensitive information such as credentials.<br /><br /><br />## Recommendation<br /><br />Upgrade to version 3.0.0 or 2.2.3. | 6.1 | https://github.com/advisories/GHSA-pc5p-h8pf-mvwp |
| 1069395 | webpack-dev-server>sockjs>faye-websocket>websocket-driver>websocket-extensions | Regular Expression Denial of Service in websocket-extensions (NPM package) | ### Impact<br /><br />The ReDoS flaw allows an attacker to exhaust the server's capacity to process<br />incoming requests by sending a WebSocket handshake request containing a header<br />of the following form:<br /><br />    Sec-WebSocket-Extensions: a; b="\c\c\c\c\c\c\c\c\c\c ...<br /><br />That is, a header containing an unclosed string parameter value whose content is<br />a repeating two-byte sequence of a backslash and some other character. The<br />parser takes exponential time to reject this header as invalid, and this will<br />block the processing of any other work on the same thread. Thus if you are<br />running a single-threaded server, such a request can render your service<br />completely unavailable.<br /><br />### Patches<br /><br />Users should upgrade to version 0.1.4.<br /><br />### Workarounds<br /><br />There are no known work-arounds other than disabling any public-facing<br />WebSocket functionality you are operating.<br /><br />### References<br /><br />- https://blog.jcoglan.com/2020/06/02/redos-vulnerability-in-websocket-extensions/ | 8.2 | https://github.com/advisories/GHSA-g78m-2chm-r7qv |
| 1082380 | webpack>node-libs-browser>crypto-browserify>browserify-sign>elliptic | Use of a Broken or Risky Cryptographic Algorithm | The npm package `elliptic` before version 6.5.4 are vulnerable to Cryptographic Issues via the secp256k1 implementation in elliptic/ec/key.js. There is no check to confirm that the public key point passed into the derive function actually exists on the secp256k1 curve. This results in the potential for the private key used in this implementation to be revealed after a number of ECDH operations are performed. | 6.8 | https://github.com/advisories/GHSA-r9p9-mrjm-926w |
| 1069331 | webpack>node-libs-browser>crypto-browserify>browserify-sign>elliptic | Signature Malleabillity in elliptic | The Elliptic package before version 6.5.3 for Node.js allows ECDSA signature malleability via variations in encoding, leading '\0' bytes, or integer overflows. This could conceivably have a security-relevant impact if an application relied on a single canonical signature. | 7.7 | https://github.com/advisories/GHSA-vh7m-p724-62c2 |
| 1069551 | grunt-sass>node-sass>lodash.mergewith | Prototype Pollution in lodash | Versions of `lodash` before 4.17.12 are vulnerable to Prototype Pollution.  The function `defaultsDeep` allows a malicious user to modify the prototype of `Object` via `{constructor: {prototype: {...}}}` causing the addition or modification of an existing property that will exist on all objects.<br /><br /><br /><br /><br />## Recommendation<br /><br />Update to version 4.17.12 or later. | 9.1 | https://github.com/advisories/GHSA-jf85-cpcp-j695 |
| 1068700 | grunt-sass>node-sass>lodash.mergewith | Prototype Pollution in lodash.mergewith | Versions of `lodash.mergewith` before 4.6.2 are vulnerable to prototype pollution. The function `mergeWith` may allow a malicious user to modify the prototype of `Object` via `{constructor: {prototype: {...}}}` causing the addition or modification of an existing property that will exist on all objects.<br /><br /><br /><br /><br />## Recommendation<br /><br />Update to version 4.6.2 or later. | 0 | https://github.com/advisories/GHSA-779f-wgxg-qr8f |
| 1067553 | sass-lint>eslint>is-my-json-valid>jsonpointer | Prototype Pollution in node-jsonpointer | This affects the package `jsonpointer` before `5.0.0`. A type confusion vulnerability can lead to a bypass of a previous Prototype Pollution fix when the pointer components are arrays. | 5.6 | https://github.com/advisories/GHSA-282f-qqgm-c34q |
| 1067427 | grunt-contrib-compress>iltorb>prebuild-install>simple-get | Exposure of Sensitive Information in simple-get | In versions of simple-get prior to 4.0.1, 3.1.1, and 2.8.2, when fetching a remote url with a cookie location response, headers will be followed, potentially resulting in an exposure of the session cookie to a third party. | 7.5 | https://github.com/advisories/GHSA-wpg7-2c88-r8xv |
| 1067351 | webpack-dev-server | Missing Origin Validation in webpack-dev-server | Versions of `webpack-dev-server` before 3.1.10 are missing origin validation on the websocket server. This vulnerability allows a remote attacker to steal a developer's source code because the origin of requests to the websocket server that is used for Hot Module Replacement (HMR) are not validated.<br /><br /><br />## Recommendation<br />For `webpack-dev-server` update to version 3.1.11 or later. | 7.5 | https://github.com/advisories/GHSA-cf66-xwfp-gvc4 |
| 1082350 | webpack-dev-server>sockjs-client>url-parse | Improper Validation and Sanitization in url-parse | Insufficient validation and sanitization of user input exists in url-parse npm package version 1.4.4 and earlier may allow attacker to bypass security checks. | 5.3 | https://github.com/advisories/GHSA-46c4-8wrp-j99v |
| 1070424 | webpack-dev-server>sockjs-client>url-parse | Path traversal in url-parse | url-parse before 1.5.0 mishandles certain uses of backslash such as http:\/ and interprets the URI as a relative path. | 5.3 | https://github.com/advisories/GHSA-9m6j-fcg5-2442 |
| 1070014 | webpack-dev-server>sockjs-client>url-parse | Incorrect returned href via an '@' sign but no user info and hostname | A specially crafted URL with an '@' sign but empty user info and no hostname, when parsed with url-parse, url-parse will return the incorrect href. In particular,<br />`````<br />parse(\"http://@/127.0.0.1\")<br />`````<br />Will return:<br />`````<br />{<br /> slashes: true,<br /> protocol: 'http:',<br /> hash: '',<br /> query: '',<br /> pathname: '/127.0.0.1',<br /> auth: '',<br /> host: '',<br /> port: '',<br /> hostname: '',<br /> password: '',<br /> username: '',<br /> origin: 'null',<br /> href: 'http:///127.0.0.1'<br /> }<br />`````<br />If the 'hostname' or 'origin' attributes of the output from url-parse are used in security decisions and the final 'href' attribute of the output is then used to make a request, the decision may be incorrect. | 6.5 | https://github.com/advisories/GHSA-8v38-pw62-9cw2 |
| 1067774 | webpack-dev-server>sockjs-client>url-parse | Open redirect in url-parse | # Overview<br /><br />Affected versions of npm `url-parse` are vulnerable to URL Redirection to Untrusted Site.<br /><br /># Impact<br /><br />Depending on library usage and attacker intent, impacts may include allow/block list bypasses, SSRF attacks, open redirects, or other undesired behavior. | 6.1 | https://github.com/advisories/GHSA-hh27-ffr2-f2jc |
| 1067405 | webpack-dev-server>sockjs-client>url-parse | Authorization bypass in url-parse | Authorization Bypass Through User-Controlled Key in NPM url-parse prior to 1.5.6. | 5.3 | https://github.com/advisories/GHSA-rqff-837h-mm52 |
| 1067316 | webpack-dev-server>sockjs-client>url-parse | Authorization Bypass Through User-Controlled Key in url-parse | url-parse prior to version 1.5.8 is vulnerable to Authorization Bypass Through User-Controlled Key. | 9.1 | https://github.com/advisories/GHSA-hgjh-723h-mx2j |
| 1067315 | webpack-dev-server>sockjs-client>url-parse | Incorrect hostname / protocol due to unstripped leading control characters. | Leading control characters in a URL are not stripped when passed into url-parse. This can cause input URLs to be mistakenly be interpreted as a relative URL without a hostname and protocol, while the WHATWG URL parser will trim control characters and treat it as an absolute URL.<br /><br />If url-parse is used in security decisions involving the hostname / protocol, and the input URL is used in a client which uses the WHATWG URL parser, the decision may be incorrect.<br /><br />This can also lead to a cross-site scripting (XSS) vulnerability if url-parse is used to check for the javascript: protocol in URLs. See following example:<br />`````<br />const parse = require('url-parse')<br />const express = require('express')<br />const app = express()<br />const port = 3000<br /><br />url = parse(\"\\bjavascript:alert(1)\")<br /><br />console.log(url)<br /><br />app.get('/', (req, res) => {<br /> if (url.protocol !== \"javascript:\") {res.send(\"<a href=\\'\" + url.href + \"\\'>CLICK ME!</a>\")}<br /> })<br /><br />app.listen(port, () => {<br /> console.log(`Example app listening on port ${port}`)<br /> })<br />````` | 6.5 | https://github.com/advisories/GHSA-jf5r-8hm2-f872 |
| 1081883 | grunt-sass>node-sass>sass-graph>yargs>yargs-parser | yargs-parser Vulnerable to Prototype Pollution | Affected versions of `yargs-parser` are vulnerable to prototype pollution. Arguments are not properly sanitized, allowing an attacker to modify the prototype of `Object`, causing the addition or modification of an existing property that will exist on all objects.  <br />Parsing the argument `--foo.__proto__.bar baz'` adds a `bar` property with value `baz` to all objects. This is only exploitable if attackers have control over the arguments being passed to `yargs-parser`.<br /><br /><br /><br />## Recommendation<br /><br />Upgrade to versions 13.1.2, 15.0.1, 18.1.1 or later. | 5.3 | https://github.com/advisories/GHSA-p9pc-299p-vxgp |
| 1068780 | grunt-sass>node-sass | Denial of Service in node-sass | Affected versions of `node-sass` are vulnerable to Denial of Service (DoS). Crafted objects passed to the `renderSync` function may trigger C++ assertions in `CustomImporterBridge::get_importer_entry` and `CustomImporterBridge::post_process_return_value` that crash the Node process. This may allow attackers to crash the system's running Node process and lead to Denial of Service.<br /><br /><br />## Recommendation<br /><br />Upgrade to version 4.13.1 or later | 5.9 | https://github.com/advisories/GHSA-9v62-24cr-58cx |
| 1082491 | npm>libcipm>bin-links | Arbitrary File Write in bin-links | Versions of `bin-links` prior to 1.1.5 are vulnerable to an Arbitrary File Write. The package fails to restrict access to folders outside of the intended `node_modules` folder through the `bin` field. This allows attackers to create arbitrary files in the system. Note it is not possible to overwrite files that already exist.<br /><br /><br />## Recommendation<br /><br />Upgrade to version 1.1.5 or later. | 0 | https://github.com/advisories/GHSA-gqf6-75v8-vr26 |
| 1082490 | npm>libcipm>bin-links | Symlink reference outside of node_modules in bin-links | Versions of `bin-links` prior to 1.1.5 are vulnerable to a Symlink reference outside of node_modules. It is possible to create symlinks to files outside of the`node_modules` folder through the `bin` field. This may allow attackers to access unauthorized files.<br /><br /><br />## Recommendation<br /><br />Upgrade to version 1.1.5 or later. | 0 | https://github.com/advisories/GHSA-2mj8-pj3j-h362 |
| 1082489 | npm>libcipm>bin-links | Global node_modules Binary Overwrite in bin-links | Versions of  `bin-links` prior to 1.1.6 are vulnerable to a Global node_modules Binary Overwrite. It fails to prevent globally-installed binaries to be overwritten by other package installs. For example, if a package was installed globally and created a `serve` binary, any subsequent installs of packages that also create a `serve` binary would overwrite the first binary. This behavior is still allowed in local installations.<br /><br /><br />## Recommendation<br /><br />Upgrade to version 1.1.6 or later. | 0 | https://github.com/advisories/GHSA-v45m-2wcp-gg98 |
| 1069638 | npm>node-gyp>tar | Arbitrary File Overwrite in tar | Versions of `tar` prior to 4.4.2 for 4.x and 2.2.2 for 2.x are vulnerable to Arbitrary File Overwrite. Extracting tarballs containing a hardlink to a file that already exists in the system, and a file that matches the hardlink will overwrite the system's file with the contents of the extracted file.<br /><br /><br />## Recommendation<br /><br />For tar 4.x, upgrade to version 4.4.2 or later.<br />For tar 2.x, upgrade to version 2.2.2 or later. | 7.5 | https://github.com/advisories/GHSA-j44m-qm6p-hp7m |
| 1069630 | npm>libcipm>npm-lifecycle>node-gyp>tar>fstream | Arbitrary File Overwrite in fstream | Versions of `fstream` prior to 1.0.12 are vulnerable to Arbitrary File Overwrite. Extracting tarballs containing a hardlink to a file that already exists in the system and a file that matches the hardlink will overwrite the system's file with the contents of the extracted file. The `fstream.DirWriter()` function is vulnerable.<br /><br /><br />## Recommendation<br /><br />Upgrade to version 1.0.12 or later. | 7.5 | https://github.com/advisories/GHSA-xf7w-r453-m56c |
| 1082255 | webpack-dev-server>sockjs | Improper Input Validation in SocksJS-Node | Incorrect handling of Upgrade header with the value websocket leads in crashing of containers hosting sockjs apps. This affects the package sockjs before 0.3.20. | 5.3 | https://github.com/advisories/GHSA-c9g6-9335-x697 |
| 1082045 | webpack-dev-server>ansi-html | Uncontrolled Resource Consumption in ansi-html | This affects all versions of package ansi-html. If an attacker provides a malicious string, it will get stuck processing the input for an extremely long time. | 7.5 | https://github.com/advisories/GHSA-whgm-jr23-g3j9 |
| 1070434 | webpack-dev-server>sockjs-client>eventsource | Exposure of Sensitive Information in eventsource | When fetching an url with a link to an external site (Redirect), the users Cookies & Autorisation headers are leaked to the third party application. According to the same-origin-policy, the header should be "sanitized." | 9.3 | https://github.com/advisories/GHSA-6h5x-7c5m-7cr7 |
| 1068341 | webpack-dev-server>selfsigned>node-forge | Prototype Pollution in node-forge | The package node-forge before 0.10.0 is vulnerable to Prototype Pollution via the util.setPath function. Note: Version 0.10.0 is a breaking change removing the vulnerable functions. | 8.8 | https://github.com/advisories/GHSA-92xj-mqp7-vmcj |
| 1067472 | webpack-dev-server>selfsigned>node-forge | Prototype Pollution in node-forge util.setPath API | ### Impact<br />`forge.util.setPath` had a potential prototype pollution issue if called with untrusted keys. This API was not used by forge itself.<br /><br />### Patches<br />The `forge.util.setPath` API and related functions were removed in 0.10.0.<br /><br />### Workarounds<br />Don't call `forge.util.setPath` directly or indirectly with untrusted keys.<br /><br />### References<br />- https://security.snyk.io/vuln/SNYK-JS-NODEFORGE-598677<br />- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7720<br /><br />### For more information<br />If you have any questions or comments about this advisory:<br />* Open an issue in [forge](https://github.com/digitalbazaar/forge).<br />* Email us at support@digitalbazaar.com. | 0 | https://github.com/advisories/GHSA-wxgw-qj99-44c2 |
| 1067459 | axios>follow-redirects | Exposure of sensitive information in follow-redirects | follow-redirects is vulnerable to Exposure of Private Personal Information to an Unauthorized Actor | 8 | https://github.com/advisories/GHSA-74fj-2j2h-c42q |
| 1067407 | axios>follow-redirects | Exposure of Sensitive Information to an Unauthorized Actor in follow-redirects | Exposure of Sensitive Information to an Unauthorized Actor in NPM follow-redirects prior to 1.14.8. | 5.9 | https://github.com/advisories/GHSA-pw2r-vq6v-hr8c |