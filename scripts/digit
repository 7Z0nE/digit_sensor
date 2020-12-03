#! /usr/bin/env python
import sys
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from digit_interface.digit import Digit
from digit_interface.digit_handler import DigitHandler


if __name__=="__main__":
    rospy.init_node("digit_sensor")
    argv = rospy.myargv(argv=sys.argv)
    #serial_id = rospy.get_param('~serial_id')
    #resolution = rospy.get_param('~resolution')
    #fps = rospy.get_param('~fps')
    serial_id = argv[1]
    resolution = argv[2]
    fps = int(argv[3])


    if not len(argv) == 4:
        raise ValueError("Invalid number of arguments. Should be digit.py id resolution fps")

    if resolution == "VGA":
        if not fps in [15, 30]:
            raise ValueError("Invalid fps {} for resolution {}. Allowed {}".format(fps, resolution, [15, 30]))
    elif resolution == "QVGA":
        if not fps in [30, 60]:
            raise ValueError("Invalid fps {} for resolution {}. Allowed {}".format(resolution, fps, [30, 60]))
    else:
        raise ValueError("Unknown resolution {}".format(fps))

    digit = Digit(serial_id, rospy.get_name())
    digit.connect()
    digit.set_resolution(DigitHandler.STREAMS[resolution])
    digit.set_fps(fps)

    pub = rospy.Publisher(rospy.get_name(), Image, queue_size=1)

    rate = rospy.Rate(fps)

    bridge = CvBridge()

    while not rospy.is_shutdown():
        img = digit.get_frame()
        # msg = Image()
        # msg.header = Header(stamp=rospy.Time.now())
        # msg.step = digit.resolution["width"]
        # msg.width = digit.resolution["width"]
        # msg.height = digit.resolution["height"]
        # msg.data = img
        # msg.encoding = "rgb8"
        pub.publish(bridge.cv2_to_imgmsg(img))
        rate.sleep()




