## Blackjack Game Simulator & Calculator

This program implements a simple blackjack algorithm that uses a Monte Carlo simulation-based approach to determine the optimal strategy for playing blackjack. The algorithm is implemented in Python and consists of several classes and functions.

### Prerequisites

- Python 3.x

### How to Run

1. Save the algorithm code to a Python file (e.g., `blackjack_solver.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python file is saved.
4. Run the following command to execute the algorithm:

   ```shell
   python blackjack_solver.py```

### Algorithm Overview

The blackjack solving algorithm uses a simulation approach to determine the optimal strategy for playing blackjack. It consists of the following key components:

- `Card` class: Represents a playing card and provides methods to retrieve the suit and rank of a card.

- `Hand` class: Represents a hand in the game and provides methods to add cards to the hand and calculate the value of the hand.

- `Deck` class: Represents a deck of playing cards and provides methods to shuffle the deck and deal cards.

- `Winzer` class: Represents a counter that keeps track of the number of wins and total games played for a specific player hand value and dealer face card value.

- `Player` class: Implements the main logic of the blackjack solving algorithm. It simulates multiple blackjack games to determine the optimal strategy for hitting or standing based on the player's hand value and the dealer's face card value.

- `hit()` function: Simulates a hit action in a blackjack game by adding a card to the player's hand. It returns a boolean value indicating whether the player's hand value exceeds 21 (bust).

- `stand()` function: Simulates a stand action in a blackjack game by adding cards to the dealer's hand until the hand value reaches 17 or higher. It compares the values of the player's and dealer's hands to determine the outcome of the game (win, lose, or tie).

- `deal()` function: Simulates the initial deal of cards in a blackjack game, including shuffling the deck and distributing cards to the player and dealer.

- `recursive_hitter()` method: Implements a recursive strategy for hitting in a blackjack game based on the optimal strategy determined by the algorithm. It calls the `hit()` function and recursively continues hitting as long as the optimal strategy suggests.

- `play()` method: Simulates a specified number of blackjack games and returns the win rate as a percentage.

To use the blackjack solving algorithm, follow these steps:

1. Run the Python script containing the algorithm.
2. The algorithm will simulate blackjack games to determine the optimal strategy for hitting or standing.
3. After the simulation is complete, the algorithm will output the win rate achieved based on the determined strategy.

Notes:
- The The win rate calculated represents the expected win rate based on the simulated games. The actual win rate in real-world scenarios may vary.
- The algorithm determines the optimal strategy for a specific set of conditions, such as the number of trials and the initial threshold for deciding whether to hit or stand. You can modify these parameters in the code to experiment with different settings and analyze their impact on the win rate.
- The code includes some commented-out sections (`find_threshold()` function) that were used for finding the optimal hit threshold value. You can uncomment and modify these sections if you want to experiment further with the algorithm.