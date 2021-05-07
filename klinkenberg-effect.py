# Klinkenberg Effect

# The permeability of a core plug is measured by air. Only one measurement is made at a mean pressure of 2.152 psi.
# The air permeability is 46.6 md. Estimate the absolute permeability of the core sample. Compare
# the result with the actual absolute permeability of 23.66 md.

# 1. kg = kl + c(1/pm)
# 2. c = b*kl
# 3. 6.9*kl^0.64 + pm*kl - pm*kg = 0

# newton raphson method
# k(i+1) = k(i) - f(ki)/f'(ki)
# f(ki) = 6.9*ki^0.64 + pm*ki - pm*kg
# f'(ki) = 4.416*ki^-0.36 + pm

k = float(input('\nEnter the actual absolute permeability:'))
pm = float(input('\nEnter the mean pressure:'))
kg = float(input('\nEnter the gas permeability:'))
           
while abs(6.9*k**0.64 + pm*k - pm*kg)>0.01:
      k = k - ((6.9*k**0.64 + pm*k - pm*kg)/(4.416*k**(-0.36) + pm))

print(f'The final value of k is: {k}')


