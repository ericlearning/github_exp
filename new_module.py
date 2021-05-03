import torch
import torch.nn as nn

class ConvBlk(nn.Module):
    def __init__(self, ic, oc):
        super().__init__()
        self.conv = nn.Conv2d(ic, oc, 3, 1, 1)
    
    def forward(self, x):
        return self.conv(x)

blk = ConvBlk(16, 64)
x = torch.randn(256, 16, 4, 4)
o = blk(x)

print(x.shape, o.shape, x.dtype, o.dtype)