# newton raphson

# f(x)=x^0.5
# df(x)=1/(2*(x^0.5))

import math

f = lambda x : math.sqrt(x)
df = lambda x : 0.5/(math.sqrt(x))

x=1

for i in range(50):
    x = x - f(x)/df(x)

root=x
        
