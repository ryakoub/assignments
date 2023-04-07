#!/usr/bin/env python
# coding: utf-8

# In[115]:


from scipy.spatial.transform import Rotation as R
import numpy as np


# In[116]:


def rotation_sequence(vector):
    vx = vector[0]
    vy = vector[1]
    vz = vector[2]
    if (vx!=0 or vy!=0) and vz!=0:
        ry = np.arctan(vx/vz)
        rx = np.arctan(vy/vz)
#         if abs(ry) <= abs(rx): 
#             rotation_axis = np.array([0, 1, 0])
#             rotation_vector = -ry * rotation_axis
#             rotation = R.from_rotvec(rotation_vector)
#             rotated_vector = rotation.apply(vector)
#             vyp = rotated_vector[1]
#             vzp = rotated_vector[2]
#             rx = np.arctan(vyp/vzp)
#             print("RX=",-rx*180/np.pi,"RY=",-ry*180/np.pi,"RZ=",0,rotated_vector)

#         else:
        rotation_axis = np.array([1, 0, 0])
        rotation_vector = rx * rotation_axis
        rotation = R.from_rotvec(rotation_vector)
        rotated_vector = rotation.apply(vector)
        vxp = rotated_vector[0]
        vzp = rotated_vector[2]
        ry = np.arctan(vxp/vzp)
        print("RX=",rx*180/np.pi,"RY=",ry*180/np.pi,"RZ=",0,rotated_vector)
            
    elif vx==0 and vy!=0 and vz==0:
        if vy>0:
            print("RX=",-90,"RY=",0,"RZ=",0)
        else:
            print("RX=",90,"RY=",0,"RZ=",0)
    elif vx!=0 and vy==0 and vz==0:
        if vx>0:
            print("RX=",0,"RY=",90,"RZ=",0)
        else:
            print("RX=",0,"RY=",-90,"RZ=",0)
    elif vx!=0 and vy!=0 and vz==0:
        print("RX=",90,"RY=",45,"RZ=",0)
    
    
    


# In[ ]:




