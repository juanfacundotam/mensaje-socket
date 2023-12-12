# Código del cliente (client.py)
import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Crear un objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configurar la dirección y el puerto del servidor
HOST = '192.168.116.130'  # Cambia esto por la dirección IP del servidor
PORT = 12345

# Conectar al servidor
client_socket.connect((HOST, PORT))
print(f"Conectado al servidor en {HOST}:{PORT}")

# Llave secreta para AES (debe ser la misma en el servidor y el cliente)
key = b'mi_llave_secreta'  # Cambia esto por la misma llave que en el servidor

# Enviar un mensaje al servidor
message = "Hola, servidor! Soy el cliente."

# Agregar relleno a los datos para que tengan una longitud múltiplo de 16
block_size = 16
padding_length = block_size - (len(message) % block_size)
padded_message = message + chr(padding_length) * padding_length

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()

# Cifrar el mensaje con relleno
encrypted_message = encryptor.update(padded_message.encode('utf-8')) + encryptor.finalize()
client_socket.send(encrypted_message)

# Cerrar la conexión
client_socket.close()