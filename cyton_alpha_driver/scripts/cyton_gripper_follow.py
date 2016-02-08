#! /usr/bin/env python

import roslib
import rospy
import math

from cyton.msg import cytonAction, cytonActionGoal, cytonGoal

import actionlib

# import actionlib_tutorials.msg
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
# from motoman_msgs.srv import CmdJointTrajectoryEx
from control_msgs.msg import (
    FollowJointTrajectoryAction,
    FollowJointTrajectoryGoal,
    FollowJointTrajectoryFeedback,
    FollowJointTrajectoryResult
)

#from servo_device import Controller
#from unigripper_msgs.srv import *

#
#Action server to receive MoveIt goals and 
#Action client to send to cyton hardware_node
#
class CytonActionServer(object):
  # create messages that are used to publish feedback/result
  _feedback = FollowJointTrajectoryFeedback()
  _result   = FollowJointTrajectoryResult()
  _cyton_goal = cytonGoal()

  def __init__(self, name):
    self._action_name = name
    print name
    self._names = ['claw_left', 'claw_right']
    self._state = JointState(name = self._names, position = [0]*len(self._names))
    print self._state.position
    # self._joint_limits = {'shoulder_base':{'min':0,'max':1.57,'vel':.4}}
    # print self._joint_limits
    self._as = actionlib.SimpleActionServer(self._action_name, FollowJointTrajectoryAction, execute_cb=self.execute_cb, auto_start = False)
    self._as.start()
    
    #cyton action client
    #self.client = actionlib.SimpleActionClient('cyton', cytonAction)
    #rospy.loginfo('Cyton Action Client start.')    
 
    print "@@@@@@@@@@@@@ Initial head_hinge position = ", self._state.position[0]

  def execute_cb(self, goal):
    rospy.loginfo('Received Trajectory')
#     ## helper variables
    r = rospy.Rate(20)
    success = True
#    print "I'm executing and I got the goal", goal
        
    trajectory = goal.trajectory
    current_point = trajectory.points[0]
     
     # start executing the action
    for i in xrange(0, len(trajectory.points)):
      # check that preempt has not been requested by the client
      if self._as.is_preempt_requested():
        rospy.loginfo('%s: Preempted' % self._action_name)
        self._as.set_preempted()
        success = False
        break
      
      print "Gripper Controller: Executando:[%f,%f]" % (trajectory.points[i].positions[0],trajectory.points[i].positions[1])  
      self._state.position[0] = trajectory.points[i].positions[0]
      self._state.position[1] = trajectory.points[i].positions[1]
      
      #rospy.loginfo('wait Hardware node start...')
      #self.client.wait_for_server()
      #rospy.loginfo('Hardware node started.')
      #self.client.send_goal(self._cyton_goal)
      #finished_before_timeout = self.client.wait_for_result(rospy.Duration(1))
      # publish the feedback
      # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
      r.sleep()
    
    if success:
      self._as.set_succeeded(self._result)
      rospy.loginfo("SUCCESS!!!")
    else:
      rospy.loginfo("FAILURE :( :( :(")
      
#end execute_cb
if __name__ == '__main__':
  rospy.init_node('cyton_gripper_driver')

  action = CytonActionServer('/claw_controller/gripper_action')

  pub = rospy.Publisher('/joint_states', JointState, queue_size=2)
  rate = rospy.Rate(10) # 10hz

  while not rospy.is_shutdown():
    action._state.header.stamp = rospy.Time.now()
    pub.publish(action._state)
    rate.sleep()

