We will break the problem up into two parts. We want to have a way to turn any given image of a Tetris screen and translate that screen into a representation of the way that the blocks could be represented in memory.

The other half of the project will require a way to train the model, based on the computers memory that tells us where the blocks are, that will classify the best inputs into the game.

We will require a way to classify what a good move is. I think that a tool assisted (TAS) would be a good way to give us labels for training. I am not sure how a TAS works but I think that the amount of training data we could get is okay even if the TAS works in a deterministic manner.

Tetris does have a random number generator (RNG) nd I think we can use that to our advantage. I think that there should also be a heuristic function that is based on the score for the model to maximise if we can?

The classes will be the game controller buttons that would be the best to be pressed at an certain time.

```
----[CNN]----[representation of memory]----[RNN]----[GAME CONTROLLER]
```

We can train the models separately you break up the work as a team.
