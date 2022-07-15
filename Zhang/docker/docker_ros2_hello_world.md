### System Requirements

software requirements: docker, two host machines connected within local network

### Set up environment

1. build docker image

```
docker build -t ${tag_name} -f ros2.Dockerfile .
```

2. run docker image and set docker network as host, open a docker bash


```
docker run -it --net=host ${tag_name}
```

3. open a new terminal on your host machine, copy the ros2 package

```
docker cp py_pubsub/ ${conatiner_name}:/root/ros_ws/src
```

4. go to the docker bash

```
cd ~/ros_ws && colcon build
source ~/.bashrc
```

repeat the same procedure on host machine 2

### Test Results



```
ros2 run py_pubsub talker
```

![](../images/docker/talker.png)

```
ros2 run py_pubsub listenr
```

![](../images/docker/listener.png)
