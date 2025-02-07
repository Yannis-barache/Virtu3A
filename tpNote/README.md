# TP Note Virtualisation
## 1ère partie: Déploiement de l'application

### Les urls 

Il faut d'avoir faire le pont pour accéder à l'application.

### Commandes pour faire le pont 

```bash
ssh -L 8080:172.16.7.10:80 -N o22204443@acces-tp.iut45.univ-orleans.fr
```

#### Liste des urls

- [http://utilisateurs.localhost](http://utilisateurs.localhost:8080)
- [http://fortune.localhost](http://fortune.localhost:8080)



### Commandes pour l'API flask

#### POST d'une nouvelle valeur

```bash
curl -X POST http://flask.localhost/kv/1/ma_cle/ma_valeur
```

#### GET d'une valeur

```bash
curl http://flask.localhost/kv/1/ma_cle
```

#### DELETE d'une valeur

```bash
curl -X DELETE http://flask.localhost/kv/1/ma_cle
```

