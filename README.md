## Conway's Game of Life Clone

Conway's Game of Life is a cellular automaton, which is a simulation defined by a simple set of rules and an initial input on a grid with either dead or alive cells.

(although, as you will see, I included a feature where you can continuously add live cells as the simulation plays, for optimizing chaos of course)

Feel free to read more about it [here](https://en.wikipedia.org/wiki/Conway's_Game_of_Life_)

## Why would I do something that has already been created countless of times?

Uhhhh because I can, but mostly so I can say I learned Python, created a project from start to end, and move on with my life. *cries in lack of type safety*

## Installation Instructions

> Note: If you are on Windows, I HIGHLY recommend using WSL2 to run this project. Trust me. 

1. Make sure you have python3 installed on your system the command
`python3`

If not, install it
https://www.python.org/downloads/

2. Clone this repository:
`git clone https://github.com/mirmeep/game-of-life.git`

3. cd into the repository

4. Run the program:
`uv run main.py`

You should receive a pop up window of the pygame!

## How to Play

PLAY / PAUSE: Spacebar

ADD LIVE CELLS (or remove): Mouse click

### Example
1. Input some live cells by clicking tiles
2. Hit the space bar
3. Watch the chaos unfold *dyanmic system noises*
4. Hit space bar again to pause
5. Lather, rinse, repeat