### Docker basic commands

```
$docker build -t $(tag_name) $(file_path)
$docker run -it --rm $(tag_name)
-it instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container. 
--rm Automatically remove the container when it exits
$docker exec $(NAMES) bash
exec help you to bash into the existing docker environments
$docker ps
showing all the running docker container
$docker images
showing all the existing docker images
$docker image rm $(tag_name) --force
remove the docker images
$docker rmi $(docker images --filter "dangling=true" -q --no-trunc) --force
remove the docker images with none tag and also make sure they are not used by other images

```



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

