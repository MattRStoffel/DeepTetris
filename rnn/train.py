import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import pickle

from model import My_Linear
from data import Data_Loader

torch.manual_seed(0)  # Set seed for reproducibility

train_data = Data_Loader("board", "input", "../tetris/data/addresses_output.csv")
# We are using batch size of 30 because the tetromino will take about 30 frames to reach the bottom
# I am not sure if we should shuffle the data or not
train_loader = DataLoader(train_data, batch_size=1, shuffle=True)

model = My_Linear()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
criterion = nn.MSELoss()
num_epochs = 20


losses = []
for epoch in range(num_epochs):
    epoch_loss = 0
    for x, y in train_loader:
        optimizer.zero_grad()
        output = model(x)
        print(output, y[0].float())
        loss = criterion(output, y[0].float())
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    avg_loss = epoch_loss / len(train_loader)
    losses.append(avg_loss)
    print(f"Epoch: {epoch + 1}, Loss: {avg_loss:.4f}")

# stop the model from training
model.eval()

pickle.dump(model, open("rnn.pkl", "wb"))
