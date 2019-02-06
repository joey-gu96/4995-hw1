from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target
features = iris.feature_names
fig, axes = plt.subplots(4, 4, figsize=(15, 15))
plt.subplots_adjust(wspace=0,hspace=0)

for i in range(4):
    axes[i,i].hist(X[:,i], bins=20)
    
for i in range(4):
    for j in range(4):
        if i!=j:
            axes[j,i].scatter(X[:,i], X[:,j],c=y)
        if j!=3:
            axes[j,i].set_xticks([])
        if i!=0:
            axes[j,i].set_yticks([])
            
for i in range(4):
    axes[i,0].set_ylabel(features[i])
    axes[3,i].set_xlabel(features[i])
    
axes[0,0].set_yticklabels(np.arange(4,8.5,0.5))
axes[0,0].yaxis.get_ticklabels()[0].set_visible(False)

plt.savefig('task22.png')
plt.show()