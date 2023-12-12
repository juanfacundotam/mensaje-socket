# Código del servidor (server.py)
import socket
import subprocess
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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

# Llave secreta para AES (debe ser la misma en el servidor y el cliente)
key = b'mi_llave_secreta'  # Cambia esto por una llave segura y secreta

# Recibir datos del cliente
data = client_socket.recv(1024)
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(data) + decryptor.finalize()
message = decrypted_message.decode('utf-8')
print(f"Mensaje recibido: {message}")

# Mostrar un mensaje emergente en Kali Linux usando zenity
subprocess.run(['zenity', '--info', '--text', message])

# Cerrar la conexión
client_socket.close()
server_socket.close()