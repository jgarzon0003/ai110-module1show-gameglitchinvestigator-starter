# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
  - Hard to follow since it provided incorrect answers.
- List at least two concrete bugs you noticed at the start  (for example: "the hints were backwards").
    - When attempts are finished in normal it says 0, but if difficulty is switched to easy or hard, attempts left become negative.
    - The new game button only resets attempts left but does not allow game to start yet.
    - I still had one attempt left and gave answer
    - What does score represent? The score from output is different from developer debug info
    - Range does not change when changing difficulty
    - Strings are stored

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 6 | Go lower | Go Higher  | none |
| -1| Go higher | Go lower | none |
| 6 | Go lower| Go higher | Out of attempts! The secret was 43. Score: -5 |
| easy | attempts = 0 | attempts = -2 | none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Sonnet 4.6
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - A suggestion it made was with function check guess where guessings where opposite of what it should do originally. If guess was higher then secret should go lower. I verified the result by telling claude to do somo pytest regarding this function. They passed. Now, we test directly by running the app.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - I asked claude a commmand to run the pytests. It did run but not the proper directory which made me questioned what was wrong since it displayed there was only one test and it failed. I then asked to give a simpler command to re run it which gave the following: `python -m pytest tests/test_game_logic.py -v` and passed all tests.  

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Testing with pytests and through the app.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - It showed that the tests passed. When check with app, behaviour was expected.
- Did AI help you design or understand any tests? How?
  - AI helped me design them by including the context of the function and what shoukd happen with examples.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns allows for the app to refresh instead of closing the app and re run it. It helps to do in real time. Also since is performed in a virtual environment it will work in all machines.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
  - Pytests will be helpful since it isolates each function and make sure it works properly
  - One/More shot prompts are helpful since it gives the AI the idea on what is happening and what the expected outcome should be. 
- What is one thing you would do differently next time you work with AI on a coding task?
  - Not do everything at once. One step at a time although it may take longer to do, it creates stability and maintability.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI is not always right. It needs to be supervised since sometimes it will do work that works for them but not for you.
