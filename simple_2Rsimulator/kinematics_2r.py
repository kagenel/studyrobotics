#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import robotmodel_2r

def kinematics(robot):
    c1 = math.cos(robot.joints[0].angle)
    s1 = math.sin(robot.joints[0].angle)
    c12 = math.cos(robot.joints[0].angle + robot.joints[1].angle)
    s12 = math.sin(robot.joints[0].angle + robot.joints[1].angle)

    robot.joints[1].position[0] = robot.links[0].length * c1
    robot.joints[1].position[1] = robot.links[0].length * s1

    robot.eejoint.position[0] = robot.links[0].length * c1 + robot.links[1].length * c12
    robot.eejoint.position[1] = robot.links[0].length * s1 + robot.links[1].length * s12
