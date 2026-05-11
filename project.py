import json
from players.strategies import (
    TitForTat, 
    TitForTwoTats, 
    GenerousTitForTat, 
    Joss, 
    Graaskamp, 
    Tester, 
    RandomPlayer
)
from core.tournament import Tournament

def main():
    """
    Main entry point for the Prisoner's Dilemma Tournament simulator.
    """
    # 1. Get the number of rounds from the user
    rounds_per_match = get_user_rounds()

    # 2. Define the list of players participating in the tournament
    strategy_names = [
        "TitForTat", 
        "TitForTwoTats", 
        "GenerousTitForTat", 
        "Joss", 
        "Graaskamp", 
        "Tester", 
        "RandomPlayer"
    ]
    
    players = get_player_instances(strategy_names)

    print(f"\n--- Starting Prisoner's Dilemma Tournament ({rounds_per_match} rounds per match) ---\n")
    
    # 3. Initialize and run the tournament
    tournament = Tournament(players, rounds_per_match)
    results = tournament.run()

    # 4. Format and display the leaderboard
    leaderboard_display = generate_leaderboard_display(results["leaderboard"])
    print(leaderboard_display)

    # 5. Save detailed results to a JSON file
    with open("tournament_results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)
        
    print("Detailed match data has been saved to 'tournament_results.json'.")


def get_user_rounds() -> int:
    """
    Prompts the user for the number of rounds until a valid input is provided.
    Delegates the actual validation to parse_rounds().
    """
    while True:
        user_input = input("Enter the number of rounds per match (5-50): ")
        try:
            # We return directly; if it fails, it jumps to the except block
            return parse_rounds(user_input)
        except ValueError as error:
            print(f"Invalid input: {error}. Please try again.")


def parse_rounds(rounds_str: str) -> int:
    """
    Parses and validates the user input for the number of rounds.
    Raises ValueError if the input is not a number or falls outside the 5-50 range.
    """
    try:
        rounds = int(rounds_str)
    except ValueError:
        raise ValueError("Input must be a valid integer")

    if rounds < 5 or rounds > 50:
        raise ValueError("Number of rounds must be between 5 and 50")

    return rounds


def get_player_instances(strategy_names: list) -> list:
    """
    Maps a list of strategy string names to their corresponding instantiated objects.
    """
    available_strategies = {
        "TitForTat": TitForTat,
        "TitForTwoTats": TitForTwoTats,
        "GenerousTitForTat": GenerousTitForTat,
        "Joss": Joss,
        "Graaskamp": Graaskamp,
        "Tester": Tester,
        "RandomPlayer": RandomPlayer
    }
    
    instances = []
    for name in strategy_names:
        if name in available_strategies:
            instances.append(available_strategies[name]())
            
    return instances


def generate_leaderboard_display(leaderboard: dict) -> str:
    """
    Takes the leaderboard dictionary and formats it into a clean, readable string table.
    """
    lines = []
    lines.append("================================")
    lines.append("           LEADERBOARD          ")
    lines.append("================================")
    
    position = 1
    for player_name, score in leaderboard.items():
        lines.append(f"{position}. {player_name:<20} {score} pts")
        position += 1
        
    lines.append("================================\n")
    
    return "\n".join(lines)


if __name__ == "__main__":
    main()