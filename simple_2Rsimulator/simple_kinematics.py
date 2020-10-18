#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import robotmodel_2r

# マニピュレータの設定
robo = robotmodel_2r.Robot2R()

robo.joints[0].angle = math.pi/3
robo.joints[1].angle = math.pi/4

# 順運動学
import kinematics_2r
kinematics_2r.kinematics(robo)

print(robo.eejoint.position)
# 描画
import view_2r
view_2r.view(robo)

import view_2r_3d
view_2r_3d.view(robo)
