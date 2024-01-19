import matplotlib.pyplot as plt 
x = [ 'python' , 'c' , 'c++', 'java'] ; y = [80,70,75,83]
plt.xlabel('Programming Language', fontsize = 15) 
plt.ylabel( 'No. of Users', fontsize = 15) 
plt.title( ' Users vs Language Bar Chart', fontsize = 15)
color_name = [ 'r', 'y' , 'b' , 'g' ]
plt.bar(x,y, width = 0.4, color = color_name)
plt.show()