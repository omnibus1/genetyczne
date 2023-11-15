import numpy as np
import math
#right to left
#1number of cases
#2-3 lower/upper range of random constant
#4 number of numbers inserted into 
#5 num of variables
num_of_numbers = 10


def f11(start=-10, end=10):
    x = np.linspace(start, end, num=num_of_numbers)
    y=5*x**3-2*x**2+3*x-17
    return x,y


def f21(start=-3.14, end=3.14):

    x = np.linspace(start, end, num=num_of_numbers)
    y=np.sin(x)+np.cos(x)
    return x,y

def f31(start=-10, end=10):

    x = np.linspace(start, end, num=num_of_numbers)
    y=2*np.log(x+1)
    return x,y

def f41(start=-10, end=10):

    x = np.linspace(start, end, num=num_of_numbers)
    y = np.linspace(start, end, num=num_of_numbers)
    res=[]
    x_res=[]
    x_res_1=[]
    x_res_2=[]
    for x_val in x:
        for y_val in y:
            res.append(x_val+2*y_val)
            x_res.append(f"{x_val:.2f} {y_val:.2f}")
            x_res_1.append(f"{x_val:.2f}")
            x_res_2.append(f"{y_val:.2f}")

    return x_res,x_res_1,x_res_2,res

def f11(start=-10, end=10):

    x = np.linspace(start, end, num=num_of_numbers)
    y = np.linspace(start, end, num=num_of_numbers)
    res=[]
    x_res=[]
    x_res_1=[]
    x_res_2=[]
    for x_val in x:
        for y_val in y:
            res.append(math.sin(x_val/2)+2*math.cos(y_val))
            x_res.append(f"{x_val:.2f} {y_val:.2f}")
            x_res_1.append(f"{x_val:.2f}")
            x_res_2.append(f"{y_val:.2f}")

    return x_res,x_res_1,x_res_2,res

def f61(start=-10, end=10):

    x = np.linspace(start, end, num=num_of_numbers)
    y = np.linspace(start, end, num=num_of_numbers)
    res=[]
    x_res=[]
    x_res_1=[]
    x_res_2=[]
    for x_val in x:
        for y_val in y:
            res.append(x_val*x_val+3*x_val*y_val-7*y_val+1)
            x_res.append(f"{x_val:.2f} {y_val:.2f}")
            x_res_1.append(f"{x_val:.2f}")
            x_res_2.append(f"{y_val:.2f}")

    return x_res,x_res_1,x_res_2,res

def create_files_4(x,x1,x2,y):
    open_file = open("output.txt","w")
    for i in range(len(x)):
        open_file.write(f"{x[i]} {y[i]:.2f}\n")
        print(f"{x[i]} - {y[i]} \n")

    open_file = open("x1.txt","w")
    for i in range(len(x)):
        open_file.write(f"{x1[i]}\n".replace(".",","))

    open_file = open("x2.txt","w")
    for i in range(len(x)):
        open_file.write(f"{x2[i]}\n".replace(".",","))

    open_file = open("y.txt","w")
    for i in range(len(x)):
        open_file.write(f"{y[i]:.2f}\n".replace(".",","))


def create_files_2(x,y):
    open_file = open("output.txt","w")
    for i in range(len(x)):
        open_file.write(f"{x[i]:.2f} {y[i]:.2f}\n")
        print(f"{x[i]} - {y[i]} \n")

    open_file = open("x.txt","w")
    for i in range(len(x)):
        open_file.write(f"{x[i]:.2f}\n".replace(".",","))

    open_file = open("y.txt","w")
    for i in range(len(x)):
        open_file.write(f"{y[i]:.2f}\n".replace(".",","))


x,x1,x2,y = f61()
print(x)
create_files_4(x,x1,x2,y)




