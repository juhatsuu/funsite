import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
import math


def func(x):
    return math.sin(x) / x

xmin = -100.0
xmax = 100.0
count = 200
lol = np.linspace(xmin, xmax, count)
ylist = [func(x) for x in lol]
plt.plot(lol, ylist)
fig = plt.gcf()
buf = BytesIO()
fig.savefig(buf, format='png')
buf.seek(0)
data = base64.b64encode(buf.read())
plt.show()
plt.close()
context = {'image': data.decode('utf8')}
