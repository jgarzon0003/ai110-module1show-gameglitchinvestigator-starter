from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- get_range_for_difficulty bug regression ---
# Bug: Hard returned (1, 50) and Normal returned (1, 100), making Hard
# accidentally easier than Normal. Fixed to Easy=1-20, Normal=1-50, Hard=1-100.

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_difficulty_ordering():
    # Each difficulty must have a strictly wider range than the one below it.
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


# --- check_guess hint message bug regression ---
# Bug 1: "Too High" returned "Go HIGHER" and "Too Low" returned "Go LOWER" —
#         the hint messages were swapped, actively misleading the player.
# Bug 2: On even attempts app.py passed secret as a string; the old fallback
#         used lexicographic comparison, so e.g. guess=9 vs secret="10" would
#         wrongly report "Too High" because "9" > "10" alphabetically.

def test_too_high_hint_says_go_lower():
    # Guess is above secret — player should be told to go lower, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint for Too High, got: {message!r}"

def test_too_low_hint_says_go_higher():
    # Guess is below secret — player should be told to go higher, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint for Too Low, got: {message!r}"

def test_string_secret_compares_numerically():
    # app.py converts secret to str on even attempts; 9 < 10 numerically but
    # "9" > "10" lexicographically, so the old code returned "Too High" here.
    outcome, _ = check_guess(9, "10")
    assert outcome == "Too Low", (
        "String secret must be compared numerically: 9 < 10 should be 'Too Low'"
    )

def test_string_secret_win():
    # Winning against a string secret must still be detected correctly.
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"
