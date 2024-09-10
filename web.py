from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
    if self.path == "/":
        # Leer el contenido del archivo home.html
        with open("home.html", "r") as file:
            content = file.read()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))
    else:
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("<h1>Error 404: Página no encontrada</h1>".encode("utf-8"))

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