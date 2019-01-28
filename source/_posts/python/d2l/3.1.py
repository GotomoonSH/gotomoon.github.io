from mxnet import nd
from time import time

a = nd.ones(shape=1000)
b = nd.ones(shape=1000)

start = time()
c = nd.zeros(shape=1000)
# 将两个向量进行标量计算
for i in range(1000):
	c[i] = a[i]+b[i]
print(time()-start)


# 将两个向量进行矢量计算
start1 = time()
d = a+b
print(time()-start1)

