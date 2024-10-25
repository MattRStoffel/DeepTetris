# Tetris data gathering for Tetris AI

This is a project for our CSC-671 Deep learning class. The goal of the project is to train a model to play Tetris. While it would be best to train using reinforcement learning, we do not have the experience nor the resources to do so. Instead we will be training our model using supervised learning. We are labeling data using Tool-Assisted Speedrun (TAS) software which is created by many different users who painstakingly played the game at an extremely slow speed to make the best moves possible. We will be using this data to train our model.

## Data Gathering Process

We used an emulator called FCEUX to play the game. While developing our plans we decided to develop 2 seperate models where we had a CNN model to develop outputs that would represent the memory inside the emulated game state so we created a lua script to record the data during game play. We also created a second model that would take in the game state and output the best move to make.

### Running the lua script

First you need to have downloaded FCEUX

macOS:

```zsh
brew install fceux
```

Then you can run the lua script by running the following command in this directory

```zsh
fceux --playmov perfect.fm2 --loadlua script.lua Tetris.nes > /dev/null
```
