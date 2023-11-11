#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:44:38 2023

@author: alper
"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

rospy.init_node('engele_carpmadan_dur')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def algilama(bilgi):
    algilama_bilgisi= bilgi.ranges
    
    if min(algilama_bilgisi) < 1.0:
        dur = Twist()
        dur.linear.x = 0.0
        dur.angular.z = 0.0
        pub.publish(dur)
    else:
        yurume_hiz= Twist()
        yurume_hiz.linear.x = 0.2
        pub.publish(yurume_hiz)

rospy.Subscriber('/scan', LaserScan,algilama)
rospy.spin()
    

    
   
    
   
   