# coding: utf-8

### extract origin and axis array for each joint

import xml.etree.ElementTree as ET
# get xml root
root = ET.parse('franka_robot.urdf').getroot()
# get base namespace
root = root.getchildren()[0]

# create list to store results
results = []


for joint_elem in root.findall('joint'):
    # extract joint attributes
    joint = {}
    joint['joint_name'] = joint_elem.attrib['name'].split("}_")[1]
    joint['joint_axis'] = joint_elem.find('axis').attrib['xyz']
    joint['joint_origin_rpy'] = joint_elem.find('origin').attrib['rpy']
    joint['joint_origin_xyz'] = joint_elem.find('origin').attrib['xyz']


    results.append(joint)

print(results)

# results = [{'joint_axis': '0 0 1',
#   'joint_name': 'joint1',
#   'joint_origin_rpy': '0 0 0',
#   'joint_origin_xyz': '0 0 0.333'},
#  {'joint_axis': '0 0 1',
#   'joint_name': 'joint2',
#   'joint_origin_rpy': '${-pi/2} 0 0',
#   'joint_origin_xyz': '0 0 0'},
#  {'joint_axis': '0 0 1',
#   'joint_name': 'joint3',
#   'joint_origin_rpy': '${pi/2} 0 0',
#   'joint_origin_xyz': '0 -0.316 0'},
#  {'joint_axis': '0 0 1',
#   'joint_name': 'joint4',
#   'joint_origin_rpy': '${pi/2} 0 0',
#   'joint_origin_xyz': '0.0825 0 0'},
#  {'joint_axis': '0 0 1',
#   'joint_name': 'joint5',
#   'joint_origin_rpy': '${-pi/2} 0 0',
#   'joint_origin_xyz': '-0.0825 0.384 0'},
#  {'joint_axis': '0 0 1',
#   'joint_name': 'joint6',
#   'joint_origin_rpy': '${pi/2} 0 0',
#   'joint_origin_xyz': '0 0 0'},
#  {'joint_axis': '0 0 1',
#   'joint_name': 'joint7',
#   'joint_origin_rpy': '${pi/2} 0 0',
#   'joint_origin_xyz': '0.088 0 0'},
#  {'joint_axis': '0 0 0',
#   'joint_name': 'joint8',
#   'joint_origin_rpy': '0 0 0',
#   'joint_origin_xyz': '0 0 0.107'}]

# output to CSV (optional)
'''import pandas as pd
pd.DataFrame(results).to_csv("results.csv")'''

