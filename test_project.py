import pytest
from project import parse_rounds, get_player_instances, generate_leaderboard_display

def test_parse_rounds():
    """
    Test the validation of the user input for the number of rounds.
    """
    # Valid inputs (boundaries and normal cases)
    assert parse_rounds("5") == 5
    assert parse_rounds("50") == 50
    assert parse_rounds("20") == 20

    # Invalid input: Not a number
    with pytest.raises(ValueError, match="Input must be a valid integer"):
        parse_rounds("hello")
    with pytest.raises(ValueError):
        parse_rounds("twenty")

    # Invalid input: Out of range (Too low)
    with pytest.raises(ValueError, match="Number of rounds must be between 5 and 50"):
        parse_rounds("4")
    with pytest.raises(ValueError):
        parse_rounds("-10")

    # Invalid input: Out of range (Too high)
    with pytest.raises(ValueError, match="Number of rounds must be between 5 and 50"):
        parse_rounds("51")
    with pytest.raises(ValueError):
        parse_rounds("1000")


def test_get_player_instances():
    """
    Test that string names are correctly mapped to strategy instances.
    """
    # Valid strategies
    names = ["TitForTat", "RandomPlayer"]
    instances = get_player_instances(names)
    assert len(instances) == 2
    # Check if the class names match
    assert type(instances[0]).__name__ == "TitForTat"
    assert type(instances[1]).__name__ == "RandomPlayer"

    # Mix of valid and invalid strategies
    mixed_names = ["Joss", "FakeStrategy", "Graaskamp"]
    mixed_instances = get_player_instances(mixed_names)
    assert len(mixed_instances) == 2
    assert type(mixed_instances[0]).__name__ == "Joss"
    assert type(mixed_instances[1]).__name__ == "Graaskamp"

    # Only invalid strategies or empty lists
    assert get_player_instances(["UnknownStrategy"]) == []
    assert get_player_instances([]) == []


def test_generate_leaderboard_display():
    """
    Test the string formatting of the leaderboard dictionary.
    """
    mock_leaderboard = {
        "TitForTat": 1500,
        "RandomPlayer": 800,
        "Tester": 50
    }
    
    result = generate_leaderboard_display(mock_leaderboard)

    # Check for the presence of header elements
    assert "LEADERBOARD" in result
    assert "================================" in result

    # Check for correct formatting of player positions and scores
    assert "1. TitForTat" in result
    assert "1500 pts" in result
    
    assert "2. RandomPlayer" in result
    assert "800 pts" in result
    
    assert "3. Tester" in result
    assert "50 pts" in result