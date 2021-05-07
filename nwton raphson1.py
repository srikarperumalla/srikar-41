import math

# Newton-Raphson method

# f(x)=1+x-sin(x)
# f'(x)=1-cos(x)


f= lambda x_0 : 1 + x_0 - math.sin(x_0)
fdash= lambda x_0 : 1 - math.cos(x_0)

x_0 = 1
for i in range(100):
    x_0= x_0 - f(x_0)/fdash(x_0)

root=x_0
