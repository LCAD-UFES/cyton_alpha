//     Copyright (c) 2009-2012 Energid Technologies. All rights reserved. ////
//
// Filename:    actinSE_node.cpp
//
// Description: Action server recieves EE Coordinates and send Joint Information
//
// Contents:    CytonAction class
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
#include <string>

using namespace actinSE;
using namespace cyton;

//Joint angles and Rate vector
EcRealVector jointAngles;//, jointRates;

//ControlSystem object
ControlSystem control;


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



//acessing cyton bin Environmental variable 
EcString cyton_bin_path=getenv("CYTON_BIN");
//Reading control system file from bin folder
const EcString control_system_file=cyton_bin_path + "cyton.ecz";




///CytonAction class which contains methods of ActinSE for receiving EE Coordinates and sending Joint Information
class CytonAction
{
public:
   ///constructor
   CytonAction(
	      std::string name
 	      ) :
 		as_(nh_,name,
		     boost::bind(&CytonAction::executeCB,this,_1),
		     false),
		     action_name_(name
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




///return status of conversion from EE value to Joint Values
///@param[in] control		(actinSE::ControlSystem) ControlSystem object for joint value computation
///@param[in] goal		(cyton::cytonGoalConstPtr) Goal message from action client have EE points ,EE type and time

EcBoolean 
testControl
(
actinSE::ControlSystem& control,
const cyton::cytonGoalConstPtr &goal
)

{

   /// Pull the starting position.
   EndEffectorVector eeVec;

   ///clearing jointAngles and Rates
   jointAngles.clear();
   //jointRates.clear();

   if(!control.getParam<ControlSystem::EndEffectors>(eeVec))
   {
      ROS_INFO("Problem getting EE vector.\n");
      return EcFalse;
   }

   EndEffector& ee = eeVec[goal->eeindex];


   /// Will return EcFalse if not linked with rendering version of lib.
   EcBoolean Rendering = control.setParam<ControlSystem::Rendering>(EcTrue);

   std::cout << "Initial state of hardware = " << jointAngles << std::endl;
   EcBoolean passed = control.setParam<ControlSystem::JointAngles>(jointAngles);

   EcReal currentTime = 0.0; // time counter for this pass

   ///Recieving EE points from action client 
   Array3Vector point;
   point.push_back(Array3( goal->position[0], goal->position[1],goal->position[2]));

   for(size_t ii=0; passed && ii<point.size(); ++ii)
   {
      Array3 actualPos;
      passed &= ee.getParam<EndEffector::ActualPose>(actualPos);
      std::cout << "Starting EE position: " << actualPos << std::endl;

      
      passed &= ee.setParam<EndEffector::DesiredPose>(point[ii]);
      std::cout << "Desired EE position: " << point[ii] << std::endl;

      const EcReal totalTime = currentTime + goal->time; // Give 20s for each point
      const EcReal timeStep = 0.1;   // 10Hz update

      /// Run until we get where we want to go, or it took too long.
      while(passed && !actualPos.approxEq(point[ii], 1e-7) && currentTime <= totalTime)
      {
         // Calculate a new state at the given time.
         passed &= control.calculateToNewTime(currentTime);

         // Calculate our current time.
         currentTime += timeStep;

         // Pull updated joint angles after calculating.
         passed &= control.getParam<ControlSystem::JointAngles>(jointAngles);
         //passed &= control.getParam<ControlSystem::JointVelocities>(jointRates);
         // Pass them directly to hardware

         // Get EE position for loop check.
         passed &= ee.getParam<EndEffector::ActualPose>(actualPos);

         // Print out the results
         std::cout << "Time = " << std::setw(2) << currentTime
                   << ", Current pos (" << actualPos << ")"
                   << ", Joint angles = ";

	 //if home flag is set cyton will move to home position
	 if(goal->home==1)
	 {
 	    feedback_.position.clear();
	    for(size_t anglesize=jointAngles.size(),jj=0; jj<anglesize; jj++)
            {
               feedback_.position.push_back(1);
 
            }

	 }

	 //It will feedback actual joint values 
	 else
	 {

       	    feedback_.position.clear();
            for(size_t anglesize=jointAngles.size(),jj=0; jj<anglesize; jj++)
            {
               std::cout << std::setw(9) << jointAngles[jj] << " ";
               feedback_.position.push_back(jointAngles[jj]);
 
            }
	 }

         //feedbacking joint rates
 	/* for(size_t ratesize=jointRates.size(),jj=0;jj<ratesize; jj++)
	 {
            std::cout << std::setw(9) << jointRates[jj] << " ";
	    feedback_.rate.push_back(jointRates[jj]);
	 }*/
   

         std::cout << std::endl;
         feedback_.time=currentTime;
   

         feedback_.gripper_feed_value=goal->gripper_value;
	 feedback_.gripper_feed_rate=goal->gripper_rate;
	
         ///publishing values tp /cyton/feedback topic
         as_.publishFeedback(feedback_);  

         if(currentTime < totalTime)
         {
	    ROS_INFO("Achieved Desire Position ");         
	
         }
         else
         {
        
	    ROS_WARN("Did not achieve desired position after=%f",totalTime);
	                 
         }

	 //If there is a prempt request ,the current operation will break
         if(as_.isPreemptRequested() || ! ros::ok())
         {
            ROS_INFO("Preempted");
            as_.setPreempted();
            break;
	 }
	 else
	 {
	 }
    
   }
	 //If passed return false

         if(!passed)
         {
	    return EcFalse;
         }
	 //Passing result position to /cyton/result topic
         else 
         {
    
  	    result_.position.clear();
  	    result_.position.push_back(actualPos[0]); 
  	    result_.position.push_back(actualPos[1]); 
  	    result_.position.push_back(actualPos[2]); 
  
  	    return EcTrue;
         } 

   }

}





///execute when a goal recieves from Action client
///@param[in] goal 		(cyton::cytonGoalConstPtr) It has goal value such as jointValues ,EE type and time
void 
executeCB
(
const cyton::cytonGoalConstPtr &goal
)

{
   
   ROS_INFO("Goal from Action Client %f  %f %f",goal->position[0],goal->position[1],goal->position[2]);
  
   ///avoiding (0,0,0) value which will create collision
   if(goal->position[0]==0 && goal->position[1]==0 && goal->position[2]==0)
   {
      jointAngles.clear();
	
   }
   	
   ///Running controlsystem for getting Joint values from EE coordinates
   if(testControl(control,goal))
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
main
   (	
   int argc,
   char** argv
   )

{

ros::init(argc,argv,"cyton");

//Loading cyton.ecz file
if(!control.loadFromFile(control_system_file))
{
   ROS_ERROR( "Problem loading Cyton control system file.\n");
}
else
{
   ROS_INFO("Loaded Cyton control system file\n");
}

//Creating action and spins the node
CytonAction cyton(ros::this_node::getName());

ros::spin();

return 0;
}
