FROM arm32v7/ros:melodic-robot
ENV ARCH=arm32v7
ENV PACKNAME=robot_motion_control

RUN apt-get update && apt-get install -q -y \
		wget \
    build-essential \
    cmake


ENV CATKIN_WS=/root/ws_$PACKNAME
WORKDIR $CATKIN_WS
RUN mkdir src
