import torch
import torch.nn as nn
import numpy as np

x = torch.randn(32, 12)
w = torch.randn(12, 64)

o = x @ w

def mult(a, b):
    """Returns a dot product of two tensors

    Args:
        a (Tensor): first tensor
        b (Tensor): second tensor

    Returns:
        Tensor: Dot product result
    """
    return a @ b
