# cube root of a number

N=1

f = lambda x : x**3 - N
df = lambda x : 3*(x**2)

x = float(input('Enter the cube root of {N} = '))
for i in range(25):
    x = x - f(x)/df(x)

cuberoot_of_N = x

