import matplotlib.pyplot as plt 
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Company profit per month')
plt.plot(x,y,linewidth=3.0,"r--","b0")
plt.show()
