

# Shisho AI chat bot

[![codecov](https://codecov.io/gh/author_name/project_urlname/branch/main/graph/badge.svg?token=project_urlname_token_here)](https://codecov.io/gh/author_name/project_urlname)
![CI](https://github.com/author_name/project_urlname/actions/workflows/main.yml/badge.svg)
![docker](https://img.shields.io/docker/pulls/edeng23/shibou-bot)

## Installation & Setup

[Install Python] https://www.dataquest.io/blog/installing-python-on-mac/

[Install pip] https://phoenixnap.com/kb/install-pip-mac

If you have Python & pip installed then check their version in the terminal or command line tools

```
python3 --version
```

```
pip --version
```

## Installing Node
https://nodejs.org/en
```
npm install
```
```
running the front with:
npm run dev
```

## Installing Flask

In your terminal run the requirements.txt file using this pip

```
pip install -r requirements.txt
```


## Running ChatBot Application in Terminal

```
cd into your directory
```

```
python BinanceRessource.py

get => http://127.0.0.1:5000/api/history
```



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

Les commandes suivantes permettent de créer (build) et demarrer les containers

    cd ./database
    docker-compose build 
    docker-compose up -d


A tout moment vous pouvez les arrrété avec la commande :

    # Assurez vous d'être positionné dans le repertoire **database**
    docker-compose stop

Vous avez la possibilité de tous reconstruire après la suppression des container avec la commande:

    # Assurez vous d'être positionné dans le repertoire database
    docker-compose down



## Structure
```text
├── Containerfile            # The file to build a container using buildah or docker
```


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

Les commandes suivantes permettent de créer (build) et demarrer les containers

    cd ./database
    docker-compose build 
    docker-compose up -d


A tout moment vous pouvez les arrrété avec la commande :

    # Assurez vous d'être positionné dans le repertoire **database**
    docker-compose stop
    
Vous avez la possibilité de tous reconstruire après la suppression des container avec la commande:

    # Assurez vous d'être positionné dans le repertoire database
    docker-compose down


