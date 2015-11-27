cmake_minimum_required(VERSION 2.4.6)
project(cyton)

find_package(Boost REQUIRED COMPONENTS system thread)
find_package(catkin REQUIRED COMPONENTS roscpp std_msgs message_generation actionlib actionlib_msgs)

include_directories(${catkin_INCLUDE_DIRS})
include_directories(${PROJECT_SOURCE_DIR}/include)
link_directories(${PROJECT_SOURCE_DIR}/lib/)

add_message_files(
  FILES
  cytonActionFeedback.msg
  cytonActionGoal.msg
  cytonAction.msg
  cytonActionResult.msg
  cytonFeedback.msg
  cytonGoal.msg
  cytonResult.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime)

add_executable(actinSE_node src/actinSE_node.cpp)
add_dependencies(actinSE_node ${PROJECT_NAME}_gencpp)

add_executable(guide_frame_node src/guide_frame_node.cpp)
add_dependencies(guide_frame_node ${PROJECT_NAME}_gencpp)

add_executable(cyton_move_node src/cyton_move.cpp)
add_dependencies(cyton_move_node ${PROJECT_NAME}_gencpp)

add_executable(set_home src/set_home.cpp)
add_dependencies(set_home ${PROJECT_NAME}_gencpp)

add_executable(hardware_node src/hardware_node.cpp)
add_dependencies(hardware_node ${PROJECT_NAME}_gencpp)

add_executable(send_joints src/send_joints.cpp)
add_dependencies(send_joints ${PROJECT_NAME}_gencpp)

target_link_libraries(actinSE_node ecFoundCore ecActinSE ecCytonHardwareInterface ${catkin_LIBRARIES}) 
target_link_libraries(guide_frame_node ecFoundCore ecActinSE ${catkin_LIBRARIES})
target_link_libraries(cyton_move_node ecFoundCore ecActinSE ecCytonHardwareInterface ${catkin_LIBRARIES}) 
target_link_libraries(set_home ${catkin_LIBRARIES})
target_link_libraries(hardware_node ecFoundCore ecActinSE ecCytonHardwareInterface ${catkin_LIBRARIES})
target_link_libraries(send_joints ecFoundCore ecActinSE ecCytonHardwareInterface ${catkin_LIBRARIES})

