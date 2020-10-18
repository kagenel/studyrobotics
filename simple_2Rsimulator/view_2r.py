#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as patches

import robotmodel_2r

def view(robo):
    joints_pos_x = [robo.joints[i].position[0] for i in range(2+1)]
    joints_pos_y = [robo.joints[i].position[1] for i in range(2+1)]

    fig = plt.figure()
    ax = plt.axes()
    ax.grid()

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    plt.plot(joints_pos_x, joints_pos_y, label="link")

    joint0_circle = patches.Circle(xy=(0, 0), radius=0.2, fc='g', ec='black', fill=False)
    joint1_circle = patches.Circle(xy=(robo.joints[1].position), radius=0.2, fc='g', ec='black', fill=False)

    ax.add_patch(joint0_circle)
    ax.add_patch(joint1_circle)

    plt.show()
