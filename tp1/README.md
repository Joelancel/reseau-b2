# TP1 : Maîtrise réseau du poste

Pour ce TP, on va utiliser **uniquement votre poste** (pas de VM, rien, quedal, quetchi).

Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.

C'est un premier TP *chill*, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.

La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**

C:\Users\Joel>ipconfig -all
```
-  Adresse physique . . . . . . . . . . . : F8-89-D2-E7-0B-5F
-  Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.181
-  Masque de sous-réseau. . . . . . . . . : 255.255.240.0/24
- Masque de sous-réseau. . . . . . . . . : 255.255.240.0
 ```

☀️ **Déso pas déso**
- 10.33.64.0 
- 10.33.79.255
- 4096
---

☀️ **Hostname**

```
C:\Users\Joel>hostname
LAPTOP-DS0S1GKI
```


☀️ **Passerelle du réseau**
C:\Users\Joel>ipconfig
```
- Passerelle par défaut. . . . . . . . . : 10.33.79.254

 - C:\Users\Joel>arp -a|findstr 10.33.79.254
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  ```

---

☀️ **Serveur DHCP et DNS**

Déterminer...
```
- C:\Users\Joel>route print | findstr 10.33.79.254
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.181     30
-   C:\Users\Joel>ipconfig /all
 Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```
---

☀️ **Table de routage**

Déterminer...
```
- C:\Users\Joel>route print | findstr 10.33.79.254
          0.0.0.0          0.0.0.0     10.33.79.254 
```
---

# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`
- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`
```
Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 10ms, Maximum = 10ms, Moyenne = 10ms
    ```

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**
``` C:\Users\Joel>netstat -n
-    142.250.180.142:443 
- 443
- 10.33.76.181:55491
```
---

☀️ **Requêtes DNS**

Déterminer...
```
- à quelle adresse IP correspond le nom de domaine `www.ynov.com`
C:\Users\Joel>nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          104.26.10.233
          172.67.74.226
          104.26.11.233
 ```

- à quel nom de domaine correspond l'IP `174.43.238.89`
```
C:\Users\Joel>nslookup 174.43.289.3
Serveur :   dns.google
Address:  8.8.8.8

*** dns.google ne parvient pas à trouver 174.43.289.3 : Non-existent domain
```


---

☀️ **Hop hop hop**

```
- C:\Users\Joel>nslookup www.ynov.com
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          104.26.11.233
          104.26.10.233
          172.67.74.226
```
---

☀️ **IP publique**

Déterminer...

- l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)

---

☀️ **Scan réseau**

Déterminer...

- combien il y a de machines dans le LAN auquel vous êtes connectés

> Allez-y mollo, on va vite flood le réseau sinon. :)

![Stop it](./img/stop.png)

# III. Le requin

Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format `.pcap` donc.

Faites *clean* 🧹, vous êtes des grands now :

- livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour
  - vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark
- stockez les fichiers `.pcap` dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :

```markdown
[Lien vers capture ARP](./captures/arp.pcap)
```

---

☀️ **Capture ARP**

- 📁 fichier `arp.pcap`
- capturez un échange ARP entre votre PC et la passerelle du réseau

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

☀️ **Capture DNS**

- 📁 fichier `dns.pcap`
- capturez une requête DNS vers le domaine de votre choix et la réponse
- vous effectuerez la requête DNS en ligne de commande

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

☀️ **Capture TCP**

- 📁 fichier `tcp.pcap`
- effectuez une connexion qui sollicite le protocole TCP
- je veux voir dans la capture :
  - un 3-way handshake
  - un peu de trafic
  - la fin de la connexion TCP

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

![Packet sniffer](img/wireshark.jpg)

> *Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈*