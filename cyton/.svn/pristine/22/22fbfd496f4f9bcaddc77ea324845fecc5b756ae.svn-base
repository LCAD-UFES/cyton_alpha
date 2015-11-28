//     Copyright (c) 2009-2012 Energid Technologies. All rights reserved. ////
//
// Filename:    hardware_node.cpp
//
// Description: Action server recieves Joint Information and feedback to /cyton/feedback
//
// Contents:Cyton Action class
//
/////////////////////////////////////////////////////////////////////////


#ifdef WIN32
#  define _CRTDBG_MAP_ALLOC
#  include <stdlib.h>
#  include <crtdbg.h>
#  define DEBUG_FLAGS _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF|_CRTDBG_LEAK_CHECK_DF)
#else
#  define DEBUG_FLAGS
#endif


//ROS headers
#include "ros/ros.h"
#include <actionlib/server/simple_action_server.h>
#include <cyton/cytonAction.h>

//ActinSE & cyton headers
#include <actinSE/ControlSystem.h>
#include <actinSE/EndEffector.h>
#include <actinSE/CoordinateSystemTransformation.h>
#include <cytonHardwareInterface.h>

//System headers
#include <cstring>
#include <iostream>
#include <cstring>
#include <iostream>
#include <string>



using namespace actinSE;
using namespace cyton;


EcRealVector jointAngles, jointRates;
ControlSystem control;


///CytonAction class which contains methods of ActinSE for receiving EE Coordinates and sending Joint Information
class CytonAction
												
{

public:
   ///constructor
   CytonAction(
   	      std::string name
              ):as_(
                   nh_,
 		   name,
		   boost::bind(&CytonAction::executeCB,this,_1),
		   false
                   ),
                   action_name_(
		        	name
 				)
{
   as_.start();
   jointAngles.clear();
}


///destructor
~CytonAction(void)
{
   jointAngles.clear();
}

///return status of conversion from EE to Joint Values
///@param[in] goal		(cyton::cytonGoalConstPtr) Goal message from action client have EE points ,EE type and time
EcBoolean 
testHardware
   	(
   	const cyton::cytonGoalConstPtr &goal
   	)

{
	
   for(int i=0;i<9;i++) 
   {
      ROS_INFO("Joint Angles=%f\t",goal->position[i]);
   }     
   std::cout<<"\n";
   for(int i=0;i<9;i++)
   { 
   ROS_INFO("Joint Rates=%f\t",goal->rate[i]);
   }
   //printing recieved values from send_joints node
   ROS_INFO("\n");
   ROS_INFO("goal time=%f",goal->time);
   ROS_INFO("gripper value=%f",goal->gripper_value);
   ROS_INFO("gripper rate=%f",goal->gripper_rate);
	
   //feedback position
   feedback_.position.clear();
   feedback_.rate.clear();
   for(int i=0;i<9;i++)
   {
      feedback_.position.push_back(goal->position[i]);
   }
   //feedback joint rates
   for(int i=0;i<9;i++)
   {
      feedback_.rate.push_back(goal->rate[i]);
   }

   //feedback gripper values
   feedback_.gripper_feed_value=goal->gripper_value;
   feedback_.gripper_feed_rate=goal->gripper_rate;
	
      
   as_.publishFeedback(feedback_);  

   if(as_.isPreemptRequested() || ! ros::ok())
   {
      ROS_WARN("Preempted");
      as_.setPreempted();
         
   }
  else
  {
     result_.position.clear();
     result_.position.push_back(0); 
  }

 
return EcTrue;
}





///execute when a goal recieves from Action client
///@param[in] goal 		(cyton::cytonGoalConstPtr) It has goal value such as jointValues ,EE type and time
void 
executeCB(
         const cyton::cytonGoalConstPtr &goal
         )
{
   
   
   	
   //Calling hardware function with goal
   if(testHardware(goal))
   {
      ROS_INFO( "Test passed.\n");
      as_.setSucceeded(result_);
   }
   else
   {
    ROS_ERROR("Test failed.\n");
    as_.setAborted(result_);
   }

  

}

protected:

///ROS Node handle Object
ros::NodeHandle nh_;
///ActionServer class
actionlib::SimpleActionServer<cyton::cytonAction>as_;
///action name
std::string action_name_;
///feedback value class
cyton::cytonFeedback feedback_;
///result values class
cyton::cytonResult result_;
 


};


int 
main(
    int argc,
    char** argv
    )

{

//ros initialisation
ros::init(argc,argv,"cyton");


//Starting action and spin
CytonAction cyton(ros::this_node::getName());
ros::spin();


return 0;
}
