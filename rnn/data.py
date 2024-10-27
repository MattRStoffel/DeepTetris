from torch.utils.data import Dataset
import pandas as pd

from utils import lineToTensor, lineToNums


class Data_Loader(Dataset):
    def __init__(self, feature_name, label_name, path):
        df = pd.read_csv(path)
        self.X = [lineToTensor(x) for x in df[feature_name]]
        self.Y = [lineToNums(y) for y in df[label_name]]

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.Y[idx]


data = Data_Loader("board", "input", "../tetris/data/addresses_output.csv")

for i in range(700, 710):
    print(data[i][1])
