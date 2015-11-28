//     Copyright (c) 2009-2012 Energid Technologies. All rights reserved. ////
//
// Filename:    guide_frame_node.cpp
//
// Description: example action client which send EE Coordinates from a guide_frame.txt file
//
// guideframe.txt:File contains EE coordinates arranged in the following fashion
//   0.2
//   0.2
//   0.6
//   ,
//   0.5
//   0.45
//   0.84
//   ,
//   ...
// 
//
/////////////////////////////////////////////////////////////////////////


//ROS headers
#include "ros/ros.h"
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <cyton/cytonAction.h>
#include <boost/thread.hpp>

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

//int j=0;

int 
main (
     int argc,
     char **argv 
     )

{
   ros::init(argc ,argv,"cyton1");
   actionlib::SimpleActionClient<cyton::cytonAction>ac("cyton",true);
   ROS_INFO("Waiting for action server to start.");
   ac.waitForServer();
   ROS_INFO("Action server started ,sending guide frame");

   string line;
   string dot (",");
   string::iterator it;

   string var1,var2,var3;

   //reading guide frame from a text file .The path of the text file can acess through CYTON_EE_FILE ,and send to actinSE server

   ifstream myfile(getenv("CYTON_EE_FILE"));
   double pos[3];
   int i=0;

   if(myfile.is_open())
   {
      while(myfile.good())
      {
         getline(myfile,line);
	 char *line1;
	 line1=new char[line.size()+1];
         strcpy(line1,line.c_str());
       	 if(strcmp(line1,","))
       	 {
	    pos[i]=atof(line1);
	    i++;
	    if (i==3)
            {
	       bool finished_before_timeout ;
 	       if(!(pos[0]==0 && pos[1]==0 && pos[2]== 0))
  	       {
  	          cyton::cytonGoal goal;
 		  goal.position.push_back(pos[0]);
  		  goal.position.push_back(pos[1]);
  		  goal.position.push_back(pos[2]);
                  goal.time=20;
 		  goal.eeindex=2;
 		  goal.home=0;
  		  goal.gripper_value=-1.57079;
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

            else
	    {
            }

		
	
	 }
      }
   }
myfile.close();
return 0;
}



