#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist


last_command = Twist()
linear_speed_setpoint = 0
rotational_speed_setpoint = 0




#load the pru talker c++ library
def load_pru_lib(libname)




def send_command




class motor
    ki = 0.001
    kp = 1
    kd = 0
    id = 0

    def set_speed(self, speed)

def sanitize_cmd(vel_cmd)
    #limit the values based on loaded parameters, add logging
    return limit_cmd



def motor_vel_callback(vel_cmd)
    last_command = vel_cmd



def decompose_twist_to_track(vel_cmd, side)
    linear_component = vel_cmd.linear.x * conv_ms_to_trackspeed
    rotational_component = vel_cmd.angular.z * conv_radsec_to_trackspeed
    if side == "left":
        rotational_component = rotational_component*-1
    return linear_component + rotational_component


def robot_control():
    rospy.init_node("robot_motion_control")

    #loop here
    while True:
            #get the last last_command
            clean_command = sanitize_cmd(last_command)
            left_motor
            #0.1 ms superloop time
            sleep(0.1)


    rospy.spin()



if __name__ == '__main__':
    try:
        robot_control()
    except rospy.ROSInterruptException:
        pass
