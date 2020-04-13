import math
import numpy as np
from franka_robot import FrankaRobot

if __name__ == '__main__':
    dh_params = np.array([[0, 0.333, 0, 0],
                          [0, 0, -math.pi/2, 0],
                          [0, 0.316, math.pi/2, 0],
                          [0.0825, 0, math.pi/2, 0],
                          [-0.0825, 0.384, -math.pi/2, 0],
                          [0, 0, math.pi/2, 0],
                          [0.088, 0, math.pi/2, 0],
                          [0, 0.107, 0, 0],
                          [0, 0.1034, 0, 0]])
    fr = FrankaRobot('franka_robot.urdf', dh_params, 7)
    joints = [0, -math.pi/4, 0, -3*math.pi/4, 0, math.pi/2, math.pi/4]
    urdf_fk = fr.forward_kinematics_urdf(joints)[-1]

    dh_fk = [[ 7.06788607e-01, -7.06788607e-01,  2.99955002e-02,  3.10514607e-01],
    [-7.07106781e-01, -7.07106781e-01, -8.91816715e-17, -7.42078226e-17],
    [ 2.12100216e-02, -2.12100216e-02, -9.99550034e-01,  5.01097479e-01],
    [0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]

    print(np.allclose(urdf_fk, dh_fk))