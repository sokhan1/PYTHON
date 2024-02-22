#!/usr/bin/env python

# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Bool 
from std_msgs.msg import Float64 
from math import pi
 
pub1 = rospy.Publisher('/detected_object_angle', Float64, queue_size=1) #pub->pub1 LIDAR SENDS ANGLE OF TARGET FROM THE GROUND TO MOTOR 
pub2 = rospy.Publisher('lidar_pub_find', Bool, queue_size=1) #  pub2  LIDAR SENDS A MESSAGE TO STOP TO TURTLEBOT BECUASE FOUND OUT TARGET

def callback(msg):
    # let's define a range
    distance_min = 1.0
    distance_max = 1.5
    sum=0
    count=0
    result = Float32MultiArray()
    lidar_find=Bool()
    lidar_find.data=False
    for i, r in enumerate(msg.ranges):
        # we need object in 1 to 1.5 m range
        if distance_min < r < distance_max:
            angle = msg.angle_min + i * msg.angle_increment
            if 4.71239<=angle<2*pi:
                lidar_find.data=True
                
                sum=sum+angle 
                count=count+1        
                result.data.append(angle)            
    average=Float64()
    try:
        pub2.publish(lidar_find) 
        average.data=sum/count
        sum=0
        count=0
        
    except:
        average.data=0
        sum=0
        count=0
    pub1.publish(average) 
    print()
    
def objectDetector():
    rospy.init_node('object_detector', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback) # base_scan->scan
    rospy.spin()
if __name__ == '__main__':

    objectDetector()
