#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

cmd_vel = Twist()
cmd_vel.linear.x = 2.0
#cmd_vel.linear.y = 2.0
A = 2.0
B = 2.0
a = 0
b = 0
right = True
left = False
#t_up = True
#down = False

pose = Pose()

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y
    rospy.loginfo(f"x={pose.x},y={pose.y}")
"""
def update_cmd_vel():
    global cmd_vel
    global right
    global left
    global up
    global down
    
    if pose.x > 11.0:#右についたら
        right = False
        left = True
    if pose.x < 0.5:#左についたら
        right = True
        left = False
        
    if right == True:
        a = A
    if left == True:
        a = A*(-1)
        
    cmd_vel.linear.x = a
"""
def autonomous_controller():
    rospy.init_node('autonomous_controller')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, update_pose)

    rate = rospy.Rate(10) # 1秒間に10回
    while not rospy.is_shutdown():
        #update_cmd_vel()
    
        if pose.x > 11.0:#右についたら
            right = False
            left = True
        if pose.x < 0.1:#左についたら
            right = True
            left = False
        """
        if pose.y > 11.0:#上についたら
            t_up = False
            down = True
        if pose.y < 0.0:#下についたら
            t_up = True
            down = False
        """
        if right == True:
            a = A
        if left == True:
            a = A*(-1)
        """ 
        if t_up == True:
            b = B
        if down == True:
            b = B*(-1)
        """    
        cmd_vel.linear.x = a
        #cmd_vel.linear.y = b
        
        pub.publish(cmd_vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        autonomous_controller()
    except rospy.ROSInterruptException:
        pass