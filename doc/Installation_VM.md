<!--suppress HtmlRequiredAltAttribute -->
<a href="https://www.ensicaen.fr">
<img src="https://www.ensicaen.fr/wp-content/uploads/2017/02/LogoEnsicaen.gif" width="256" >
</a>

Projet VM - Installation des Machines Virtuelles
================================================
ANODEAU Boris
HANICOTTE Flavien
HERVET Marine

# Description

Ce document regroupe l'ensemble des procédures à effectuer pour mettre en place
les machines virtuelles constituant la base nécessaire au développement du
projet.
Deux logiciels seront utilisés dans cette partie : GNS3 et VirtualBox.

# Installation des logiciels GNS3 et VirtualBox

Les deux logiciels sont téléchargeables gratuitement en ligne et ne
nécessitent pas de license pour fonctionner.
*(Se référer aux différents tutoriels disponibles sur les sites respectifs des
logiciels pour l'instalation sur vos systèmes - À titre indicatif, la
configuration initiale à été réalisée sur Linux Ubuntu 20.04 LTS)*

# Configuration des différents machines virtuelles nécessaires

Il est nécessaire de configurer 3 machines virtuelles différentes afin de
pouvoir mettre en place le réseau souhaité. Les trois machines virtuelles sont
configurées sur Linux Ubuntu 20.04 LTS et sont respectivement nommées *User*,
*Target* et *Attacker*. Les 3 configurations sont identiques : Configuration
minimale lors de l'installation, password identique au username de la machine
avec Log In automatique. Une fois les mises à jour initiales effectuées lors
du premier lancer de chaque VM, installer le package net-tools afin d'avoir
accès aux utilitaires réseaux :
```
sudo apt install net-tools
```
Une fois le package installé, valider la bonne instalation avec la commande
ifconfig :
```
ifconfig
```
Seront alors affichés les interfaces réseaux de la machine ainsi que ses 
configurations. Fermer alors les VM et modifier l'interface réseaux dans la
configuration depuis VirtualBox en mettant le *network adapter* en **non
attached** *(Force la reconfiguration en cas de coupure manuelle depuis GNS3)*.

La configuration des VM est alors terminée.

# Création du projet sur GNS3 et Importation de VM

Lancer GNS3 et créer un nouveau projet nommé **Projet_VM**. Il faut alors
importer un router qui servira de server DHCP lors des simulations
*(Considérant le cas d'une grande entreprise, le serveur DHCP est un router)*.
Le router choisi est un router Cisco C7200, modèle très répandu et très utilisé
en entreprise. L'image du router ainsi que sa configuration sont obtenables sur
le cours de Réseau 1A de la filière informatique de l'ENSICAEN, la
configuration étant détaillée dans la trâme de TP.

Une fois le router importé, il faut alors importer les 3 VM crées lors de la
phase précédente *(NB : GNS3 VM n'a pas été utilisé lors de cette
configuration. Si vous souhaitez utiliser GNS3 VM, reportez-vous à la
documentation adéquate)* :
```
Edit --> Preferences --> VirtualBox VMs --> New
```
Si VirtualBox est lancé lors de la phase d'importation, GNS3 peut détecter les
différentes VM et les importer automatiquement.

Une fois les VM importées, il faut modifier la cofiguration réseau pour
permettre à GNS3 d'utiliser tout adapteur configuré par GNS3 *(Criticité à
approfondir)* :
```
Edit --> Preferences --> VirtualBox VMs --> Edit --> Network
```
Il ne reste alors plus qu'à checker la case correspondante, ce qui conclut la
configuration.

# Setup du réseau et du routeur

Importer une VM de chaque type, 2 switch Ethernet, 1 router Cisco C7200, un
"cloud" *(qui symbolise la connexion à un réseau plus large, extérieur à
l'entreprise)* ainsi que 3 VPCS *(symbolisant 2 utilisateurs et un serveur)*.
Relier les différents composants comme indiqué sur la figure ci-contre :

**Insert Network Image**

La seule contrainte à vérifier est de relier le switch central à l'interface
FastEthernet 0/0 du routeur Cisco.

Une fois ceci fait, il ne reste qu'à configurer le serveur DHCP. Après avoir
lancé le réseau :
```
# conf t
# service dhcp
# ip dhcp pool LAN
# network 192.168.1.0 255.255.255.0
# lease 7 (Optionnal)
# default-router 192.168.1.1
# ex
# int fa0/0
# ip address 192.168.1.1 255.255.255.0
# no shut
# ex
# copy running-config startup-config
# exit
```
La configuration du router termine la configuration du réseau.

# Test de Fonctionnalité

Lancer le réseau sur GNS3, ce qui lance également les 3 VM. Sur chacune de VM,
lancer la commande `ifconfig` : Pour la première interface de chaque VM, vous
devez voir normalement voir une addresse IP associée de la forme 192.168.1.X,
avec X compris entre 2 et 254.

Si aucune IP n'est associé à la VM lors de l'exécution de `ifconfig`, utilisez
alors la commande `dhclient -r` pour raffraichir la configuration du serveur
DHCP local, avant de relancer `ifconfig`, qui devrait normalement donner le
résultat du premier cas.

Si aucune des solutions ne fonctionne, merci de contacter le service client
(#Boris).
