cmake_minimum_required(VERSION 3.0.2)
project(digit_sensor)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
)

catkin_python_setup()

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/digit
  scripts/list_digits
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
