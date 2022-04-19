import numpy as np
import time
import pymeasure
from pymeasure.instruments.lakeshore import LakeShore425
import matplotlib.pyplot as plt


gaussmeter = LakeShore425('/dev/lakeshore425')
#print(gaussmeter.field)    #Test measurement

data_list=[]
startT=time.time()
finishT=0
measureTime=204
while finishT<(startT + measureTime):
    data_list.append(gaussmeter.field)
    time.sleep(0.05)
    finishT=time.time()

data_array=np.array(data_list) 

#Plot
#data_array=data_array[::-1]           
#recorrido= np.linspace(0,4,data_array.size)         
#plt.plot(recorrido, data_array)
