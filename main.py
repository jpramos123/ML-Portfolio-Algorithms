
from utils import *
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

if __name__ == "__main__":

    print("** US-Census **")


    us_census_data = pd.read_csv("US-Census.txt", delim_whitespace=True)
    
    points = buildPoints(us_census_data)
    data = buildData(us_census_data)

    
    l = linear(data)
    q = quadratic(data)
    plt.title('US-Census')
    plt.scatter(points[0],points[1], c='r')
    plt.plot(l[0],l[1], label='normal')
    plt.plot(q[0],q[1], label='quadratic')
    plt.xlim(1890,2010)
    plt.ylim(60,300)
    plt.legend()


    print("** Alpswater **")

    alpswater_data = pd.read_csv("alpswater.txt", delim_whitespace=True)
    
    alpswater_data.drop(columns=['Row'], inplace=True)

    points = buildPoints(alpswater_data)
    data = buildData(alpswater_data)

    l = linear(data)
    q = quadratic(data)
    plt.figure()
    plt.title('Alpswater')
    plt.scatter(points[0],points[1], c='r')
    plt.plot(l[0],l[1], label='normal')
    plt.plot(q[0],q[1], label='quadratic')
    plt.xlim(38,12)
    plt.ylim(240,175)
    plt.legend()


    print("** Books Attend Grade **")

    def f(x, y):
        return 1.28348*y + 4.03689*x + 37.3792
       
    books_data = pd.read_csv("Books_attend_grade.txt", delim_whitespace=True)

    
    data = buildData(books_data)


    l = linear(data)
    x = np.linspace(0, 4, 10)
    y = np.linspace(0, 20, 10)
    plt.figure()
    plt.title('Books Attend Grade')
    ax = plt.axes(projection='3d')
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.scatter3D(books_data.iloc[:,0], books_data.iloc[:,1], books_data.iloc[:,2],cmap='viridis')
    ax.contour3D(X, Y, Z, 50, cmap='viridis')
    plt.show()