#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import robot_model

def view(robo):
    num_joints = len(robo.joints)
    joints_pos_x = [robo.joints[i].position[0] for i in range(num_joints)]
    joints_pos_y = [robo.joints[i].position[1] for i in range(num_joints)]
    joints_pos_z = [robo.joints[i].position[2] for i in range(num_joints)]



    # 3Dでプロット
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    ax.plot(joints_pos_x, joints_pos_y, joints_pos_z, "o-", color="#00aa00", ms=4, mew=0.5)

    # 軸ラベル
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_zlim(-5,5)


    # 表示
    plt.show()
