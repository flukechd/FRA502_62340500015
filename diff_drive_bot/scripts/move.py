#!/usr/bin/env python3
import rospy
import speech_recognition as sr
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
import time
# this method will make the robot move to the goal location
def move_to_goal(xGoal, yGoal,angle):
    # define a client for to send goal requests to the move_base server through a SimpleActionClient
    ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    # wait for the action server to come up
    while (not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()

    # set up the frame parameters
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # moving towards the goal*/

    goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = angle
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal location ...")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(120))

    if (ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("You have reached the destination")
        return True

    else:
        rospy.loginfo("The robot failed to reach the destination")
        return False


if __name__ == '__main__':
    rospy.init_node('map_navigation', anonymous=False)
    x_goal1 = -2.564
    x_goal2 = 3.995
    x_goal3 = 3.114
    x_goal4 = -2.304
    x_goalh = -4.993
    x_goal5 = -2.603
    y_goal1 = 2.365
    y_goal2 = 2.522
    y_goal3 = -1.709
    y_goal4 = -2.229
    y_goalh = 0.0043
    y_goal5 = 0.109
    angle1 = 1.57
    angle2 = -1.593
    angle3 = -1.564
    angleh = 0.001
    angle4 = 1
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print(source)
        print("start")
        # playsound("signal.mp3")
        audio = r.record(source, duration=5)  # บันทึกเสียง 5 วินาท
        # print(type(audio))# ี
        print("finish")
        # playsound("signal.mp3")
        # print(audio)
    try:
        text = r.recognize_google(audio, language = 'en')
        print(text)
    except:
        text = "Try again please"
    if "room a" in text:
        move_to_goal(x_goal1, y_goal1,angle1)
        print('go to room A')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "B" in text or "b" in text:
        move_to_goal(x_goal2, y_goal2,angle2)
        print('go to room B')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "C" in text or"c" in  text:
        move_to_goal(x_goal3, y_goal3,angle3)
        print('go to room C')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "room d" in text:
        move_to_goal(x_goal4, y_goal4,angle1)
        print('go to room d')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
