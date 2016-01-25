#Cyton Alpha

Status
------

This package is currently under development.

Tutorial
------

####Simulation

```
roslaunch cyton_alpha_bringup bringup.launch
roslaunch cyton_alpha_moveit_config moveit_cyton_alpha_sim.launch
```

####Real Robot

- MoveIt! and Cyton real robot
  
This lauch starts MoveIt!, the controllers and the action server to comunicate MoveIt with cyton.

```
  roslaunch cyton_alpha_driver moveit_cyton_alpha_real.launch
```




