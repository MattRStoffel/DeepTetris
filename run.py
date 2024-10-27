import pickle
from rnn.model import My_Linear
from rnn.utils import lineToTensor

import subprocess

rnn_instance = My_Linear()
# Load the model
with open("rnn/rnn.pkl", "wb") as f:
    pickle.dump(rnn_instance, f)

x = subprocess.Popen(["fceux", "--loadlua", "tetris/run.lua", "tetris/Tetris.nes"])

while True:
    with open("tetris/active.csv", "r") as f:
        data = f.read()
        if len(data) == 432:
            bot_input = round(rnn_instance(lineToTensor(data)).item())
            with open("tetris/active_input.csv", "w") as f:
                f.write(str(bot_input))
    if x.poll() is not None:
        break
