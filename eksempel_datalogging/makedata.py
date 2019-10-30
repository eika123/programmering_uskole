from pylab import *

# alle tidspunkter med måling
# 4*60*60*24*90 = 31104000
t = linspace(0, 90, 31104000)
T = 21 + t*0.03 + 3*sin(2*pi*t)

standard_deviation = 0.9

for i in range(int(1E2)):
    r = np.random.normal(scale=standard_deviation)
    print(r)