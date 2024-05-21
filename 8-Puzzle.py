# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/158MBAEtmLs5QmIwtUnXC1VpoMqW86sgZ
"""

!pip install simpleai
from simpleai.search import SearchProblem, astar, greedy, breadth_first, depth_first

# Class containing methods to solve the puzzle
class PuzzleSolver(SearchProblem):
      # Action method to get the list of the possible numbers that can be moved in to the empty space
      def actions(self, cur_state):
          rows = string_to_list(cur_state)
          row_empty, col_empty = get_location(rows, 'E')

          actions = []
          if row_empty > 0: actions.append(rows[row_empty - 1][col_empty])
          if row_empty < 2: actions.append(rows[row_empty + 1][col_empty])
          if col_empty > 0: actions.append(rows[row_empty][col_empty - 1])
          if col_empty < 2: actions.append(rows[row_empty][col_empty + 1])
          return actions

      # Return the resulting state after moving a piece to the empty space
      def result(self, state, action):
          rows = string_to_list(state)
          row_empty, col_empty = get_location(rows, 'E')
          row_new, col_new = get_location(rows, action)
          rows[row_empty][col_empty], rows[row_new][col_new] = rows[row_new][col_new], rows[row_empty][col_empty]
          return list_to_string(rows)

      # Returns true if a state is the goal state
      def is_goal(self, state):
          return state == GOAL

      # Returns the number of misplaced tiles
      def heuristic(self, state):
          rows = string_to_list(state)
          goal = string_to_list(GOAL)
          distance = sum([rows[i] != goal[i] for i in range(len(rows))]) - 1
          return distance

# Convert list to string
def list_to_string(input_list):
    return '\n'.join(['-'.join(x) for x in input_list])

# Convert string to list
def string_to_list(input_string):
    return [x.split('-') for x in input_string.split('\n')]

# Find the 2D location of the input element
def get_location(rows, input_element):
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            if item == input_element:
                return i, j

# Final result that we want to achieve
GOAL = '''\
E-1-2
3-4-5
6-7-8'''

# Starting point - solution depth = 4
INITIAL = '''\
1-4-2
3-5-8
6-7-E'''

# Create a cache for the goal position of each piece
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678E':
    goal_positions[number] = get_location(rows_goal, number)

# Create the A* solver object
result = astar(PuzzleSolver(INITIAL))

# Print the results
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    else:
        print('Step %s: After moving %s into the empty space' %(i, action))
    print(state)
print('Goal achieved!')