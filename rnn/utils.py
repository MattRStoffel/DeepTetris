import torch


def lineToNums(line):
    bytes_list = [line[i : i + 2] for i in range(0, len(line), 2)]
    return [int(byte, 16) for byte in bytes_list]


def lineToTensor(line):
    tensor = torch.tensor(lineToNums(line), dtype=torch.float32)
    return tensor
