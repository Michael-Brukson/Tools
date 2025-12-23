# call python -m http.server %PORT% --bind !IPV4! --directory "!DIR!"

import http.server
import socketserver
import sys

if __name__ == "__main__":
    PORT = 80
    HANDLER = http.server.SimpleHTTPRequestHandler

    print(*sys.argv[1:])

    # with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
        # print(f"Serving on port: {PORT}")
        # httpd.serve_forever()
