#!/usr/bin/env python
# coding: utf-8

# In[97]:


class parsingastring:
    def __init__(self, input_string):
        self.input_string = input_string #input string
        self.variable = ""
        self.values = ()
        self.parameters = {}
        
    def parse(self):
        Initial_split = self.input_string.strip() 
        ip_split = Initial_split.split('=', maxsplit=1)
        self.variable = ip_split[0] #capturing the var
        custom_split = ip_split[1].replace(',','')
        custom_split.replace(" ",'')
        custom_split=custom_split.split()
        Second_split = custom_split 
        self.values = tuple(float(x) for x in Second_split[0:3]) #capturing the values
        Third_split = Second_split[3].split(" ") #finally splitting to capture the paramteres
        k = 3
        for i in range(int((len(Second_split)-3)/3)):
            self.parameters[i] = Second_split[k+i] + Second_split[k+i+1] + Second_split[k+i+2]
            k = k+2
    def print_parts(self):
        print(self.variable)
        print(self.values)
        print(self.parameters)
        
        
        
    


# In[98]:


sample3 =  "s = -2, -15, -0.5, x = 2, rz = s y = 30"
Output = parsingastring(sample3)
Output.parse()
Output.print_parts()

