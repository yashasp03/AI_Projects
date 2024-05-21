## 8-Puzzle

This project implements an AI solution to the classic 8-puzzle problem using the A* search algorithm. The 8-puzzle is a sliding puzzle consisting of a 3x3 grid with eight numbered tiles and one blank space. The goal is to rearrange the tiles from a given starting configuration to a specified goal configuration by sliding the tiles into the blank space.


## Implementation Details

- **Initial State**: The puzzle is initialized with a start state.
- **Goal State**: The target configuration that the puzzle aims to reach.
- **Heuristic Function**: Manhattan distance.
- **Cost Function**: Each move (sliding a tile into the blank space) has a cost of 1.
- **Priority Queue**: Used to select the next state with the lowest estimated cost (current path cost + heuristic).


## Features

Implements A* search algorithm to solve the 8-puzzle problem.
Utilizes Manhattan distance as the heuristic function.
Computes and displays the path from the start state to the goal state.