from ros_android import *
import rospy
import roslib
from std_msgs.msg import String
from std_msgs.msg import Int16


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def main():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.Subscriber("chatter", String, callback)
    rospy.init_node('androidxolo', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

main()

        
