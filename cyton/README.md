
#Cyton Alpha Ros Drive

Package catkinized to use ROS to control the Cyton Alpha arm

#Instructions

1)Install ROS

2)Clone cyton folder(cyton interface) to catkin workspace

     git clone 

-------
*Updating the instructions below
-------
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

export CYTON_INC=~/catkin_ws/src/cyton/include/
export CYTON_LIB=~/catkin_ws/src/cyton/lib/
export CYTON_BIN=~/catkin_ws/src/cyton/bin/
export CYTON_EE_FILE=~/catkin_ws/src/cyton/guide_frame.txt
export ROS_PACKAGE_PATH=~/ros:$ROS_PACKAGE_PATH



4)Add ROS_PACKAGE_PATH as shown below .

##Setting ROS_PACKAGE_PATH here

source /opt/ros/indigo/setup.bash
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/home/lentin/myworks/cyton


5)Clear or Delete the existing Makefile and replace with the following line

include $(shell rospack find mk)/cmake.mk

5)Open a terminal inside cyton folder and build using rosmake command

6)Install module using rosmake --rosdep-install command

---------------------------------------------------------------
*Updating the instructions above
---------------------------------------------------------------


##Execution 
---------

Connect the Cyton on USB port

lookup the correct port (e.g. /dev/ttyUSB0)

in the bin folder, on files: cytonConfig.xml and cytonAlphaConfig.xml. fill the field <portName>  with the correct port

give permition to cyton port

     $ sudo chmod 777 /dev/ttyUSB0

use the export command to set the correct link to libraries

     $ export LD_LIBRARY_PATH=/home/ros/catkin_ws/src/cyton/lib:/home/ros/catkin_ws/devel/lib:/home/ros/catkin_ws/devel/lib/x86_64-linux-gnu:/opt/ros/indigo/lib/x86_64-linux-gnu:/opt/ros/indigo/lib

### For EE control
-------------

     $ roslaunch cyton cyton.launch

     $ rosrun cyton  guide_frame_node

### For setting to home position
-----------------------------

     rosrun cyton set_home

### For Joint Control
-----------------

     $ roslaunch cyton hardware.launch

     $ rosrun cyton send_joints

