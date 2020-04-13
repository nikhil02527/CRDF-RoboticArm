import math
import numpy as np
import re


def parse_urdf(urdf_file_path):
    '''   
    Implement a urdf file parser and extract the origins and axes for each joint into numpy arrays.
    Arguments: string
    Returns: A dictionary with numpy arrays that contain the origins and axes of each joint
    '''
    pass

class FrankaRobot():

    def __init__(self, urdf_file_path, dh_params, num_dof):
        self.robot_params = parse_urdf(urdf_file_path)
        self.dh_params = dh_params
        self.num_dof = num_dof

    def forward_kinematics_urdf(self, joints):
        '''
        Calculate the position of each joint using the robot_params
        Arguments: array of joint positions (rad)
        Returns: A numpy array that contains the 4x4 transformation matrices from the base to the position of each joint.
        '''
        pass

    def ee(self, joints):
        '''       
        Use one of your forward kinematics implementations to return the position of the end-effector.
        Arguments: array of joint positions (rad)
        Returns: A numpy array that contains the [x, y, z, roll, pitch, yaw] location of the end-effector.
        '''
        pass

    def jacobian(self, joints):
        '''       
        Calculate the end-effector jacobian analytically using your forward kinematics
        Arguments: array of joint positions (rad)
        Returns: A numpy array that contains the 6 x num_dof end-effector jacobian.
        '''
        pass

    def inverse_kinematics(self, desired_ee_pos, current_joints):
        '''       
        Implement inverse kinematics using one of the methods mentioned in class.
        Arguments: desired_ee_pos which is a np array of [x, y, z, r, p, y] which represent the desired end-effector position of the robot
                   current_joints which represents the current location of the robot
        Returns: A numpy array that contains the joints required in order to achieve the desired end-effector position.
        '''
        pass

    