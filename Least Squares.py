

import matplotlib.pyplot as plt

import numpy as np

from scipy import stats
x=[5,7,10,12,15,17,20,25]
Lt=[17.8216667,19.4833333,23.31,26.1633333,28.7066667,30.3733333,32.88833333,36.585]

y=[i**2 for i in Lt]
'''slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(slope)
print(intercept)
plt.scatter(x,y)
Y=[i*slope+intercept for i in x]
plt.plot(x,Y)
plt.show()'''
import numpy as np
import pandas as pd


def linear_lsf(x,y):
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    x_sq_bar = np.mean([i**2 for i in x])
    x_bar_sq = x_bar**2
    xy = []
    for i in range(len(x)):
        xy.append(x[i]*y[i])
    xy_bar = np.mean(xy)
    x_bar_y_bar = x_bar*y_bar
    b = (xy_bar - x_bar_y_bar)/(x_sq_bar - x_bar_sq)
    a = y_bar - b*x_bar
    
    #Error table
    err_table = pd.DataFrame(columns=['x','y','y^p','e','e^2'])
    err_table['x'] = x
    err_table['y'] = y
    err_table['y^p'] = [a + b*i for i in x]
    err_table['e'] = err_table['y'] - err_table['y^p']
    err_table['e^2'] = err_table['e']**2
#     print(err_table)

    #Error Calculation
    n = len(x)
    e_sum = err_table['e'].sum()
    err_y = err_table['e^2'].sum()/(n-2)
    err_a_sq = (x_sq_bar*(err_y**2))/(n*(x_sq_bar-x_bar_sq))
    err_b_sq = (err_y)**2/(n*(x_sq_bar-x_bar_sq))
    err_a = err_b_sq**(1/2)
    err_b = err_a_sq**(1/2)

    err_result = pd.DataFrame(columns=['Quantity','Value'])
    err_result['Quantity'] = ['Sum of e','err_y','err_b_sq','err_a_sq','err_b','err_a']
    err_result['Value'] = [e_sum,err_y,err_b_sq,err_a_sq,err_b,err_a]
    
    return b,a

def data_plot(b,a,x,y,x_label,y_label,fig_name,save_plot):
    x_line = np.linspace(min(x),max(x),1000)
    y_line = [a+b*i for i in x_line]
    plt.plot(x_line,y_line)
    plt.scatter(x,y,c='orange')
    eq = f'${y_label} = {round(a,8)} + {round(b,8)}{x_label}$'
    t1= plt.text(max(x)*0.50, max(y)*0.100, r"{}".format(eq), fontsize=12)
    t1.set_bbox(dict(facecolor='white', edgecolor='black'))
#     plt.xticks(fontweight='bold')
#     plt.yticks(fontweight='bold')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    if save_plot:
        plt.savefig(f'data/{fig_name}.png',dpi=200)
    plt.show()


