import torch
import torch.nn as nn
import numpy as np

x = torch.randn(32, 12)
w = torch.randn(12, 64)

def mult(a, b):
    """Returns a dot product of two tensors

    Args:
        a (Tensor): first tensor
        b (Tensor): second tensor

    Returns:
        Tensor: Dot product result
    """
    return a @ b

def obscure(a, b, c):
    """Very long and difficult functions

    Args:
        a (Tensor): Amazing tensor
        b (Tensor): Yet another amazing tensor
        c (Tensor): Very amazing tensor
    """
    r = 3.14
    tmp = (2 * (a + b).sum() ** c.mean()) - r
    return tmp + c

v1 = mult(x, w)
v2 = obscure(v1, v1, w)
out = v1.mean() ** v2.mean()
print(out)