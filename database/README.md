

## Déploiement

Il est indiqué dans cette section du projet tous les composants nécessaires à la recolte des données et la mise en place de l'architecture de la donnée.

Les composants sont basés sur des containers Docker que nous allons construire.


## Prérequis

* **Docker** doit être installé correctement sur le poste de même que **docker-compose** pour exécution. 



## Containers

Trois containers sont construit mais seul 2 sont indispensables :

* **mariadb** qui contient un moteur de base de données MariaDB. C'est dans ce container que les données seront stockées et recupérée pour les differents cas d'usage.

* **python_launcher** qui va exécuter le script python permetant la collecte des données des marchés à travers les API de Binance. Il crée le schéma de la base de dennées s'il n'existe pas et l'alimente avec les données historiques et celles collecter par streamming. Le script demeurre en arrière plan pour la collecte en streaming.

Le dernier container n'est pas insdispensable et pourrait être arrété à tout moment.

* **adminer** il offre une interface web leger permettant l'exploitation et l'administration de la base de donnée.


## Etapes de construction

    cd ./database
    docker-compose build 
    docker-compose up -d



