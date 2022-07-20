### Docker basic commands

```bash
docker build -t $(tag_name) -f $(file_path)
```

```bash
docker run -it --rm $(tag_name)
```

-it instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container. 
--rm Automatically remove the container when it exits

```bash
docker exec $(NAMES) bash
```

exec help you to bash into the existing docker environments

```
docker ps
```

showing all the running docker container

```
docker images
```

showing all the existing docker images

```
docker image rm $(tag_name) --force
```

remove the docker images

```
docker rmi $(docker images --filter "dangling=true" -q --no-trunc) --force
```

remove the docker images with none tag and also make sure they are not used by other images

```
docker cp [OPTIONS] $(NAMES):SRC_PATH DEST_PATH
```

copy files from docker container to host machine

### Docker remote running 

On remote machine, start docker daemon, make sure docker is stopped

```
systemctl status docker
systemctl stop docker
dockerd -H tcp://0.0.0.0:2375
```

On local machine, 

```
docker -H tcp://$(ip):2375 run -it --rm images
```

