#! /usr/bin/env python
import sys
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from digit_interface.digit import Digit


if __name__=="__main__":
    myargv = rospy.myargv(argv=sys.argv)
    serial_id = myargv[1]
    resolution = myargv[2]
    fps = myargv[3]

    if not len(sys.argv) == 4:
        raise ValueError("Invalid number of arguments. Should be digit.py id resolution fps")

    if resolution == "VGA":
        if not fps in ["15", "30"]:
            raise ValueError("Invalid fps {} for resolution {}. Allowed {}".format(resolution, fps, ["15", "30"]))
    elif resolution == "QVGA"]:
        if not fps in ["30", "60"]:
            raise ValueError("Invalid fps {} for resolution {}. Allowed {}".format(resolution, fps, ["30", "60"]))
    else:
        raise ValueError("Unknown resolution {}".format(fps))

    digit = Digit(serial_id)
    digit.set_resolution(resolution)
    digit.set_fps(int(sys.argv[2]))

    rospy.init_node("digit-{}".format(serial_id))

    pub = rospy.Publisher("/digit/{}".format(serial_id), Image, queue_size=1)

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




