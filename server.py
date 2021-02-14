from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from urllib.parse import urlparse, parse_qs
import associate
import rephrase

port = os.getenv('PORT', '8000')


class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        path = urlparse(self.path).path

        if path == '/associate':
            query = parse_qs(urlparse(self.path).query)
            word = query['word']
            if len(word) > 0:
                self.wfile.write(associate.getAssociate(word[0]).encode())
        else:
            self.wfile.write(b'Use path \'GET /associate\' or \'POST /rephrase\'')

    def do_POST(self):
        self._set_headers()
        path = urlparse(self.path).path

        if path == '/rephrase':
            content_length = int(self.headers['Content-Length'])
            query = parse_qs(self.rfile.read(content_length).decode('utf-8'))
            text = query['text']
            if len(text) > 0:
                self.wfile.write(rephrase.rephraseText(text[0]).encode())
        else:
            self.wfile.write(b'Use path \'GET /associate\' or \'POST /rephrase\'')


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class(('0.0.0.0', int(port)), MyHandler)
    print('Server started in port ' + port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
