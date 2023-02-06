from http.server import HTTPServer,SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
print("Server started on https://localhost:8000")
sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='certificado.crt' , keyfile='certificado.key')
httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()