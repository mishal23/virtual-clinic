
# ZAP Scanning Report




## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 0 |
| Low | 37 |
| Informational | 0 |

## Alert Detail


  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://activity-stream-icons.services.mozilla.com/v1/icons.json.br](https://activity-stream-icons.services.mozilla.com/v1/icons.json.br)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `public,max-age=3600`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://activity-stream-icons.services.mozilla.com/v1/icons.json.br](https://activity-stream-icons.services.mozilla.com/v1/icons.json.br)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://shavar.services.mozilla.com/downloads?client=navclient-auto-ffox&appver=62.0&pver=2.2](https://shavar.services.mozilla.com/downloads?client=navclient-auto-ffox&appver=62.0&pver=2.2)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Web Browser XSS Protection Not Enabled
##### Low (Medium)
  
  
  
  
#### Description
<p>Web Browser XSS Protection is not enabled, or is disabled by the configuration of the 'X-XSS-Protection' HTTP response header on the web server</p>
  
  
  
* URL: [http://127.0.0.1:8000/appointment/list/](http://127.0.0.1:8000/appointment/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/update/](http://127.0.0.1:8000/profile/update/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/favicon.ico](http://127.0.0.1:8000/favicon.ico)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/medicalinfo/patient/](http://127.0.0.1:8000/medicalinfo/patient/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/prescription/list/](http://127.0.0.1:8000/prescription/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/calendar/](http://127.0.0.1:8000/appointment/calendar/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/robots.txt](http://127.0.0.1:8000/robots.txt)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/new/](http://127.0.0.1:8000/message/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/sitemap.xml](http://127.0.0.1:8000/sitemap.xml)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/list/](http://127.0.0.1:8000/message/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
Instances: 16
  
### Solution
<p>Ensure that the web browser's XSS filter is enabled, by setting the X-XSS-Protection HTTP response header to '1'.</p>
  
### Other information
<p>The X-XSS-Protection HTTP response header allows the web server to enable or disable the web browser's XSS protection mechanism. The following values would attempt to enable it: </p><p>X-XSS-Protection: 1; mode=block</p><p>X-XSS-Protection: 1; report=http://www.example.com/xss</p><p>The following values would disable it:</p><p>X-XSS-Protection: 0</p><p>The X-XSS-Protection HTTP response header is currently supported on Internet Explorer, Chrome and Safari (WebKit).</p><p>Note that this alert is only raised if the response body could potentially contain an XSS payload (with a text-based content type, with a non-zero length).</p>
  
### Reference
* https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet
* https://blog.veracode.com/2014/03/guidelines-for-setting-security-headers/

  
#### CWE Id : 933
  
#### WASC Id : 14
  
#### Source ID : 3

  
  
  
### Cross-Domain JavaScript Source File Inclusion
##### Low (Medium)
  
  
  
  
#### Description
<p>The page includes one or more script files from a third-party domain.</p>
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `POST`
  
  
  * Parameter: `https://code.jquery.com/jquery-3.3.1.min.js`
  
  
  * Evidence: `<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js`
  
  
  * Evidence: `<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/new/](http://127.0.0.1:8000/message/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://code.jquery.com/jquery-3.3.1.min.js`
  
  
  * Evidence: `<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/calendar/](http://127.0.0.1:8000/appointment/calendar/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/update/](http://127.0.0.1:8000/profile/update/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/calendar/](http://127.0.0.1:8000/appointment/calendar/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/medicalinfo/patient/](http://127.0.0.1:8000/medicalinfo/patient/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://code.jquery.com/jquery-3.3.1.min.js`
  
  
  * Evidence: `<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/new/](http://127.0.0.1:8000/message/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/list/](http://127.0.0.1:8000/message/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `POST`
  
  
  * Parameter: `https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `POST`
  
  
  * Parameter: `https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js`
  
  
  * Evidence: `<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/prescription/list/](http://127.0.0.1:8000/prescription/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `POST`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/new/](http://127.0.0.1:8000/message/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/calendar/](http://127.0.0.1:8000/appointment/calendar/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://code.jquery.com/jquery-3.3.1.min.js`
  
  
  * Evidence: `<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>`
  
  
  
  
* URL: [http://127.0.0.1:8000/medicalinfo/patient/](http://127.0.0.1:8000/medicalinfo/patient/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js"></script>`
  
  
  
  
Instances: 91
  
### Solution
<p>Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.</p>
  
### Reference
* 

  
#### CWE Id : 829
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Cookie No HttpOnly Flag
##### Low (Medium)
  
  
  
  
#### Description
<p>A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.</p>
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/prescription/list/](http://127.0.0.1:8000/prescription/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/update/](http://127.0.0.1:8000/profile/update/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/medicalinfo/patient/](http://127.0.0.1:8000/medicalinfo/patient/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/new/](http://127.0.0.1:8000/message/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/list/](http://127.0.0.1:8000/appointment/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/calendar/](http://127.0.0.1:8000/appointment/calendar/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
Instances: 13
  
### Solution
<p>Ensure that the HttpOnly flag is set for all cookies.</p>
  
### Reference
* http://www.owasp.org/index.php/HttpOnly

  
#### CWE Id : 16
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [http://127.0.0.1:8000/message/list/](http://127.0.0.1:8000/message/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/update/](http://127.0.0.1:8000/profile/update/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/prescription/list/](http://127.0.0.1:8000/prescription/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/static/css/dashboard.css](http://127.0.0.1:8000/static/css/dashboard.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/medicalinfo/patient/](http://127.0.0.1:8000/medicalinfo/patient/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/message/new/](http://127.0.0.1:8000/message/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/list/](http://127.0.0.1:8000/appointment/list/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/appointment/calendar/](http://127.0.0.1:8000/appointment/calendar/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 14
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Password Autocomplete in Browser
##### Low (Medium)
  
  
  
  
#### Description
<p>The AUTOCOMPLETE attribute is not disabled on an HTML FORM/INPUT element containing password type input.  Passwords may be stored in browsers and retrieved.</p>
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `POST`
  
  
  * Parameter: `id_password`
  
  
  * Evidence: `<input type="password" name="password" maxlength="50" class="form-control" placeholder="Enter password here" required id="id_password">`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password_second`
  
  
  * Evidence: `<input type="password" name="password_second" maxlength="50" class="form-control" placeholder="Enter new password again" required id="id_password_second">`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password_current`
  
  
  * Evidence: `<input type="password" name="password_current" maxlength="50" class="form-control" placeholder="Enter your current password here" required id="id_password_current">`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password_first`
  
  
  * Evidence: `<input type="password" name="password_first" maxlength="50" minlength="1" class="form-control" placeholder="Enter password here" required id="id_password_first">`
  
  
  
  
* URL: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password_second`
  
  
  * Evidence: `<input type="password" name="password_second" maxlength="50" minlength="1" class="form-control" placeholder="Enter password again" required id="id_password_second">`
  
  
  
  
* URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password`
  
  
  * Evidence: `<input type="password" name="password" maxlength="50" class="form-control" placeholder="Enter password here" required id="id_password">`
  
  
  
  
* URL: [http://127.0.0.1:8000/profile/password/](http://127.0.0.1:8000/profile/password/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password_first`
  
  
  * Evidence: `<input type="password" name="password_first" maxlength="50" class="form-control" placeholder="Enter new password here" required id="id_password_first">`
  
  
  
  
Instances: 7
  
### Solution
<p>Turn off the AUTOCOMPLETE attribute in forms or individual input elements containing password inputs by using AUTOCOMPLETE='OFF'.</p>
  
### Reference
* http://www.w3schools.com/tags/att_input_autocomplete.asp
* https://msdn.microsoft.com/en-us/library/ms533486%28v=vs.85%29.aspx

  
#### CWE Id : 525
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://api.github.com/_private/browser/stats](https://api.github.com/_private/browser/stats)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `no-cache`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/7699e59a-e28e-4a83-921e-7caed91d60c3/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/7699e59a-e28e-4a83-921e-7caed91d60c3/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/9a1474a5-29fb-434c-8379-6fb4d62de525/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/9a1474a5-29fb-434c-8379-6fb4d62de525/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/9de4e638-62e4-4b0d-8da8-71764bae7ae0/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/9de4e638-62e4-4b0d-8da8-71764bae7ae0/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/144bda71-6794-4777-a7e3-2af24053b3f5/main/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/144bda71-6794-4777-a7e3-2af24053b3f5/main/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/b1eff9f5-6a78-497a-b6f7-7170114e4f10/event/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/b1eff9f5-6a78-497a-b6f7-7170114e4f10/event/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/45266154-dc46-4f6a-a896-5dcfb17f8e79/event/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/45266154-dc46-4f6a-a896-5dcfb17f8e79/event/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/363d2ad1-c14a-4910-b143-1db4c2b25541/modules/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/363d2ad1-c14a-4910-b143-1db4c2b25541/modules/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/ff8304a0-0e1b-4ac4-a2bd-6d5871fc1c61/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/ff8304a0-0e1b-4ac4-a2bd-6d5871fc1c61/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/d739ed36-8869-49e9-81c4-f1283d3e8180/event/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/d739ed36-8869-49e9-81c4-f1283d3e8180/event/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/40fc73a7-eb9e-4880-9d16-4991854ec089/main/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/40fc73a7-eb9e-4880-9d16-4991854ec089/main/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/dd1c72f6-94e2-4fe7-a83a-6cba81ab244b/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/dd1c72f6-94e2-4fe7-a83a-6cba81ab244b/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/70f119d1-7e79-4885-a923-f07729ae77d5/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/70f119d1-7e79-4885-a923-f07729ae77d5/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/d88c6416-b4b9-4f72-90f6-27898e1e2959/main/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/d88c6416-b4b9-4f72-90f6-27898e1e2959/main/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 13
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/d88c6416-b4b9-4f72-90f6-27898e1e2959/main/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/d88c6416-b4b9-4f72-90f6-27898e1e2959/main/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/144bda71-6794-4777-a7e3-2af24053b3f5/main/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/144bda71-6794-4777-a7e3-2af24053b3f5/main/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/9a1474a5-29fb-434c-8379-6fb4d62de525/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/9a1474a5-29fb-434c-8379-6fb4d62de525/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/b1eff9f5-6a78-497a-b6f7-7170114e4f10/event/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/b1eff9f5-6a78-497a-b6f7-7170114e4f10/event/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/45266154-dc46-4f6a-a896-5dcfb17f8e79/event/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/45266154-dc46-4f6a-a896-5dcfb17f8e79/event/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/363d2ad1-c14a-4910-b143-1db4c2b25541/modules/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/363d2ad1-c14a-4910-b143-1db4c2b25541/modules/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/40fc73a7-eb9e-4880-9d16-4991854ec089/main/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/40fc73a7-eb9e-4880-9d16-4991854ec089/main/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/70f119d1-7e79-4885-a923-f07729ae77d5/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/70f119d1-7e79-4885-a923-f07729ae77d5/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/9de4e638-62e4-4b0d-8da8-71764bae7ae0/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/9de4e638-62e4-4b0d-8da8-71764bae7ae0/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/7699e59a-e28e-4a83-921e-7caed91d60c3/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/7699e59a-e28e-4a83-921e-7caed91d60c3/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/dd1c72f6-94e2-4fe7-a83a-6cba81ab244b/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/dd1c72f6-94e2-4fe7-a83a-6cba81ab244b/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/d739ed36-8869-49e9-81c4-f1283d3e8180/event/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/d739ed36-8869-49e9-81c4-f1283d3e8180/event/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://incoming.telemetry.mozilla.org/submit/telemetry/ff8304a0-0e1b-4ac4-a2bd-6d5871fc1c61/health/Firefox/62.0.3/release/20181002130007?v=4](https://incoming.telemetry.mozilla.org/submit/telemetry/ff8304a0-0e1b-4ac4-a2bd-6d5871fc1c61/health/Firefox/62.0.3/release/20181002130007?v=4)
  
  
  * Method: `POST`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
Instances: 13
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://fonts.googleapis.com/css?family=Lato:400,700,400italic](https://fonts.googleapis.com/css?family=Lato:400,700,400italic)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `private, max-age=86400`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://fonts.googleapis.com/css?family=Lato:400,700,400italic](https://fonts.googleapis.com/css?family=Lato:400,700,400italic)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://assets-cdn.github.com/assets/frameworks-5aa6d9885579bb2359f66266aee26f3b.css](https://assets-cdn.github.com/assets/frameworks-5aa6d9885579bb2359f66266aee26f3b.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/compat-3c69a4d015c4208bce7a9d5e4e15a914.js](https://assets-cdn.github.com/assets/compat-3c69a4d015c4208bce7a9d5e4e15a914.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/static/fonts/inter/Inter-UI-Medium.woff](https://assets-cdn.github.com/static/fonts/inter/Inter-UI-Medium.woff)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/github-4e1b5c601c8ffb2a97df514b249fe52b.js](https://assets-cdn.github.com/assets/github-4e1b5c601c8ffb2a97df514b249fe52b.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/static/fonts/inter/Inter-UI-Regular.woff](https://assets-cdn.github.com/static/fonts/inter/Inter-UI-Regular.woff)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/frameworks-a2f69f341e3df821fdcb56e335ef9920.js](https://assets-cdn.github.com/assets/frameworks-a2f69f341e3df821fdcb56e335ef9920.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/site-3ba3ae12a2f85a6290c97a963107cc97.css](https://assets-cdn.github.com/assets/site-3ba3ae12a2f85a6290c97a963107cc97.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/github-2bf9c5ab90af2104656120603fa7ae6a.css](https://assets-cdn.github.com/assets/github-2bf9c5ab90af2104656120603fa7ae6a.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 8
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://assets-cdn.github.com/assets/site-3ba3ae12a2f85a6290c97a963107cc97.css](https://assets-cdn.github.com/assets/site-3ba3ae12a2f85a6290c97a963107cc97.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `max-age=31536000, public`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/github-2bf9c5ab90af2104656120603fa7ae6a.css](https://assets-cdn.github.com/assets/github-2bf9c5ab90af2104656120603fa7ae6a.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `max-age=31536000, public`
  
  
  
  
* URL: [https://assets-cdn.github.com/assets/frameworks-5aa6d9885579bb2359f66266aee26f3b.css](https://assets-cdn.github.com/assets/frameworks-5aa6d9885579bb2359f66266aee26f3b.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `max-age=31536000, public`
  
  
  
  
Instances: 3
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Cookie Without Secure Flag
##### Low (Medium)
  
  
  
  
#### Description
<p>A cookie has been set without the secure flag, which means that the cookie can be accessed via unencrypted connections.</p>
  
  
  
* URL: [https://github.com/](https://github.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `has_recent_activity`
  
  
  * Evidence: `Set-Cookie: has_recent_activity`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted channel. Ensure that the secure flag is set for cookies containing such sensitive information.</p>
  
### Reference
* http://www.owasp.org/index.php/Testing_for_cookies_attributes_(OWASP-SM-002)

  
#### CWE Id : 614
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Cookie No HttpOnly Flag
##### Low (Medium)
  
  
  
  
#### Description
<p>A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.</p>
  
  
  
* URL: [https://github.com/](https://github.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `has_recent_activity`
  
  
  * Evidence: `Set-Cookie: has_recent_activity`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the HttpOnly flag is set for all cookies.</p>
  
### Reference
* http://www.owasp.org/index.php/HttpOnly

  
#### CWE Id : 16
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://github.com/](https://github.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `no-cache`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://www.google.com/compressiontest/gzip.html](https://www.google.com/compressiontest/gzip.html)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `no-cache, must-revalidate`
  
  
  
  
* URL: [https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8](https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `private, max-age=0`
  
  
  
  
* URL: [https://www.google.com/async/bgasy?ei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=_fmt:jspb](https://www.google.com/async/bgasy?ei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=_fmt:jspb)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `private`
  
  
  
  
* URL: [https://www.google.com/async/ecr?ei=cD_IW6SCEcv1rQHvx6K4Bg&lei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=encoded_cache_key:ChMIpPr7z8SP3gIVy3orCh3vowhnEgIYAg,version_info:8wbPWvFMtR8ZkCukv5weOhh8F31jaBY,attempt:1,_fmt:jspb](https://www.google.com/async/ecr?ei=cD_IW6SCEcv1rQHvx6K4Bg&lei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=encoded_cache_key:ChMIpPr7z8SP3gIVy3orCh3vowhnEgIYAg,version_info:8wbPWvFMtR8ZkCukv5weOhh8F31jaBY,attempt:1,_fmt:jspb)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `private,max-age=3600`
  
  
  
  
Instances: 4
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://www.google.com/compressiontest/gzip.html](https://www.google.com/compressiontest/gzip.html)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://www.google.com/async/ecr?ei=cD_IW6SCEcv1rQHvx6K4Bg&lei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=encoded_cache_key:ChMIpPr7z8SP3gIVy3orCh3vowhnEgIYAg,version_info:8wbPWvFMtR8ZkCukv5weOhh8F31jaBY,attempt:1,_fmt:jspb](https://www.google.com/async/ecr?ei=cD_IW6SCEcv1rQHvx6K4Bg&lei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=encoded_cache_key:ChMIpPr7z8SP3gIVy3orCh3vowhnEgIYAg,version_info:8wbPWvFMtR8ZkCukv5weOhh8F31jaBY,attempt:1,_fmt:jspb)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://www.google.com/async/bgasy?ei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=_fmt:jspb](https://www.google.com/async/bgasy?ei=cD_IW6SCEcv1rQHvx6K4Bg&client=ubuntu&yv=3&async=_fmt:jspb)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8](https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 4
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Cookie Without Secure Flag
##### Low (Medium)
  
  
  
  
#### Description
<p>A cookie has been set without the secure flag, which means that the cookie can be accessed via unencrypted connections.</p>
  
  
  
* URL: [https://www.google.com/compressiontest/gzip.html](https://www.google.com/compressiontest/gzip.html)
  
  
  * Method: `GET`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/gen_204?s=web&t=aft&atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&rt=wsrt.199650,aft.8799,prt.576,sct.302](https://www.google.com/gen_204?s=web&t=aft&atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&rt=wsrt.199650,aft.8799,prt.576,sct.302)
  
  
  * Method: `POST`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8](https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8)
  
  
  * Method: `GET`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/client_204?&atyp=i&biw=1299&bih=616&ei=cD_IW6SCEcv1rQHvx6K4Bg](https://www.google.com/client_204?&atyp=i&biw=1299&bih=616&ei=cD_IW6SCEcv1rQHvx6K4Bg)
  
  
  * Method: `GET`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/gen_204?atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&s=web&t=all&imn=2&adh=&ima=1&ime=1&imeb=0&imeo=0&wh=616&scp=0&fld=1248.199951171875&sys=hc.4&rt=aft.8798,dcl.705,iml.10275,ol.23456,prt.575,xjs.18541,xjsee.18540,xjses.18342,xjsls.1685,sct.301,wsrt.199650,cst.0,dnst.0,rqst.11386,rspt.11386,sslt.188258,rqstt.188258,unt.188253,cstt.188258,dit.84&zx=1539850127322](https://www.google.com/gen_204?atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&s=web&t=all&imn=2&adh=&ima=1&ime=1&imeb=0&imeo=0&wh=616&scp=0&fld=1248.199951171875&sys=hc.4&rt=aft.8798,dcl.705,iml.10275,ol.23456,prt.575,xjs.18541,xjsee.18540,xjses.18342,xjsls.1685,sct.301,wsrt.199650,cst.0,dnst.0,rqst.11386,rspt.11386,sslt.188258,rqstt.188258,unt.188253,cstt.188258,dit.84&zx=1539850127322)
  
  
  * Method: `POST`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
Instances: 5
  
### Solution
<p>Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted channel. Ensure that the secure flag is set for cookies containing such sensitive information.</p>
  
### Reference
* http://www.owasp.org/index.php/Testing_for_cookies_attributes_(OWASP-SM-002)

  
#### CWE Id : 614
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Cookie No HttpOnly Flag
##### Low (Medium)
  
  
  
  
#### Description
<p>A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.</p>
  
  
  
* URL: [https://www.google.com/gen_204?s=web&t=aft&atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&rt=wsrt.199650,aft.8799,prt.576,sct.302](https://www.google.com/gen_204?s=web&t=aft&atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&rt=wsrt.199650,aft.8799,prt.576,sct.302)
  
  
  * Method: `POST`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/client_204?&atyp=i&biw=1299&bih=616&ei=cD_IW6SCEcv1rQHvx6K4Bg](https://www.google.com/client_204?&atyp=i&biw=1299&bih=616&ei=cD_IW6SCEcv1rQHvx6K4Bg)
  
  
  * Method: `GET`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/gen_204?atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&s=web&t=all&imn=2&adh=&ima=1&ime=1&imeb=0&imeo=0&wh=616&scp=0&fld=1248.199951171875&sys=hc.4&rt=aft.8798,dcl.705,iml.10275,ol.23456,prt.575,xjs.18541,xjsee.18540,xjses.18342,xjsls.1685,sct.301,wsrt.199650,cst.0,dnst.0,rqst.11386,rspt.11386,sslt.188258,rqstt.188258,unt.188253,cstt.188258,dit.84&zx=1539850127322](https://www.google.com/gen_204?atyp=csi&ei=cD_IW6SCEcv1rQHvx6K4Bg&s=web&t=all&imn=2&adh=&ima=1&ime=1&imeb=0&imeo=0&wh=616&scp=0&fld=1248.199951171875&sys=hc.4&rt=aft.8798,dcl.705,iml.10275,ol.23456,prt.575,xjs.18541,xjsee.18540,xjses.18342,xjsls.1685,sct.301,wsrt.199650,cst.0,dnst.0,rqst.11386,rspt.11386,sslt.188258,rqstt.188258,unt.188253,cstt.188258,dit.84&zx=1539850127322)
  
  
  * Method: `POST`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8](https://www.google.com/search?client=ubuntu&channel=fs&q=how+to+view+the+certificates+added+by+us+in+forefix&ie=utf-8&oe=utf-8)
  
  
  * Method: `GET`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
* URL: [https://www.google.com/compressiontest/gzip.html](https://www.google.com/compressiontest/gzip.html)
  
  
  * Method: `GET`
  
  
  * Parameter: `1P_JAR`
  
  
  * Evidence: `Set-Cookie: 1P_JAR`
  
  
  
  
Instances: 5
  
### Solution
<p>Ensure that the HttpOnly flag is set for all cookies.</p>
  
### Reference
* http://www.owasp.org/index.php/HttpOnly

  
#### CWE Id : 16
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://mishal23.github.io/flatly-bootstrap.css](https://mishal23.github.io/flatly-bootstrap.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://mishal23.github.io/flatly-bootstrap.css](https://mishal23.github.io/flatly-bootstrap.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `max-age=600`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://code.jquery.com/jquery-3.3.1.min.js](https://code.jquery.com/jquery-3.3.1.min.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/fonts/fontawesome-webfont.woff2?v=4.3.0](https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/fonts/fontawesome-webfont.woff2?v=4.3.0)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css](https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js](https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 3
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css](https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `max-age=31536000`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js](https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js](https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css](https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 3
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css](https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `public, max-age=31536000`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.css](https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css](https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js](https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js](https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js](https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 5
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css](https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `public, max-age=30672000`
  
  
  
  
* URL: [https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.css](https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `public, max-age=30672000`
  
  
  
  
Instances: 2
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Cross-Domain JavaScript Source File Inclusion
##### Low (Medium)
  
  
  
  
#### Description
<p>The page includes one or more script files from a third-party domain.</p>
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://code.jquery.com/jquery-3.3.1.min.js`
  
  
  * Evidence: `<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js`
  
  
  * Evidence: `<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js"></script>`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/plug-ins/1.10.7/integration/bootstrap/3/dataTables.bootstrap.js"></script>`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.8.2/fullcalendar.min.js"></script>`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js`
  
  
  * Evidence: `<script src="https://cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js`
  
  
  * Evidence: `<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.21.0/moment.min.js"></script>`
  
  
  
  
Instances: 7
  
### Solution
<p>Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.</p>
  
### Reference
* 

  
#### CWE Id : 829
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/static/css/dashboard.css](http://virtual-clinic.herokuapp.com/static/css/dashboard.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 2
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Cookie No HttpOnly Flag
##### Low (Medium)
  
  
  
  
#### Description
<p>A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.</p>
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `csrftoken`
  
  
  * Evidence: `Set-Cookie: csrftoken`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the HttpOnly flag is set for all cookies.</p>
  
### Reference
* http://www.owasp.org/index.php/HttpOnly

  
#### CWE Id : 16
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Web Browser XSS Protection Not Enabled
##### Low (Medium)
  
  
  
  
#### Description
<p>Web Browser XSS Protection is not enabled, or is disabled by the configuration of the 'X-XSS-Protection' HTTP response header on the web server</p>
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the web browser's XSS filter is enabled, by setting the X-XSS-Protection HTTP response header to '1'.</p>
  
### Other information
<p>The X-XSS-Protection HTTP response header allows the web server to enable or disable the web browser's XSS protection mechanism. The following values would attempt to enable it: </p><p>X-XSS-Protection: 1; mode=block</p><p>X-XSS-Protection: 1; report=http://www.example.com/xss</p><p>The following values would disable it:</p><p>X-XSS-Protection: 0</p><p>The X-XSS-Protection HTTP response header is currently supported on Internet Explorer, Chrome and Safari (WebKit).</p><p>Note that this alert is only raised if the response body could potentially contain an XSS payload (with a text-based content type, with a non-zero length).</p>
  
### Reference
* https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet
* https://blog.veracode.com/2014/03/guidelines-for-setting-security-headers/

  
#### CWE Id : 933
  
#### WASC Id : 14
  
#### Source ID : 3

  
  
  
### Password Autocomplete in Browser
##### Low (Medium)
  
  
  
  
#### Description
<p>The AUTOCOMPLETE attribute is not disabled on an HTML FORM/INPUT element containing password type input.  Passwords may be stored in browsers and retrieved.</p>
  
  
  
* URL: [http://virtual-clinic.herokuapp.com/](http://virtual-clinic.herokuapp.com/)
  
  
  * Method: `GET`
  
  
  * Parameter: `id_password`
  
  
  * Evidence: `<input type="password" name="password" maxlength="50" class="form-control" placeholder="Enter password here" required id="id_password">`
  
  
  
  
Instances: 1
  
### Solution
<p>Turn off the AUTOCOMPLETE attribute in forms or individual input elements containing password inputs by using AUTOCOMPLETE='OFF'.</p>
  
### Reference
* http://www.w3schools.com/tags/att_input_autocomplete.asp
* https://msdn.microsoft.com/en-us/library/ms533486%28v=vs.85%29.aspx

  
#### CWE Id : 525
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [http://detectportal.firefox.com/success.txt](http://detectportal.firefox.com/success.txt)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3
