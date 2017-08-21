# MXNet Modeling (Python) Sandbox

Reference sites for content within this project:

[MxNet Site - Installation](http://mxnet.io/get_started/install.html) : Used the MacOS, Python, CPU, Pip version of the installation.

Education:
- [Python Tutorials](http://mxnet.io/api/python/index.html)

## Packages

### Basic

- [Arrays](http://mxnet.io/tutorials/basic/ndarray.html)
- [Symbols](http://mxnet.io/tutorials/basic/symbol.html)
- [Modules](http://mxnet.io/tutorials/basic/module.html)

Modified code above slightly from the sources to include in a package, and to explicity create variables for nested object.  Somehow, eclipse gives an error. So for example, the following:

```
net = mx.sym.Variable('data')
net = mx.sym.FullyConnected(net, name='fc1', num_hidden=64)
net = mx.sym.Activation(net, name='relu1', act_type="relu")
net = mx.sym.FullyConnected(net, name='fc2', num_hidden=26)
```

is coded:

```
symbol = mx.sym
net = symbol.Variable('data')
net = symbol.FullyConnected(net, name='fc1', num_hidden=64)
net = symbol.Activation(net, name='relu1', act_type="relu")
net = symbol.FullyConnected(net, name='fc2', num_hidden=26)
```

_Personal Environment Notes:_
- Analytics Installation:  Although using Mac, installation is using the Linux version via Pip.
- Visualization : Graphviz
