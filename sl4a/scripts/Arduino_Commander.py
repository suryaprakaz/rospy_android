from ros_android import *  #Contains the ENV_VAR_SET() functions for setting up the workspace

import rospy
import roslib
from std_msgs.msg import String
from std_msgs.msg import Int16



def talker():
    ENV_VAR_SET()
    
    pub = rospy.Publisher('talker', String, queue_size=10)
    rospy.init_node('Android_Node')
    rate = rospy.Rate(10) #10hz
    while not rospy.is_shutdown():
        msg= "Hello World! I am ROS running on Android"
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

        
