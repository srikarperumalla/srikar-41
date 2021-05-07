#BEHAVIOR OF IDEAL GASES

# A gas well is producing gas with a specific gravity of 0.65 at a rate of 1.1 MMscf/day. The average reservoir pressure and temperature are 1,500 psi and 150°F. Calculate:
# a. Apparent molecular weight of the gas
# b. Gas density at reservoir conditions
# c. Flow rate in lb/day

r= float(input('\nEnter the value of specific gravity-'))
p= int(input('\nEnter the pressure-'))
t= int(input('\nEnter the temperature-'))
q= float(input('\nEnter the flow rate-'))

ma = 28.96*r          # apparent mol wt
print(ma)

dg = p*ma/(10.73*t)   # gas density
print(dg)
n = q*10**6/379.4     # no.of moles
n
m = n*ma              # flowrate in lb/day
print(m)
         

      
               
