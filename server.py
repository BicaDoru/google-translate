import socket
import threading

translations = {
    "hello": {"es": "hola", "fr": "bonjour", "de": "hallo"},
    "goodbye": {"es": "adiós", "fr": "au revoir", "de": "auf Wiedersehen"},
    "cat": {"es": "gato", "fr": "chat", "de": "Katze"},
    "dog": {"es": "perro", "fr": "chien", "de": "Hund"},
    "tree": {"es": "árbol", "fr": "arbre", "de": "Baum"},
    "car": {"es": "coche", "fr": "voiture", "de": "Auto"},
    "house": {"es": "casa", "fr": "maison", "de": "Haus"},
    "city": {"es": "ciudad", "fr": "ville", "de": "Stadt"},
    "flower": {"es": "flor", "fr": "fleur", "de": "Blume"},
    "book": {"es": "libro", "fr": "livre", "de": "Buch"},
    "pen": {"es": "pluma", "fr": "stylo", "de": "Stift"},
    "table": {"es": "mesa", "fr": "table", "de": "Tabelle"},
    "chair": {"es": "silla", "fr": "chaise", "de": "Stuhl"},
    "computer": {"es": "computadora", "fr": "ordinateur", "de": "Computer"},
    "screen": {"es": "pantalla", "fr": "écran", "de": "Bildschirm"},
    "phone": {"es": "teléfono", "fr": "téléphone", "de": "Telefon"},
    "television": {"es": "televisión", "fr": "télévision", "de": "Fernseher"},
    "mirror": {"es": "espejo", "fr": "miroir", "de": "Spiegel"},
    "window": {"es": "ventana", "fr": "fenêtre", "de": "Fenster"},
    "door": {"es": "puerta", "fr": "porte", "de": "Tür"},
    "bed": {"es": "cama", "fr": "lit", "de": "Bett"},
    "bathroom": {"es": "baño", "fr": "salle de bain", "de": "Badezimmer"},
    "shoe": {"es": "zapato", "fr": "chaussure", "de": "Schuh"},
    "sock": {"es": "calcetín", "fr": "chaussette", "de": "Socke"},
    "hat": {"es": "sombrero", "fr": "chapeau", "de": "Hut"},
    "glove": {"es": "guante", "fr": "gant", "de": "Handschuh"},
    "coat": {"es": "abrigo", "fr": "manteau", "de": "Mantel"},
    "jacket": {"es": "chaqueta", "fr": "veste", "de": "Jacke"},
    "pants": {"es": "pantalones", "fr": "pantalon", "de": "Hose"},
    "shirt": {"es": "camisa", "fr": "chemise", "de": "Hemd"},
    "socks": {"es": "calcetines", "fr": "chaussettes", "de": "Socken"},
    "shorts": {"es": "pantalones cortos", "fr": "short", "de": "Kurze Hose"},
    "glasses": {"es": "gafas", "fr": "lunettes", "de": "Brille"},
    "watch": {"es": "reloj", "fr": "montre", "de": "Uhr"},
    "ring": {"es": "anillo", "fr": "bague", "de": "Ring"},
    "necklace": {"es": "collar", "fr": "collier", "de": "Halskette"},
    "bracelet": {"es": "pulsera", "fr": "bracelet", "de": "Armband"},
    "earrings": {"es": "aretes", "fr": "boucles d'oreilles", "de": "Ohrringe"},
    "bag": {"es": "bolso", "fr": "sac", "de": "Tasche"},
    "wallet": {"es": "cartera", "fr": "portefeuille", "de": "Brieftasche"},
    "key": {"es": "llave", "fr": "clé", "de": "Schlüssel"},
    "doorbell": {"es": "timbre de la puerta", "fr": "sonnette", "de": "Türklingel"}
    
}

def handle_client(client_socket, addr):
    print(f"Accepted connection from: {addr[0]}:{addr[1]}")
    while True:
        data = client_socket.recv(1024).decode('utf-8').strip()
        print(data)
        if not data:
            break
        word, lang = data.split()
        if word in translations and lang in translations[word]:
            translation = translations[word][lang]
        else:
            translation = "I don't know this word/language. Try another one"
        client_socket.send(f"{lang}: {translation}\n".encode('utf-8'))
    client_socket.close()

host = '172.19.23.203'
port = 8886

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server started on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
