import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mpg = pd.read_csv("mpg.csv")
fig, axes = plt.subplots(2, 2, figsize=(15, 15))
y = list(mpg.drv)
y = [0 if x=='f' else x for x in y]

mpg1 = mpg[mpg['drv'] == 'f']
mpg2 = mpg[mpg['drv'] == '4']
mpg3 = mpg[mpg['drv'] == 'r']

axes[0,0].scatter(mpg1.displ, mpg1.cty, c='orange', label='FWD')
axes[0,0].scatter(mpg2.displ, mpg2.cty, c='black', label='4WD')
axes[0,0].scatter(mpg3.displ, mpg3.cty, c='lightblue', label='RWD')
axes[0,0].set_ylabel("fuel economy (mpg)")
axes[0,0].set_xlabel("displacement (l)")
axes[0,0].legend()

axes[0,1].scatter(mpg1.displ, mpg1.cty, c='orange', label='FWD', alpha=0.5)
axes[0,1].scatter(mpg2.displ, mpg2.cty, c='black', label='4WD', alpha=0.5)
axes[0,1].scatter(mpg3.displ, mpg3.cty, c='lightblue', label='RWD', alpha=0.5)
axes[0,1].set_ylabel("fuel economy (mpg)")
axes[0,1].set_xlabel("displacement (l)")
axes[0,1].legend()

def rand_jitter(arr, rate=0.01):
    stdev = rate*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

def jitter(x, y, rate=0.01, c='b', label=None, alpha=1):
    return plt.scatter(rand_jitter(x, rate), rand_jitter(y, rate), c=c, label=label, alpha=alpha)

plt.sca(axes[1,0])
jitter(mpg1.displ, mpg1.cty, c='orange', label='FWD', alpha=0.5)
jitter(mpg2.displ, mpg2.cty, c='black', label='4WD', alpha=0.5)
jitter(mpg3.displ, mpg3.cty, c='lightblue', label='RWD', alpha=0.5)
axes[1,0].set_ylabel("fuel economy (mpg)")
axes[1,0].set_xlabel("displacement (l)")
axes[1,0].legend()

plt.sca(axes[1,1])
jitter(mpg1.displ, mpg1.cty, rate=0.1, c='orange', label='FWD', alpha=0.5)
jitter(mpg2.displ, mpg2.cty, rate=0.1, c='black', label='4WD', alpha=0.5)
jitter(mpg3.displ, mpg3.cty, rate=0.1, c='lightblue', label='RWD', alpha=0.5)
axes[1,1].set_ylabel("fuel economy (mpg)")
axes[1,1].set_xlabel("displacement (l)")
axes[1,1].legend()

plt.savefig('task23.png')
plt.show()