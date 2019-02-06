import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

year = list(range(1999,2010))
film = [2,2,2,3,1,1,2,3,4,1,4]
drowning = [109,102,102,98,85,95,96,98,123,94,102]
cordf = pd.DataFrame({'Years':year,
                      'Swimming pool drownings':drowning,
                      'Nicholas Cage':film})
cordf.to_csv(r'data.csv')

df = pd.read_csv('data.csv')
year = df['Years']
film = df['Nicholas Cage']
drowning = df['Swimming pool drownings']

ax1 = plt.gca()
line1, = ax1.plot(year, drowning, marker='o')
ax2 = ax1.twinx()
line2, = ax2.plot(year, film, marker='o', c='r')
ax1.set_ylim([80,140])
ax2.set_ylim([0,6])
ax1.set_ylabel("Swimming pool drownings")
ax2.set_ylabel("Nicholas Cage")
ax2.legend((line1, line2),
           ("Swimming pool drownings", "Nicholas Cage"))
plt.title("Number of people who drowned by falling into a pool\n correlates with\n Films Nicolas Cage appeared in")
plt.figtext(0.51, 0.71, "Correlation: 66.6% (r=0.666004)")
plt.savefig('task21.png')
plt.show()
