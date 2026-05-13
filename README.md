# Axelrod's Tournament: Prisoner's Dilemma Simulator
#### Video Demo: <https://youtu.be/SAxRE0jtylM>
#### Description: 
A Python-based, object-oriented simulator for Robert Axelrod's Prisoner's Dilemma tournament, featuring various game theory strategies and detailed data logging.

## Overview
This project is a fully functional, object-oriented simulator for Robert Axelrod's famous "Prisoner's Dilemma" computer tournament. It explores game theory by allowing various programmed strategies (both "good" and "bad" guys) to compete against each other in a Round-Robin tournament to see which strategy yields the highest score over time.

The core of the simulation is based on the following Payoff Matrix for each turn:

| Player 1 Move | Player 2 Move | Player 1 Score | Player 2 Score | Result |
| :---: | :---: | :---: | :---: | :--- |
| **Cooperate** | **Cooperate** | 3 | 3 | Reward for mutual cooperation |
| **Defect** | **Defect** | 1 | 1 | Punishment for mutual defection |
| **Cooperate** | **Defect** | 0 | 5 | Sucker's payoff / Temptation |
| **Defect** | **Cooperate** | 5 | 0 | Temptation / Sucker's payoff |

The application allows the user to specify the length of the matches (between 5 and 50 rounds) and outputs both a formatted leaderboard to the console and a detailed `tournament_results.json` file for further data analysis.

## Project Structure and Files

The project has been modularized using Object-Oriented Programming (OOP) and Clean Code principles to separate logic, state, and user interface.

### 1. `project.py`
This is the main entry point of the application. It orchestrates the flow by interacting with the user, instantiating the required strategies, and starting the tournament. 
To comply with CS50P requirements and best practices, all UI logic is separated from the core math. It contains three main testable functions:
* `parse_rounds(rounds_str)`: Validates user input to ensure it is a valid integer between 5 and 50, raising specific `ValueError` exceptions if the validation fails.
* `get_player_instances(strategy_names)`: Safely maps string names to instantiated Strategy objects.
* `generate_leaderboard_display(leaderboard)`: Formats the raw dictionary data into a clean, printable string without relying on side-effect `print()` statements.

### 2. `core/` (The Game Engine)
This directory manages the rules of the world.
* **`match.py`**: Manages a 1v1 confrontation. It calculates payoffs based on the classic Prisoner's Dilemma matrix and records a highly detailed log of every single turn.
* **`tournament.py`**: Takes a list of players and executes a Round-Robin tournament (everyone plays against everyone). It aggregates the scores and returns a comprehensive dictionary with the final leaderboard and all match logs.

### 3. `players/` (The Strategies)
This directory contains the logic for the competing entities.
* **`base.py`**: Defines the `Player` abstract base class. It handles the state (score and history) and forces all subclasses to implement the `make_move()` method.
* **`strategies.py`**: Contains 7 distinct AI behaviors divided into categories:
  * *The Good Guys*: `TitForTat`, `TitForTwoTats`, `GenerousTitForTat`. These never defect first.
  * *The Bad Guys*: `Joss`, `Graaskamp`, `Tester`. These attempt to exploit the opponent through surprise defections or testing behaviors.
  * *The Chaotic*: `RandomPlayer`, which makes decisions purely on a 50/50 chance.

### 4. `test_project.py`
Contains the `pytest` suite for the application. It thoroughly tests the core functions in `project.py` to ensure boundary conditions (like invalid round numbers or unknown strategy names) are handled gracefully.

## Design Choices
During development, several key design choices were made:
1. **Returning Data over Printing:** Instead of printing results directly inside `Match` or `Tournament`, these classes return comprehensive dictionaries. This decoupling allows the data to be easily exported to a JSON file, making the project scalable for future implementations (like adding a Pandas data analysis script or a web frontend).
2. **Abstract Base Classes:** By using `from abc import ABC, abstractmethod` for the `Player` class, the simulator is easily extensible. Adding a new strategy in the future only requires creating a new class that inherits from `Player` and implementing the `make_move` logic, without touching the core engine.
3. **Simultaneous Turns:** In `match.py`, the engine explicitly reads both players' decisions before applying them to the history logs. This prevents the "Player 2" algorithm from having an unfair advantage by seeing "Player 1's" move in the current turn.
4. **Static Type Hinting:** Extensive use of Python's `typing` module (`List`, `Dict`, `Tuple`, `Any`) was implemented across all methods and classes. This ensures robust function signatures, better IDE support, and significantly reduces the likelihood of runtime errors related to unexpected data types.

## How to Run
1. Ensure you have Python installed.
2. Install the required testing library: `pip install -r requirements.txt` (contains `pytest`).
3. Run the program: `python project.py`
4. Enter the desired number of rounds when prompted (e.g., 30).
5. Check the console for the winner and explore the generated `tournament_results.json` for detailed turn-by-turn logs.

---
**Author:** Pedro Cuenca  
**Course:** CS50's Introduction to Programming with Python (CS50P)