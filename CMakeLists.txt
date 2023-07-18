cmake_minimum_required(VERSION 3.5)
project(drive_motor)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_srvs REQUIRED)
find_package(canopen REQUIRED)
find_package(lely_core_libraries REQUIRED)
find_package(canopen_interfaces REQUIRED)
find_package(ros2_canopen REQUIRED)
find_package(canopen_core REQUIRED)
find_package(canopen_base_driver)
find_package(canopen_proxy_driver)

generate_dcf(single-db42)

add_executable(position_tick_client src/position_tick_motor.cpp)
ament_target_dependencies(position_tick_client
  rclcpp std_srvs canopen_interfaces)

install(TARGETS
position_tick_client
DESTINATION lib/${PROJECT_NAME})

# install launch file
install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
