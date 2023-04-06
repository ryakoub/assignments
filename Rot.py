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
        rx = np.arctan(vy/vz) #checking the angle by which we should rotate about x-axis
        rotation_axis = np.array([1, 0, 0])
        rotation_vector = rx * rotation_axis
        rotation = R.from_rotvec(rotation_vector)
        rotated_vector = rotation.apply(vector) #performing the rotation sequence
        vxp = rotated_vector[0]
        vzp = rotated_vector[2]
        ry = np.arctan(vxp/vzp) #angle by which the rotated vector should be rotated inorder to align with z-axis. 
        print("RX=",rx*180/np.pi,"RY=",ry*180/np.pi,"RZ=",0,rotated_vector)
            
    elif vx==0 and vy!=0 and vz==0: #extreme cases
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
    
    
    


# In[117]:


vector1 = (1,2,3)
vector2 = (1,1,1)
rotation_sequence(vector1)
rotation_sequence(vector2)


# In[ ]:




