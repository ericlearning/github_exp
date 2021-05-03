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

out = mult(x, w)
print(out)
print("Stars and Rainbows")
print("1234567890")
print("Hello World!")