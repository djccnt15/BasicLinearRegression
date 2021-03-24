import numpy as np
import matplotlib.pyplot as plt

'''load data'''
data = np.loadtxt('./data.txt', skiprows=2)
# print(data)

'''set variable'''
t = data[:, 0]
v = data[:, 1]
e = data[:, 2]

'''lineFit function'''
def lineFit(x, y):
    x_bar = sum(x)/len(x)
    y_bar = sum(y)/len(y)
    b = sum((x-x_bar)*y)/sum((x-x_bar)*x)
    a = y_bar-(b*x_bar)
    return(a, b)

'''get answer'''
v0, g = lineFit(t, v)
print('v0 = %s\ng = %s' %(v0, g))

'''save answer as txt'''
answer = open('./result.txt', 'w')
answer.write('result\nv0 = %s\ng = %s' %(v0, g))
answer.close()

'''linear regression line'''
x = np.linspace(0, 25, 251)
y = v0 + (g * x)

'''plotting'''
font1 = {
    'family': 'serif',
    'color':  'darkred',
    'weight': 'normal',
    'fontstyle': 'italic'
    }

plt.figure(figsize=(15, 10))
plt.scatter(t, v, label='data')
plt.plot(x, y, label='Linear Regression', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.text(
    12, 175, '2019268005_Regression Plotting for Final',
    ha='center', va='top', size='xx-large',
    bbox=dict(facecolor='lightblue', alpha=0.4), fontdict=font1
    )
plt.title('Velocity vs time data for a falling mass', fontsize=20, style='italic', weight='heavy', color='navy')
plt.axhline(color='gray', zorder=-1)
plt.legend()
plt.savefig('./result.pdf')
plt.show()
