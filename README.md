
# Higher or Lower Card Game

A classic Higher or Lower card game implemented in Python using Tkinter GUI framework. Players must guess whether the next card will be higher or lower than the current card.




## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)

## How to Play
    1. Start the game by running the script
    2. A card will be displayed on the left side
    3. Choose whether you think the next card will be higher or lower by clicking the corresponding button
    4. If correct, your score increases by 1
    5. If incorrect, the game ends and your score resets
    6. In case of equal cards, no points are lost or gained
    7. Optional: Toggle Jokers on/off using the checkbox (Jokers are always highest)


## Game Rules

- Numbered cards (2-10) have their face value
- Face cards have the following values:

    - Jack (J) = 11
    - Queen (Q) = 12
    - King (K) = 13
    - Ace (A) = 14
    - Joker = 15 (when enabled)


- The game continues until either:

    - The player makes an incorrect guess
    - All cards have been used

## Future Improvements

- Implement high score tracking
- Add animations for card reveals
- Use images of the cards instead of just the number and sign
- A better implementation of the jocker card

## Decision made

- The easiest way I could think of to represent all the cards was numbers and signs.
- Also to give the option of being able to add jockers, it occurred to me to check or uncheck the square above the cards




"# Card_Game" 
