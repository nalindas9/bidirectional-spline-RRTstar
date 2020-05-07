#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_teleop"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/install/lib/python2.7/dist-packages:/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/build" \
    "/usr/bin/python2" \
    "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/src/turtlebot3/turtlebot3_teleop/setup.py" \
    build --build-base "/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/build/turtlebot3/turtlebot3_teleop" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/install" --install-scripts="/home/nalindas9/Documents/courses/spring_2020/enpm661-planning/github/bidirectional-spline-RRTstar/adrurlbot_ws/install/bin"
