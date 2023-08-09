import random

class Blackjack():

    def __init__(self):
        self.player = []
        self.dealer = []
        self.player_value = 0
        self.dealer_value = 0

    def deal(self):
        self.deck = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4)
        random.shuffle(self.deck)
        self.player = [self.deck.pop(), self.deck.pop()]
        self.dealer = [self.deck.pop(), self.deck.pop()]
        self.player_value = sum(self.player)
        self.dealer_value = sum(self.dealer)

        if self.player_value == 21:
            print(f"\nYour hand is {self.player} worth {self.player_value}. BLACKJACK!")
        elif self.player_value > 21:
            print(f"\nYour hand is {self.player} worth {self.player_value}. YOU BUST.")
        else:
            print(f"\nYour hand is {self.player} worth {self.player_value}. The dealer has drawn a {self.dealer[0]}.")

    def hit(self):
        card = self.deck.pop()
        self.player.append(card)
        self.player_value += card

        if self.player_value == 21:
            print(f"\nYour hand is {self.player} worth {self.player_value}. YOU WIN.")
        elif self.player_value > 21:
            print(f"\nYour hand is {self.player} worth {self.player_value}. YOU BUST.")
        else:
            print(f"\nYour hand is now {self.player} worth {self.player_value}.")
            response = input("\nWhat will you do (Hit/Stand): ")
            if response.lower() == 'hit':
                game.hit()
            elif response.lower() == 'stand':
                game.stand()
    
    def stand(self):
        while self.dealer_value < 17:
            print(f"\nThe dealer's hand is {self.dealer}")
            card = self.deck.pop()
            print(f"The dealer has drawn a {card}.")
            self.dealer.append(card)
            self.dealer_value += card       

        if self.dealer_value > 21:
            print(f"\nThe dealer's hand is {self.dealer} worth {self.dealer_value}. DEALER BUSTS!")
        elif self.player_value > self.dealer_value:
            print(f"\nThe dealer's hand is {self.dealer} worth {self.dealer_value}. Your hand is {self.player} worth {self.player_value}. YOU WIN!")
        elif self.player_value < self.dealer_value:
            print(f"\nThe dealer's hand is {self.dealer} worth {self.dealer_value}. Your hand is {self.player} worth {self.player_value}. YOU LOSE.")
        else:
            print(f"\nThe dealer's hand is {self.dealer} worth {self.dealer_value}. Your hand is {self.player} worth {self.player_value}. TIED.")

game = Blackjack()

def run_game():
    print("\nWeclome to Blackjack! You will be playing against a computer dealer.")
    while True:
        response = input("\nWhat will you do (Deal/Quit): ")
        if response.lower() == 'deal':
            game.deal()
            if game.player_value >= 21:
                continue
            else:
                response = input("\nWhat will you do (Hit/Stand): ")
                if response.lower() == 'hit':
                    game.hit()
                elif response.lower() == 'stand':
                    game.stand()
        elif response.lower() == 'quit':
            break

run_game()