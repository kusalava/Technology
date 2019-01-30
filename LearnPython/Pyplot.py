import matplotlib.pyplot as plt

x = [1950,1951,1952,1953,1956,1958,1960,1965,1970]
y = [1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.10]
plt.plot(x,y)
plt.scatter(x,y)
plt.xlabel('year')
plt.ylabel('population')
plt.title('World population projections')
#plt.yticks([1950,1951,1952,1953,1956,1958,1960,1965,1970],['1y','2y','3y','4y','5y','6y','7y','8y','9y','10y'])
#plt.xticks([1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10],['1y','2y','3y','4y','5y','6y','7y','8y','9y','10y'])
plt.show()