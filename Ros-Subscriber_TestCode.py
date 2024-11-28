#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

data = None


def callbackFunction(msg):
    global data
    data = msg

    rospy.loginfo(data)
   
subscriber = rospy.Subscriber(
        name="simple_pub", data_class=Int64, callback=callbackFunction)	

if __name__ == '__main__':
    rospy.init_node("sublisher_test")

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        r.sleep()


	