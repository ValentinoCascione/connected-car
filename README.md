Projet: Voiture télécommandée à distance

Membres du groupe et tâches:
- Tresor RASHIDI SALUMU => Création du React (partie Front)
- Wahid AMINI => Création du React (partie Front)
- Constant RODRIGUEZ => Création du code Python (côté back)
- Valentino CASCIONE => Mise en place de la robotique côté Raspberry (branchements moteurs, ...)

Tâche commune qui nous a demandé réfléxion:
- Mise en place du Websocket afin que le serveur (Python) intercepte chaque requête en direct envoyée par le client (React). 
Cette technologie fût une bonne idée car elle permet de commander la voiture en temps réel, sans décalage entre l'envoie de la requête et la retour du serveur (Ce qui ce serait produit avec une simple connection à une api et une communication en ajax et en reqûete http).


1. Technologies:
- Côté Front => React
- Côté Back => Python
- Protocole de connexion entre Front et Back => WebSocket
- Protocle de connection au rasp à distance (réseau local et externe) => SSH

Pourquoi Python?
- Ce language s'adapte bien au raspberry et l'import des ports GPIO est facilité

Pourquoi React?
- COnnaissances sur le framework de la part du groupe

Le back se trouve dans le dossier 'back-python'
Le Front correspond au reste

Ce que la voiture peut faire:
- Avancer
- Reculer
- Tourner (gauche et droite)

Vidéo qui prouve ces compétences:
https://youtu.be/ruGWMs4c5Cs