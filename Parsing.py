#!/usr/bin/env python
# coding: utf-8

# In[46]:


class parsingastring:
    def __init__(self, input_string):
        self.input_string = input_string
        self.variable = ""
        self.values = ()
        self.parameters = {}
        
    def parse(self):
        Initial_split = self.input_string.split("=",1)
        self.variable = Initial_split[0]
        Second_split = Initial_split[1].split(",",3)
        self.values = tuple(float(x) for x in Second_split[0:3])
        Third_split = Second_split[3].split(" ")
        k = 1
        for i in range(int(len((Third_split))/3)):
            self.parameters[i] = Third_split[k+i] + Third_split[k+i+1] + Third_split[k+i+2]
            k = k+2
    def print_parts(self):
        print(self.variable)
        print(self.values)
        print(self.parameters)
        
        
        
    


# In[47]:


sample3 =  "theta = 2, 15, 0.05, x = 2 rz = theta, y = 30 z = 10"
Output = parsingastring(sample3)
Output.parse()
Output.print_parts()

