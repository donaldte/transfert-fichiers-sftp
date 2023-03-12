import pysftp # Importer la bibliothèque pysftp pour la connexion et le transfert de fichiers SFTP

# Définir les informations de connexion SFTP
hostname = "example.com" # Remplacer par l'adresse du serveur SFTP
username = "user" # Remplacer par le nom d'utilisateur pour la connexion SFTP
password = "password" # Remplacer par le mot de passe pour la connexion SFTP

# Créer une connexion SFTP avec les informations d'identification définies
with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
    
    # Accéder au répertoire distant pour télécharger ou envoyer des fichiers
    with sftp.cd('/remote/directory'):
        
        # Télécharger un fichier du serveur SFTP au répertoire local
        sftp.get('file.txt') # Remplacer par le nom du fichier à télécharger
        
        # Envoyer un fichier du répertoire local au serveur SFTP
        sftp.put('file.txt') # Remplacer par le nom du fichier à envoyer
