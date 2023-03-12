# Transfert de Fichiers SFTP

Ce programme utilise la bibliothèque pysftp pour se connecter et transférer des fichiers SFTP. Il commence par définir les informations de connexion SFTP telles que l'adresse du serveur, le nom d'utilisateur et le mot de passe. Ensuite, il utilise la méthode Connection de la bibliothèque pysftp pour se connecter au serveur SFTP.

Une fois connecté, le programme utilise la méthode cd de la bibliothèque pysftp pour accéder au répertoire distant pour télécharger ou envoyer des fichiers. Il utilise ensuite la méthode get de la bibliothèque pysftp pour télécharger un fichier du serveur SFTP au répertoire local, ou la méthode put de la bibliothèque pysftp pour envoyer un fichier du répertoire local au serveur SFTP.

Il est important de noter que pour utiliser le protocole SFTP, le serveur SFTP doit être configuré pour permettre ce type de transfert de fichier. Assurez-vous également d'avoir les autorisations nécessaires pour télécharger ou envoyer des fichiers sur le serveur SFTP.