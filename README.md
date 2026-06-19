# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters 50
2. Game returns "Go LOWER"
3. User enters 4
4. Game returns "Go Higher"
5. User enters 7
6. Game returns "Correct"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
(.venv) PS C:\Users\Jhostin\Documents\Codepath\AI 110\Week 2 Project\ai110-module1show-gameglitchinvestigator-starter> python -m pytest tests/test_game_logic.py -v
============================================================================================================= test session starts =============================================================================================================
platform win32 -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Jhostin\Documents\Codepath\AI 110\Week 2 Project\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Jhostin\Documents\Codepath\AI 110\Week 2 Project\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 11 items                                                                                                                                                                                                                             

tests/test_game_logic.py::test_winning_guess PASSED                                                                                                                                                                                      [  9%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                                                                                                     [ 18%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                                                                                                      [ 27%]
tests/test_game_logic.py::test_easy_range PASSED                                                                                                                                                                                         [ 36%]
tests/test_game_logic.py::test_normal_range PASSED                                                                                                                                                                                       [ 45%]
tests/test_game_logic.py::test_hard_range PASSED                                                                                                                                                                                         [ 54%]
tests/test_game_logic.py::test_difficulty_ordering PASSED                                                                                                                                                                                [ 63%]
tests/test_game_logic.py::test_too_high_hint_says_go_lower PASSED                                                                                                                                                                        [ 72%]
tests/test_game_logic.py::test_too_low_hint_says_go_higher PASSED                                                                                                                                                                        [ 81%]
tests/test_game_logic.py::test_string_secret_compares_numerically PASSED                                                                                                                                                                 [ 90%]
tests/test_game_logic.py::test_string_secret_win PASSED                                                                                                                                                                                  [100%]

============================================================================================================= 11 passed in 0.03s ==============================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
