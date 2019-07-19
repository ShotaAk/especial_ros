#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import Float32


def main():
    rospy.init_node("serial_monitor")

    pub = rospy.Publisher("serial_data", Float32, queue_size=1)

    with serial.Serial("/dev/ttyUSB0", 115200, timeout=1) as ser:
        while not rospy.is_shutdown():
            try:
                try:
                    line = ser.readline()
                    pub.publish(float(line.replace('"','')))
                except ValueError:
                    print "Error"
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

