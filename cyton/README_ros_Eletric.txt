README
------


ROS-Cyton Installation Procedure on Ubuntu 
-------------------------------


1)Install ROS-electric from 

  http://www.ros.org/wiki/electric/Installation/Ubuntu

2)Copy cyton folder(ROS-Cyton interface) to user location
  For example copy cyton folder to home folder of Ubuntu


3)Add Environmental Variables such as 



CYTON_INC :=include folder path of cyton installer

CYTON_LIB :=lib folder path of cyton installer

CYTON_BIN :=bin folder path of cyton installer

CYTON_EE_FILE :=EE file path, which stores a series  of EE position .For testing purpose there are some default values  .The user can 
take any file name as EE file .It has to follow certain format like guide_frame.txt given as example inside the bin folder .
These variable has to add on the bottom of .bashrc on the home folder
Note:All paths must be system path not relative 

An example configuration is shown below
---------------------------------------

export CYTON_INC="/home/lentin/myworks/cyton/include/"
export CYTON_LIB="/home/lentin/myworks/cyton/lib/"
export CYTON_BIN="/home/lentin/myworks/cyton/bin/"
export CYTON_EE_FILE="/home/lentin/myworks/cyton/bin/guide_frame.txt"



4)Add ROS_PACKAGE_PATH as shown below .

#Setting ROS_PACKAGE_PATH here

source /opt/ros/electric/setup.bash
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/home/lentin/myworks/cyton


5)Clear or Delete the existing Makefile and replace with the following line

include $(shell rospack find mk)/cmake.mk

5)Open a terminal inside cyton folder and build using rosmake command

6)Install module using rosmake --rosdep-install command




Execution 
---------


For EE control
liberar porta chmod 777 /dev/ttyUSB
Pegar library certa
export LD_LIBRARY_PATH=/home/ros/catkin_ws/src/cyton/lib:/home/ros/catkin_ws/devel/lib:/home/ros/catkin_ws/devel/lib/x86_64-linux-gnu:/opt/ros/indigo/lib/x86_64-linux-gnu:/opt/ros/indigo/lib

-------------
roslaunch cyton cyton.launch
rosrun cyton  guide_frame_node

For setting to home position
-----------------------------
rosrun cyton set_home

For Joint Control
-----------------

roslaunch cyton hardware.launch
rosrun cyton send_joints

