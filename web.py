from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
    # Recoger los valores de los headers del request
    host = self.headers.get('Host')
    user_agent = self.headers.get('User-Agent')

    # Responder con un código 200
    self.send_response(200)

    # Agregar los headers de la respuesta
    self.send_header("Content-Type", "text/html")
    self.send_header("Server", "CustomPythonServer")
    self.send_header("Date", self.date_time_string())
    self.end_headers()

    # Escribir la respuesta en el cuerpo
    self.wfile.write(self.get_response(host, user_agent).encode("utf-8"))

def get_response(self, host, user_agent):
    # Obtener la ruta y el query string
    query_data = self.query_data()
    autor = query_data.get('autor', 'Luis Fernando Rodriguez Cruz')

    # Retornar HTML dinámico
    return f"""
    <h1>Proyecto: {self.url().path} Autor: {autor}</h1>
    <p> Host: {host} </p>
    <p> User-Agent: {user_agent} </p>
    """




if __name__ == "__main__":
    print("Starting server on port 8000")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)  # Cambiado a 8000
    print("Servidor escuchando en el puerto 8000")
    server.serve_forever()