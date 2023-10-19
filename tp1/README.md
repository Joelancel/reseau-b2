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
```
- 10.33.64.0 
- 10.33.79.255
- 4096
```
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
```
PS C:\Users\joela> curl ifconfig.me
Content           : 195.7.117.146
```

---

☀️ **Scan réseau**

```C:\Users\joela>nmap -sn 10.33.64.0/20
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-19 10:34 Paris, Madrid (heure dÆÚtÚ)
Nmap scan report for 10.33.64.0
Nmap scan report for 10.33.76.181
Host is up.
Nmap done: 4096 IP addresses (827 hosts up) scanned in 173.27 seconds
```


# III. Le requin

```markdown
[Lien vers capture ARP](./captures/arp.pcap)
```

---

☀️ **Capture ARP**

- 📁 fichier `arp.pcap`
Filtrage sur Arp pour voir que les traffic arp 
[Lien vers capture ARP](./capture%20arp/arp.pcapng)

---

☀️ **Capture DNS**

Filtrage sur Dns  pour voir que les traffic dns 

[Lien vers capture ARP](./capture%20arp/dns%20cours.pcapng)
---

☀️ **Capture TCP**

Filtrage sur TCP pour voir que les traffic tcp


[Lien vers capture ARP](./capture%20arp/traffic1.pcapng)
---

