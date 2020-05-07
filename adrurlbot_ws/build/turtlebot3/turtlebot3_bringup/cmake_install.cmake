# Install script for directory: /home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_bringup

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/build/turtlebot3/turtlebot3_bringup/catkin_generated/installspace/turtlebot3_bringup.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_bringup/cmake" TYPE FILE FILES
    "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/build/turtlebot3/turtlebot3_bringup/catkin_generated/installspace/turtlebot3_bringupConfig.cmake"
    "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/build/turtlebot3/turtlebot3_bringup/catkin_generated/installspace/turtlebot3_bringupConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_bringup" TYPE FILE FILES "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_bringup/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup" TYPE EXECUTABLE FILES "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/devel/lib/turtlebot3_bringup/turtlebot3_diagnostics")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics"
         OLD_RPATH "/opt/ros/kinetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup/turtlebot3_diagnostics")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_bringup" TYPE PROGRAM FILES "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_bringup/scripts/create_udev_rules")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_bringup" TYPE DIRECTORY FILES "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_bringup/launch")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_bringup" TYPE FILE FILES "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_bringup/99-turtlebot3-cdc.rules")
endif()

