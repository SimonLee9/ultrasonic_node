# ultrasonic_node.py & Teensy_ultrasonic_n.ino

## ROS2 node for Ultrasonic. serial


### build
(file path : dev_ws)

- colcon build

- source install/setup.bash

### Run

file path : dev_ws

- ro2 run ultrasonic_package ultrasonic_node


### Topic 
- ros2 topic list

- ros2 echo /ultrasonic_distance
- ros2 echo /ultrasonic_distance2
