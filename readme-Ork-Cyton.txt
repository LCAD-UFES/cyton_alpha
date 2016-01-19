================================================================================================================
Adding Object to detect
================================================================================================================
- Creating objects
cd $PRACSYS_PATH/../object_models; rosrun object_recognition_core object_add.py -n "expo_dry_erase_board_eraser" -d "An white board eraser." --commit

- Adding object mesh 
  $ cd $PRACSYS_PATH/../object_models; rosrun object_recognition_core mesh_add.py c2f3abd5df66f7067bf8e8da40000418 expo_dry_erase_board_eraser.obj --commit
  
- Training
  $ cd $PRACSYS_PATH/../object_models; rosrun object_recognition_core training -c `rospack find object_recognition_linemod`/conf/training.ork

- Delete object
  $ cd $PRACSYS_PATH/../object_models; rosrun object_recognition_core object_delete.py e9a4f4c2f2308cd9968365268f000a5d --commit


================================================================================================================
ORK Cython object detection module
================================================================================================================
--------------
Codigo atual lego: 6c075330dbadec8af614e3cd1b003c8b 
Nome: lego
----------------

- Testing
  Open 6 terminal and run in all of then
  $ cd ~/RUTGERS/apc_main 
  $ source devel/setup.sh
  Run the following commands, one on each terminal
  $ roscore
Drive knect
  $ roslaunch freenect_launch freenect.launch 
  $ rosrun dynamic_reconfigure dynparam set /camera/driver depth_registration True
Param to detector publish the TF of object
  $ rosparam set /linemod_standalone true 
  $ rosrun tf static_transform_publisher 0 0 0 0 0 0 camera_rgb_optical_frame mapping_camera_frame 10
  $ rosrun rviz rviz --display-config src/linemod/conf/linemod_test.rviz
  $ cd $PRACSYS_PATH/../object_models; export ROS_HOME=.; rosrun object_recognition_core detection -c  `rospack find object_recognition_linemod`/conf/detection.ros.ork
  $ rosrun prx_decision_making3 prx_decision_making3_node apc_2.json

