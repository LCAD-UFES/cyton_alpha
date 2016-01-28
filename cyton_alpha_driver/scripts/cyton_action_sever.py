#! /usr/bin/env python

import roslib
import rospy
import math

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


class CytonAction(object):
  # create messages that are used to publish feedback/result
  _feedback = FollowJointTrajectoryFeedback()
  _result   = FollowJointTrajectoryResult()

  def __init__(self, name):
    self._action_name = name
    print name
    self._names = ['elbow_pitch', 'shoulder_base', 'shoulder_pitch', 'shoulder_yaw', 'wrist_pitch', 'wrist_roll', 'wrist_yaw']
    self._state = JointState(name = self._names, position = [0]*len(self._names))
    print self._state.position
    # self._joint_limits = {'shoulder_base':{'min':0,'max':1.57,'vel':.4}}
    # print self._joint_limits
    self._as = actionlib.SimpleActionServer(self._action_name, FollowJointTrajectoryAction, execute_cb=self.execute_cb, auto_start = False)
    self._as.start()

    #self.servo = Controller()
    #self.servo.setAccel(1, 0) # hinge servo
    #self.servo.setSpeed(1, 0) # hinge servo
    #self.set_servo_state(self._state.position[0]) # head_hinge
    print "@@@@@@@@@@@@@ Initial head_hinge position = ", self._state.position[0]

  def execute_cb(self, goal):
    rospy.loginfo('Received Trajectory')
#     ## helper variables
    r = rospy.Rate(10)
    success = True
#    print "I'm executing and I got the goal", goal
        
    trajectory = goal.trajectory
    current_point = trajectory.points[0]
    self._state.position = trajectory.points
     
     # start executing the action
    for i in xrange(0, len(trajectory.points)):
      # check that preempt has not been requested by the client
      if self._as.is_preempt_requested():
        rospy.loginfo('%s: Preempted' % self._action_name)
        self._as.set_preempted()
        success = False
        break
      self._state.position = trajectory.points[i].positions
      # publish the feedback
      # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
      r.sleep()
    
    if success:
      self._as.set_succeeded(self._result)
      rospy.loginfo("SUCCESS!!!")
    else:
      rospy.loginfo("FAILURE :( :( :(");
      
#end execute_cb
if __name__ == '__main__':
  rospy.init_node('arm_controller')

  action = CytonAction('/arm_controller/follow_joint_trajectory')

  pub = rospy.Publisher('/joint_states', JointState, queue_size=2)
  rate = rospy.Rate(10) # 10hz

  while not rospy.is_shutdown():
    action._state.header.stamp = rospy.Time.now()
    pub.publish(action._state)
    rate.sleep()

