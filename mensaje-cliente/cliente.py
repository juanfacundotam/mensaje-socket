# Código del cliente (client.py)
import socket

# Crear un objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configurar la dirección y el puerto del servidor
HOST = '192.168.116.130'  # Cambia esto por la dirección IP del servidor
PORT = 12345

# Conectar al servidor
client_socket.connect((HOST, PORT))
print(f"Conectado al servidor en {HOST}:{PORT}")

# Enviar un mensaje al servidor
message = "Hola, Deseas aceptar la instalacion de este Software?"
client_socket.send(message.encode('utf-8'))

# Cerrar la conexión
client_socket.close()