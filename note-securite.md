# Notes sécurité Docker

```bash
docker run --rm --memory 50mb p4179-167:5000/busybox free -m
```

### Sortie 

Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
559c60843878: Pull complete 
Digest: sha256:2919d0172f7524b2d8df9e50066a682669e6d170ac0f6a49676d54358fe970b5
Status: Downloaded newer image for busybox:latest
              total        used        free      shared  buff/cache   available
Mem:          15973         641       10719          10        4613       15073
Swap:          1024           0        1024

## Question : si vous définissez --memory 50mb sur votre conteneur, quelle quantité de mémoire le conteneur autorise-t-il à utiliser ?

`52428800`

```bash
docker image inspect /busybox
```

```json
[
    {
        "Id": "sha256:fc0179a204e2d895c81bf7d0a6333986cc74ddcf84cfc3859fa29c50b112a56f",
        "RepoTags": [
            "busybox:latest"
        ],
        "RepoDigests": [
            "busybox@sha256:2919d0172f7524b2d8df9e50066a682669e6d170ac0f6a49676d54358fe970b5"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2024-09-26T21:31:42Z",
        "ContainerConfig": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": null,
            "Cmd": null,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": null,
            "Cmd": [
                "sh"
            ],
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "arm64",
        "Variant": "v8",
        "Os": "linux",
        "Size": 4042190,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/36826cab1db0e63a05907794d2a03712aa4203608334afdb8376559fa193fcc2/merged",
                "UpperDir": "/var/lib/docker/overlay2/36826cab1db0e63a05907794d2a03712aa4203608334afdb8376559fa193fcc2/diff",
                "WorkDir": "/var/lib/docker/overlay2/36826cab1db0e63a05907794d2a03712aa4203608334afdb8376559fa193fcc2/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:613e5fc506b927aeaaa9c9c3dc26c0971686e566ce4cab4c4c3181f868061c60"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```

Pour le remapping, l’installation du docker doit être nettoyée en supprimant toute image précédente. La sortie de « docker image ls » doit être vide. Modifiez ensuite le fichier daemon.json situé sous « **/etc/docker/**» (si le fichier n’existe pas, créez-le). Ajoutez ensuite les lignes suivantes au fichier daemon.json

```json
{
    "userns-remap": "default"
}
```