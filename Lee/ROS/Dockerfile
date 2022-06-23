FROM waggle/plugin-base:1.1.1-base1.1.1-ros-noetic

RUN sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN sudo apt install curl
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN sudo apt update
RUN apt install -y ros-noetic-desktop-full
RUN sudo apt install ros-noetic-slam-gmapping # e.g. if you use slam mapping
RUN bash source /opt/ros/noetic/setup.bash
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && source ~/.bashrc
RUN sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

ENV DEBIAN_FRONTEND=noninteractive

RUN sudo apt-get install keyboard-configuration
# debugging

RUN sudo apt-get install keyboard-configuration
RUN sudo apt install python3-rosdep
RUN sudo rosdep init && rosdep update
