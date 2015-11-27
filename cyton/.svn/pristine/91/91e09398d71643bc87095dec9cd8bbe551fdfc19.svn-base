//     Copyright (c) 2009-2012 Energid Technologies. All rights reserved. ////
//
// Filename:    cyton_move.cpp
//
// Description: Cyton move node controlling cyton  by subscribing  joint values from actinSE node
//
//     
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
#include <std_msgs/Float32MultiArray.h>
#include <actionlib/server/simple_action_server.h>
#include <cyton/cytonAction.h>
#include <tf/transform_broadcaster.h>

//ActinSE & Cyton headers
#include <actinSE/ControlSystem.h>
#include <actinSE/EndEffector.h>
#include <actinSE/CoordinateSystemTransformation.h>
#include <cytonHardwareInterface.h>

//System headers
#include <cstring>
#include <iostream>
#include <cstring>
#include <iostream>

#include <signal.h>

//------------------------------------------------------------------------------
// Convenience function to print a vector of joint values.
//------------------------------------------------------------------------------

static std::ostream&
operator<<
   (
   std::ostream& os,
   const EcRealVector &vec
   )
{
   size_t num = vec.size();
   if(num)
   {
      for(size_t ii=0; ii<num-1; ++ii)
      {
         os << vec[ii] << ", ";
      }
      os << vec[num-1];
   }
   return os;
}


using namespace actinSE;


//acessing cyton Bin Environmental Variable 
EcString cyton_bin_path=getenv("CYTON_BIN");
  
//acessing cytonPlugin
const EcString plugin_name=cyton_bin_path + "cytonAlphaPlugin";

//acessing cytonConfig.xml
const EcString xml_name=cyton_bin_path + "cytonAlphaConfig.xml";

//cyton hardware interface initialisation
cyton::hardwareInterface hardware(plugin_name,xml_name);




//Global decalaration of Joint angles and passed flag
EcBoolean passed;
EcRealVector jointAngle(hardware.numJoints());


void 
move_callback
(
const cyton::cytonActionFeedbackConstPtr& position
)

{

   EcRealVector angles;//,jointRates;
   cyton::cytonFeedback pos=position->feedback;
   EcReal time= pos.time;

   //angles pushback
   angles.push_back(pos.position[0]);
   angles.push_back(pos.position[1]);
   angles.push_back(pos.position[2]);
   angles.push_back(pos.position[3]);
   angles.push_back(pos.position[4]);
   angles.push_back(pos.position[5]);
   angles.push_back(pos.position[6]);
   angles.push_back(pos.gripper_feed_value);
   //angles.push_back(pos.position[8]);
/*
   //joint rates pushing to h/w
   jointRates.push_back(pos.rate[0]);
   jointRates.push_back(pos.rate[1]);
   jointRates.push_back(pos.rate[2]);
   jointRates.push_back(pos.rate[3]);
   jointRates.push_back(pos.rate[4]);
   jointRates.push_back(pos.rate[5]);
   jointRates.push_back(pos.rate[6]);
   jointRates.push_back(pos.gripper_feed_rate);
   jointRates.push_back(pos.rate[8]);
*/
/*
 //joint rates pushing to h/w
   jointRates.push_back(10);
   jointRates.push_back(10);
   jointRates.push_back(10);
   jointRates.push_back(10);
   jointRates.push_back(10);
   jointRates.push_back(10);
   jointRates.push_back(10);
   jointRates.push_back(pos.gripper_feed_rate);
   jointRates.push_back(10);
*/
   std::cout << "Angles: " << angles << std::endl ;

   hardware.setLowRate(EcTrue);

   passed = hardware.setJointCommands(time,angles,cyton::JointAngleInRadiansBiasScale/*, jointRates*/);
   if(passed)
   {
		ROS_INFO("Succesfully set the Joints");
   }
   else 
   {
		ROS_WARN("Unable to set the joints");
   }
}

void shutdown_node(int signum)
{

	ROS_INFO("Shutting down Cyton Arm\n");

	hardware.setLowRate(EcTrue);
	hardware.reset();
	hardware.waitUntilCommandFinished(10000);

	ros::shutdown();
}

int 
main
    (
    int argc,
    char **argv
    )

{
   ROS_INFO("Trying to init node");
   ros::init(argc,argv,"cyton_move_node"); // ,ros::init_options::NoSigintHandler);

   signal(SIGINT, shutdown_node);
   
   std::cout << plugin_name << std::endl;
   std::cout << xml_name << std::endl;

   ROS_INFO("Trying to init hardware");

   if(!hardware.init())
   {
      ROS_ERROR("Problem initializing Cyton hardwareInterface.\n");
   }
   else
   {
      ROS_INFO("Hardware loaded successfully");   
   }

   ros::NodeHandle n;
   cyton::cytonFeedback pos;

   ros::Subscriber sub = n.subscribe("/cyton/feedback",1000, move_callback);

   ROS_INFO("Listening to position");

   ros::spin();

   return 0;

}





