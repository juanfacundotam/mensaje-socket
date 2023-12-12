# Código del servidor (server.py)
import socket
import subprocess
import platform
import ctypes

# Crear un objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configurar la dirección y el puerto
HOST = '0.0.0.0'  # Escuchar en todas las interfaces de red
PORT = 12345

# Vincular el socket al puerto y empezar a escuchar
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}")

# Esperar a que un cliente se conecte
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

# Recibir datos del cliente
data = client_socket.recv(1024)
message = data.decode('utf-8')
print(f"Mensaje recibido: {message}")

# Mostrar un mensaje emergente en Windows usando ctypes
if platform.system() == 'Windows':
    ctypes.windll.user32.MessageBoxW(0, message, "Mensaje del Servidor", 1)
else:
    print("No se admite la visualización de mensajes emergentes en sistemas que no sean Windows.")

# Cerrar la conexión
client_socket.close()
server_socket.close()