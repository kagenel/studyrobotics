#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RobotLink:
    def __init__(self):
        self.length = 0
        self.mass = 0

class RobotJoint:
    def __init__(self):
        self.angle = 0
        self.position = [0, 0, 0]

class Robot3R:
    def __init__(self):
        self.joints = [RobotJoint() for i in range(3+2)]
        self.links  = [RobotLink() for i in range(3+1)]

        # joints[0] = BASE

        self.links[0].length = 2
        self.links[1].length = 2
        self.links[2].length = 2
        self.links[3].length = 2
        
        self.eejoint = self.joints[4]

    def set_angles(self, _angles):
        for i in range(len(joints)):
            joint[i].angle = _angles[0]
        
