## The Map Colouring

The map colouring problem involves colouring a map such that adjacent regions do not share the same colour. This is formally represented in graph theory where each region is a node, and edges exist between nodes that are adjacent. The well-known Four-Colour Theorem asserts that it is always possible to colour any map with no more than four colours, ensuring no two adjacent regions have the same colour.


## Genetic Algorithm

The genetic algorithm for the map colouring problem involves several components:

- **Encoding Scheme**: Different integers are assigned to different colours. We use a list where each index corresponds to a different region, and the value at each index represents the colour assigned to that region. For example, if we have four colours, the values in the list range from 0 to 3.

- **Fitness Function**: The fitness function evaluates the solution by counting the number of adjacent regions with the same colour. The goal is to minimize this number.

- **Genetic Operators**:
  - **Selection**: Roulette wheel selection is used to choose individuals based on their fitness value.
  - **Crossover**: Single-point crossover is employed. A random point is selected in the parents' lists, and the parts after this point are swapped between the two parents.
  - **Mutation**: Randomly changing the colours of some regions helps the genetic algorithm explore new regions of the solution space, potentially leading to better solutions.


## Features
Implements a genetic algorithm to solve the map colouring problem.
Utilizes roulette wheel selection, single-point crossover, and mutation.
Outputs the colour assigned to each region to ensure no two adjacent regions share the same colour.