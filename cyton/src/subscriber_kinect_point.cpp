//ROS headers
#include "ros/ros.h"
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <cyton/cytonAction.h>
#include <boost/thread.hpp>
#include <cyton_kinect/point.h>

//ActinSE header
#include <actinSE/ControlSystem.h>

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

void pointCallback(const cyton_kinect::point msg){

   actionlib::SimpleActionClient<cyton::cytonAction>ac("cyton",true);
   ac.waitForServer();

   double pos[3];
   int i=0;

	    pos[0] = msg.x;
	    pos[1] = msg.y;
	    pos[2] = msg.z;
	    bool finished_before_timeout ;
 	    if(!(pos[0]==0 && pos[1]==0 && pos[2]== 0))
  	    {

		  ROS_INFO("x: %f, y: %f, z: %f",msg.x, msg.y, msg.z);
  	          cyton::cytonGoal goal;
 		  goal.position.push_back(pos[0]);
  		  goal.position.push_back(pos[1]);
  		  goal.position.push_back(pos[2]);
                  goal.time=20;	
 		  goal.eeindex=2;
 		  goal.home=0;
  		  goal.gripper_value=1.0;//-1.57079;
 		  goal.gripper_rate =1;
 		  ROS_INFO("Sending EE Cordinates %f %f %f",pos[0],pos[1],pos[2]); 
  		  ac.sendGoal(goal);
    		  finished_before_timeout = ac.waitForResult(ros::Duration(3000));
                  if(finished_before_timeout)
 		  {
 		     ROS_INFO("EE Value send ");
 		  }
 		 else
		  {
 		     ROS_INFO("EE Value not send");
		  }
  		  sleep(5);		
		  i=0;                    
	   }
}

int 
main (
     int argc,
     char **argv 
     )

{
   ros::init(argc ,argv,"cyton2");

   ROS_INFO("Waiting for action server to start.");
  
   ROS_INFO("Action server started ,sending guide frame");

   ros::NodeHandle nh;
   ros::Subscriber sub = nh.subscribe("/cyton_kinect/point",1000, pointCallback);

   ros::spin();

   return 0;
}



