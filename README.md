## Monty Hall

This project addresses the Monty Hall problem, a classic probability puzzle based on a popular American TV show. The problem involves three closed doors: behind one door is a car (the prize), and behind the other two doors are goats. The participant selects one of the doors, and the host, who knows what is behind each door, opens one of the other two doors, revealing a goat. The participant then has the option to stick with their original choice or switch to the remaining unopened door. The puzzle demonstrates that switching doors increases the probability of winning the car.

In this project, we use Bayesian Networks to model the Monty Hall problem and compute the probabilities of winning the prize under different conditions. We define three variables in the Bayesian Network:

Prize: The door hiding the car.
Participant's Choice: The door initially chosen by the participant.
Host's Action: The door opened by the host to reveal a goat.
The Bayesian Network is constructed to update the probabilities based on the host's action and the participant's choice. Initially, the probability of the prize being behind any door is 1/3. As the host opens a door revealing a goat, the probabilities are updated according to Bayes' theorem.


## Implementation
In the initial setup of the Monty Hall problem, the probability of the prize being behind any of the three doors is set to 1/3. When the host takes action, they open one of the two remaining doors, always revealing a goat. This action provides new information that affects the probabilities of where the prize might be. By applying Bayesian inference, the program updates these probabilities to reflect the new information provided by the host's action. The updated probabilities demonstrate that if the participant chooses to switch doors, the probability of winning the prize is 2/3, whereas if the participant decides to stick with their initial choice, the probability of winning remains at 1/3. This calculation confirms the counterintuitive strategy that switching doors increases the likelihood of winning the car.


## Features
Implements a Bayesian Network to solve the Monty Hall problem.
Uses genetic algorithms with roulette wheel selection, single-point crossover, and mutation.
Outputs the probabilities of winning the car by either sticking with the initial choice or switching doors.

