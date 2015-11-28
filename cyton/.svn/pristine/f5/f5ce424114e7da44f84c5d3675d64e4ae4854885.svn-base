//     Copyright (c) 2009-2012 Energid Technologies. All rights reserved. ////
//
// Filename:    send_joints.cpp
//
// Description: Action client send joint values and joint rates to hardware_node
//
// Contents:    Example code to move cyton to some joints
//
/////////////////////////////////////////////////////////////////////////


//ROS Headers
#include "ros/ros.h"
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <cyton/cytonAction.h>
#include <boost/thread.hpp>

//System headers
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cstring>
#include <stdlib.h>



using namespace std;

//global variables
bool finished_before_timeout ;



int 
main 
    (
    int argc,
    char **argv
    )

{
   ros::init(argc ,argv,"cyton1");
   actionlib::SimpleActionClient<cyton::cytonAction>ac("cyton",true);
   ROS_INFO("Waiting for hardware_node to start.");
   ac.waitForServer();
   ROS_INFO("Hardware node started ,sending JointValues and Joint Rates");

   //three arbitary value to send
   cyton::cytonGoal goal;
   cyton::cytonGoal goal1;
   cyton::cytonGoal goal2;


   //first goal ..joint values =0
   for(int i=0;i<9;i++)
   {
      goal.position.push_back(0);
   }
   for(int i=0;i<9;i++)
   {
      goal.rate.push_back(0.9);
   }
 
   goal.time=10;
   goal.gripper_value=1.57079;
   goal.gripper_rate =0.5;


   //sending goal
   ac.sendGoal(goal);
   //delay 
   sleep(5);

 
   //waiting for result for 3 sec
   finished_before_timeout = ac.waitForResult(ros::Duration(10000));

  
   if(finished_before_timeout)
   {
      ROS_INFO("Joint Values send ");
   }
   else
   {
      ROS_INFO("Joint Values not send");
   }

   //second goal =all values are set to 1 in radians	
   ROS_INFO("Waiting for hardware_node to start.");
   ac.waitForServer();
   ROS_INFO("Hardware node started ,sending JointValues and Joint Rates");

 
   for(int i=0;i<9;i++)
   {
      goal1.position.push_back(1);
   }
   for(int i=0;i<9;i++)
   {	
      goal1.rate.push_back(0.9);
   }
 
   goal1.time=20;

   goal1.gripper_value=0;
   goal1.gripper_rate =0.5;
   //sending goals
   ac.sendGoal(goal1);

   sleep(5);

   //waiting for result from ActionServer for 3 sec
   finished_before_timeout = ac.waitForResult(ros::Duration(10000));


   if(finished_before_timeout)
   {
      ROS_INFO("Joint Values send ");
   }
   else
   {
      ROS_INFO("Joint Values not send");
   }
   

   //Running third goal 
   ROS_INFO("Waiting for hardware_node to start.");
   ac.waitForServer();
   ROS_INFO("Hardware node started ,sending JointValues and Joint Rates");

   for(int i=0;i<9;i++)
   {
      goal2.position.push_back(0.23);
   }
   for(int i=0;i<9;i++)
   {	
      goal2.rate.push_back(0.9);
   }
 
   goal2.time=20;
 
   goal2.gripper_value=1.57079;
   goal2.gripper_rate =0.5;

   ac.sendGoal(goal2);
  
   finished_before_timeout = ac.waitForResult(ros::Duration(10000));

   //waiting for result for 3 sec
   if(finished_before_timeout)
   {
      ROS_INFO("Joint Values send ");
   }
   else
   {
      ROS_INFO("Joint Values not send");
   }
 
return 0;
}



