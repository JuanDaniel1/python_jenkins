from http.server import BaseHTTPRequestHandler, HTTPServer

# Definir el manejador de solicitudes HTTP
class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar la respuesta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Escribir el contenido de la respuesta
        self.wfile.write(b"<html><body><h1>Hola, mundo!</h1></body></html>")

# Configurar el servidor web
def ejecutar_servidor():
    puerto = 5050
    direccion = ('', puerto)  # Para escuchar en todas las interfaces de red

    # Crear una instancia del servidor
    servidor = HTTPServer(direccion, MiManejador)
    print(f"Servidor iniciado en el puerto {puerto}")

    # Ejecutar el servidor hasta que se presione Ctrl+C
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido")
        servidor.server_close()

# Llamar a la función para ejecutar el servidor
if __name__ == '__main__':
    ejecutar_servidor()