'''
Created on Jul 20, 2017

@author: deocampo
'''
import mxnet as mx


a = mx.sym.Variable('a')
b = mx.sym.Variable('b')
c = 2 * a + b
print(c)

e = c.bind(mx.cpu(), {'a': mx.nd.array([1,2]), 'b':mx.nd.array([2,3])})
y = e.forward()
print(y)



