import tkinter as tk
from tkinter import messagebox, ttk
import random


class CardHigherLowerGame:
    def __init__(self, root):
        self.root = root
        # title of the root window
        self.root.title("Higher or Lower - Card Game")
        # Background color of the root window
        self.root.configure(bg='#1e4d2b')

        # Fix window size and  non-resizable
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        # Card values and deck initialized
        self.values = list(range(2, 15))
        self.suits = ['hearts', 'spades', 'clubs', 'diamonds']
        self.face_cards = {11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: 'JOKER'}
        self.include_jokers = tk.BooleanVar(value=False)

        # Main container frame with fixed padding
        self.container = tk.Frame(root, bg='#1e4d2b', padx=20, pady=20)
        self.container.pack(expand=True, fill='both')

        # Title frame
        self.title_frame = tk.Frame(self.container, bg='#1e4d2b', height=60)
        self.title_frame.pack(fill='x')
        self.title_frame.pack_propagate(False)

        self.title_label = tk.Label(
            self.title_frame,
            text="HIGHER OR LOWER",
            font=("Arial", 24, "bold"),
            bg='#1e4d2b',
            fg='white'
        )
        self.title_label.pack(expand=True)

        # Joker option frame
        self.joker_frame = tk.Frame(self.container, bg='#1e4d2b', height=40)
        self.joker_frame.pack(fill='x')
        self.joker_frame.pack_propagate(False)

        self.joker_check = ttk.Checkbutton(
            self.joker_frame,
            text="Include Jokers",
            variable=self.include_jokers,
            command=self.reset_game,
            style='Custom.TCheckbutton'
        )

        # Configure checkbutton style
        style = ttk.Style()
        style.configure('Custom.TCheckbutton',
                        background='#1e4d2b',
                        foreground='white')

        self.joker_check.pack(expand=True)

        # Initialize deck
        self.deck = self.generate_deck()
        random.shuffle(self.deck)
        self.score = 0
        self.current_card = self.deck.pop()

        # Cards frame with fixed height
        self.cards_frame = tk.Frame(self.container, bg='#1e4d2b', height=300)
        self.cards_frame.pack(fill='x', pady=20)
        self.cards_frame.pack_propagate(False)

        # Card display frames
        self.card_display_frame = tk.Frame(self.cards_frame, bg='#1e4d2b')
        self.card_display_frame.pack(expand=True)

        # Current card
        self.current_card_frame = tk.Frame(
            self.card_display_frame,
            bg='white',
            width=150,
            height=200,
            relief="raised",
            bd=2
        )
        self.current_card_frame.pack(side='left', padx=10)
        # Prevent the current_card_frame from resizing to fit its contents
        self.current_card_frame.pack_propagate(False)

        self.current_card_label = tk.Label(
            self.current_card_frame,
            text=self.format_card(self.current_card),
            font=("Arial", 48),
            bg='white',
            fg='black'
        )
        # Expanding it to fill any available space
        self.current_card_label.pack(expand=True)

        # Next card
        self.next_card_frame = tk.Frame(
            self.card_display_frame,
            bg='white',
            width=150,
            height=200,
            relief="raised",
            bd=2
        )
        self.next_card_frame.pack(side='right', padx=10)
        self.next_card_frame.pack_propagate(False)

        self.next_card_label = tk.Label(
            self.next_card_frame,
            text="?",
            font=("Arial", 48),
            bg='white'
        )
        # Expanding it to fill any available space
        self.next_card_label.pack(expand=True)

        # Buttons frame with fixed height
        self.buttons_frame = tk.Frame(self.container, bg='#1e4d2b', height=80)
        self.buttons_frame.pack(fill='x')
        self.buttons_frame.pack_propagate(False)

        # Higher button
        self.higher_button = tk.Button(
            self.buttons_frame,
            text="Higher",
            font=("Arial", 16),
            bg='#90EE90',
            width=8,
            command=lambda: self.make_guess('h')
        )
        self.higher_button.pack(side='left', expand=True, padx=10)

        # Lower button
        self.lower_button = tk.Button(
            self.buttons_frame,
            text="Lower",
            font=("Arial", 16),
            bg='#FFB6C1',
            width=8,
            command=lambda: self.make_guess('l')
        )
        self.lower_button.pack(side='right', expand=True, padx=10)

        # Score frame
        self.score_frame = tk.Frame(self.container, bg='#1e4d2b', height=60)
        self.score_frame.pack(fill='x')
        self.score_frame.pack_propagate(False)

        self.score_label = tk.Label(
            self.score_frame,
            text=f"Score: {self.score}",
            font=("Arial", 16, "bold"),
            bg='#1e4d2b',
            fg='white'
        )
        self.score_label.pack(expand=True)

        # Cards remaining frame
        self.remaining_frame = tk.Frame(self.container, bg='#1e4d2b', height=40)
        self.remaining_frame.pack(fill='x')
        self.remaining_frame.pack_propagate(False)

        self.cards_remaining_label = tk.Label(
            self.remaining_frame,
            text=f"Cards remaining: {len(self.deck)}",
            font=("Arial", 14),
            bg='#1e4d2b',
            fg='white'
        )
        self.cards_remaining_label.pack(expand=True)

    def generate_deck(self):
        deck = []
        # Add regular cards
        for value in self.values:
            for suit in self.suits:
                # Retrieve the face card name if the value is a face card (e.g., "Jack", "Queen")
                card_value = self.face_cards.get(value, value)
                # Dictionary for each card with its 'value' (name or face card),
                # 'numeric_value' (numeric rank), and 'suit' (e.g., Hearts, Spades)
                deck.append({'value': card_value, 'numeric_value': value, 'suit': suit})

        # Add jokers if option is selected
        if self.include_jokers.get():
            deck.append({'value': 'JOKER', 'numeric_value': 15, 'suit': 'red'})
            deck.append({'value': 'JOKER', 'numeric_value': 15, 'suit': 'black'})

        return deck

    def format_card(self, card):
        # Check if the card is a JOKER
        if card['value'] == 'JOKER':
            return f"JOKER\n{card['suit']}"

        suit_symbols = {
            'hearts': '♥',
            'diamonds': '♦',
            'clubs': '♣',
            'spades': '♠'
        }
        # Return a formatted string showing the card's value and its suit symbol
        return f"{card['value']}\n{suit_symbols[card['suit']]}"

    def make_guess(self, guess):
        # Check if the deck is empty (no more cards to draw)
        if not self.deck:
            # If the deck is empty, show a message with the final score and reset the game
            messagebox.showinfo("Game Over", "No more cards left! Final score: " + str(self.score))
            self.reset_game()
            return

        # Draw the next card by popping the last card from the deck
        next_card = self.deck.pop()

        # Update the display of the next card label with the formatted card information
        self.next_card_label.config(text=self.format_card(next_card))

        # Determine if guess is correct
        is_correct = (guess == 'h' and next_card['numeric_value'] > self.current_card['numeric_value']) or \
                     (guess == 'l' and next_card['numeric_value'] < self.current_card['numeric_value'])

        if next_card['numeric_value'] == self.current_card['numeric_value']:
            messagebox.showinfo("Tie!", "Same value - no points lost or gained!")
        elif is_correct:
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Game Over", f"Wrong! Final score: {self.score}")
            self.reset_game()
            return

        # Update display
        self.current_card = next_card
        self.current_card_label.config(text=self.format_card(self.current_card))
        self.next_card_label.config(text="?")
        self.score_label.config(text=f"Score: {self.score}")
        self.cards_remaining_label.config(text=f"Cards remaining: {len(self.deck)}")

    # Define the method to reset the game
    def reset_game(self):
        # Generate a new deck of cards
        self.deck = self.generate_deck()
        random.shuffle(self.deck)
        self.score = 0
        # Set the current card to the first card drawn from the shuffled deck
        self.current_card = self.deck.pop()
        # Update the current card label to show the new current card
        self.current_card_label.config(text=self.format_card(self.current_card))
        # Set the next card label to "?" to hide the next card's value until guessed
        self.next_card_label.config(text="?")
        # Update the score label to show the reset score (0)
        self.score_label.config(text=f"Score: {self.score}")
        # Update the cards remaining label to reflect the number of cards left in the deck
        self.cards_remaining_label.config(text=f"Cards remaining: {len(self.deck)}")


if __name__ == "__main__":
    root = tk.Tk()
    # Instantiate the CardHigherLowerGame class, passing the root window as an argument
    game = CardHigherLowerGame(root)
    root.mainloop()