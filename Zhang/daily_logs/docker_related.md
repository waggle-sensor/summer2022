### Docker remote running 

On remote machine, start docker daemon

```
systemctl status docker
systemctl stop docker
dockerd -H tcp://0.0.0.0:2375
```

On local machine, 

```
docker -H tcp://$(ip):2375 run -it --rm images
```

