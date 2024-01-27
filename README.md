# SmartIptables (Iptables Automation Tool)
## Description
Cette application est un outil d'automatisation pour gérer les règles d'iptables sur les systèmes Linux. Elle permet de définir des règles pour autoriser ou bloquer le trafic sur des ports spécifiques, avec une interface en ligne de commande pour une utilisation facile et rapide.

## Fonctionnalités
Définir des règles pour autoriser ou bloquer le trafic sur des ports spécifiques.
Prise en charge des directions de trafic entrantes et sortantes.
Interface en ligne de commande simple et intuitive.

## Prérequis
Python 3.x
Accès root ou sudo pour exécuter les commandes iptables.

## Installation
Clonez le dépôt Git :

```bash
git clone (SmartIptables)[https://github.com/CloudGuardianOps/SmartIptables.git]
```
Naviguez dans le dossier du projet :

```bash
cd SmartIptables
```

## Utilisation
Exécutez le script main.py avec les arguments nécessaires. Voici quelques exemples d'utilisation :

```bash
#Autoriser le trafic sur le port 80 :
sudo python main.py --port 80 --direction INPUT --operation allow

#Bloquer le trafic sur le port 22 :
sudo python main.py --port 22 --direction OUTPUT --operation block

#Afficher l'aide :
python main.py --help
```

## Licence
Ce projet est distribué sous la licence MIT. Voir le fichier LICENSE pour plus d'informations.

## Contribution
Les contributions à ce projet sont les bienvenues. Veuillez consulter le fichier CONTRIBUTING.md pour les directives de contribution.

## Auteur
<a href="mailto://hamza.mouadden@teluq.ca">CloudGuardianOps</a>
