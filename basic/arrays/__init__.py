'''
Created on Jul 20, 2017

@author: deocampo
'''
import mxnet as mx
import numpy as np

x = mx.nd.empty(shape=(5,3))
print(x)

x = mx.nd.zeros(shape=(5,3))
print(x.shape)

x = mx.nd.ones(shape=(5,3))
print(x.size)

x = x.asnumpy()
print(x)

b = np.array([[1,2,3,4,5], [5,6,7,8,9]], dtype=np.int64)
print(b)


