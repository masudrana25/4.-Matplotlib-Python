import matplotlib.pyplot as plt
import numpy as np

age_1 = np.random.randint(15,30, (100)) 
age_2 = np.random.randint(15,35, (100))
# print(age_1) ; print(age_2)

bins_data = [15,20,25,30,35]
plt.hist([age_1,age_2],color = ['red','y'], orientation='vertical', align='mid', rwidth=0.8, bins = bins_data, histtype='bar', label=['Age 1','Age 2'] )
plt.legend()
plt.show()