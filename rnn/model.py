import torch.nn as nn


class My_Linear(nn.Module):
    def __init__(self):
        super(My_Linear, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(216, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
        )

    def forward(self, input):
        output = self.layers(input)
        return output
