# -*- coding: UTF-8 -*-
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S=np.cos(X),np.sin(X)

#
# figure(figsize=(80,60), dpi=80)
# subplot(1,1,1)

plt.plot(X,C,color="blue", linewidth=1.0, linestyle="-")
plt.plot(X,S,color="green", linewidth=1.0, linestyle="-")



plt.show()