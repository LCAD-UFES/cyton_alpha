
//     Copyright (c) 2009-2012 Energid Technologies. All rights reserved. ////
//
// Filename:    set_home.cpp
//
// Description: Action client which set home flag for  moving into the home position
//
// Contents:    Example code to move cyton to some joi
//
/////////////////////////////////////////////////////////////////////////


//ROS headers
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

int 
main(
    int argc,
    char **argv
    )

{
   ros::init(argc ,argv,"cyton1");
   actionlib::SimpleActionClient<cyton::cytonAction>ac("cyton",true);
   ROS_INFO("Waiting for action server to start.");
   ac.waitForServer();
   ROS_INFO("Action server started ,sending guide frame");
   cyton::cytonGoal goal;

   //setting home flag=1
   goal.home=1;
   //setting some arbitary position
   goal.position.push_back(1);
   goal.position.push_back(0);
   goal.position.push_back(1);
   goal.time=20;
   goal.eeindex=2;
  
   bool finished_before_timeout ;
   ac.sendGoal(goal);
  
   finished_before_timeout = ac.waitForResult(ros::Duration(3000));


   if(finished_before_timeout)
   {
      ROS_INFO("Moving to home position ");
   }
   else
   {
      ROS_INFO("Not moved to home postion");
   }

return 0;
}



