import torch
from torch import nn

class ResidualBlock(nn.module):
    
    def __init__(self, inp_channel, mid_channel, out_channel):
        super(ResidualBlock, self).__init__()

        self.residual_block = nn.Sequential(
            nn.Conv2d(inp_channel,mid_channel, kernel_size = 3, padding = 0),
            nn.ReLU6(),
            nn.Conv2d(mid_channel,out_channel, kernel_size = 3, padding = 0)
        )
        self.relu = nn.ReLU6()

    def forward(self, x):
        out = self.residual_block(x)

        out = out + x # residual mapping
        out = self.relu(out)
        return out

