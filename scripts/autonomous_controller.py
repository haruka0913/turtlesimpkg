#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#初期設定

cmd_vel = Twist()
cmd_vel.linear.x = 2.0
cmd_vel.angular.z = 0.0

pose = Pose()
x = 0
y = 0

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y
    #rospy.loginfo(f"x={pose.x},y={pose.y}")

def update_cmd_vel():
    global cmd_vel
    cmd_vel.linear.x = 0.0
    cmd_vel.angular.z = 2.0

def autonomous_controller():
    rospy.init_node('autonomous_controller')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, update_pose)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        update_cmd_vel()
        pub.publish(cmd_vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        autonomous_controller()
    except rospy.ROSInterruptException:
        pass