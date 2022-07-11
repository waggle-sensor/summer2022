FROM waggle/plugin-base:1.1.1-base
LABEL description="Waggle base image containing primed ROS noetic."
LABEL maintainer="Sage Waggle Team <sage-waggle@sagecontinuum.org>"

# TODO
LABEL url=""

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV ROS_DISTRO=noetic
ENV ROS_ROOT=/opt/ros/${ROS_DISTRO}
ENV ROS_PYTHON_VERSION=3
ENV ROS_WS=/root/catkin_ws
# ENV ROS_MASTER=http://10.0.0.163:11311/

ARG ROS_MASTER_IP


# install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# install ros noetic-base
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
    apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-base \
    && rm -rf /var/lib/apt/lists/*

# source workspace
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && \
    /bin/bash -c 'source ~/.bashrc'

# install bootstrap adn other tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
  rosdep update

# creating and sourcing custom catkin workspace
RUN mkdir -p $ROS_WS/src
SHELL ["/bin/bash", "-c"]
RUN . "/opt/ros/$ROS_DISTRO/setup.bash" && cd $ROS_WS && catkin_make
RUN echo "source $ROS_WS/devel/setup.bash" >> ~/.bashrc

# # Setting ROS_MASTER_URI and ROS_IP in bashrc
# RUN echo "export ROS_MASTER_URI=http://$ROS_MASTER_URI:11311/" >> ~/.bashrc

# Installing network and ping tools
RUN apt-get update && apt-get install --no-install-recommends -y \ 
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Copy in beginner-tutorials ros-package
WORKDIR $ROS_WS
RUN mkdir src/beginner-tutorials
COPY beginner-tutorials/ src/beginner-tutorials
# RUN . "/opt/ros/$ROS_DISTRO/setup.bash" && cd $ROS_WS && catkin_make

CMD ["bash"]


## BUILD TIME INSTRUCTIONS
## sudo docker build --tag <tag-name> --build-arg ROS_MASTER_IP=<ip-address-of-master> .