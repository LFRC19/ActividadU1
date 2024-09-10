from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    contenido = {
    '/': """<html><h1>Página de Inicio</h1></html>""",
    '/proyecto/1': """<html><h1>Web Estática - App de recomendación de libros</h1></html>""",
    '/proyecto/2': """<html><h1>Web App - MeFalta, que película o serie me falta ver</h1></html>""",
    '/proyecto/3': """<html><h1>Web App - Foto22, web para gestión de fotos</h1></html>"""
}

def do_GET(self):
    if self.path in contenido:
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(contenido[self.path].encode("utf-8"))
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