#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# class ZyxEulerAngles:
#     def __init__(self, th):
#         self.x = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], [0, np.sin(th), np.cos(th)]])
#         self.y = np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], [-np.sin(th), 0, np.cos(th)]])
#         self.z = np.array([[np.cos(th), -np.sin(th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])




th1 = np.pi / 3
th2 = np.pi / 4


Rz1 = np.array([[np.cos(th1), -np.sin(th1), 0], [np.sin(th1), np.cos(th1), 0], [0, 0, 1]])
d1  = np.array([[0, 0, 0]]).T

htemp  = np.array([[0, 0, 0, 1]])
temp = np.concatenate([Rz1, d1], 1)
H1 = np.concatenate([temp, htemp])



Rzt = np.identity(3)
dt  = np.array([[2, 0, 0]]).T

htemp  = np.array([[0, 0, 0, 1]])
temp = np.concatenate([Rzt, dt], 1)
Ht = np.concatenate([temp, htemp])

print(H1)
# print(np.dot(H1, Ht))

Rz2 = np.array([[np.cos(th2), -np.sin(th2), 0], [np.sin(th2), np.cos(th2), 0], [0, 0, 1]])
d2  = np.array([[2, 0, 0]]).T

htemp  = np.array([[0, 0, 0, 1]])
temp = np.concatenate([Rz2, d2], 1)
H2 = np.concatenate([temp, htemp])

print(H2)


Rz3 = np.identity(3)
d3  = np.array([[2, 0, 0]]).T

htemp  = np.array([[0, 0, 0, 1]])
temp = np.concatenate([Rz3, d3], 1)
H3 = np.concatenate([temp, htemp])




Hee = np.array([[0, 0, 0, 1]]).T

print(np.dot(np.dot(np.dot(H1,H2),H3), Hee))
