
#######################################################
########## WELCOME TO BLACKJACK CARD COUNTER ##########
#######################################################


# Create dict() to represent a card deck 
# Each key represents a single card
# Each value contains a tuple of (card, count_value) 
deck = {
    '2': ('2', 1),
    '3': ('3', 1),
    '4': ('4', 1),
    '5': ('5', 1),
    '6': ('6', 1),
    '7': ('7', 0),
    '8': ('8', 0),
    '9': ('9', 0),
    '10': ('10', -1),
    'J': ('J', -1),
    'Q': ('Q', -1),
    'K': ('K', -1),
    'A': ('A', -1)
}


class CountCards:
    '''Get the Running Count and the True Count'''

    # Initialize our class
    def __init__(self, deck, deck_count):
        self.deck = deck
        self.deck_count = deck_count
        self.total_cards = self.deck_count*52
        self.run_count = 0
        self.input_card = None
        self.valid_input = False 
  
    def user_input(self):
        '''Get users card input and check for validity'''

        # Input Card
        user_input = input(str('-'*18 +'\nEnter card: ')).upper()
        
        # Pass if card is not valid
        if user_input not in self.deck:
            print("\n***That's not a valid card, try again***\n")
            self.valid_input = False

        # Accept if card is valid
        if user_input in self.deck:
            self.input_card = user_input
            self.valid_input = True

    def running_count(self):
        '''
        Match the users input card with the key in our dictionary.

        The value pair to that key contains a tuple with the count 
        value we need to access, being the second item of each tuple. 
        '''
      
        # Only increment the running count if user input was valid
        if self.valid_input == True:

            # Find key match and increment running count by count value
            for i in deck.keys():
                if i == deck[str(self.input_card)][0]:
                    self.run_count += deck[i][1]     
            print('Count: ', self.run_count)

        # Don't incerment running count if input was invalid
        else:
            pass

    def true_count(self):
        '''
        Calculate the Decks Remaining, Total Cards Remaining, and True Count.

        True Count = Running Count / Num of remaining decks.
        '''

        # Only increment if users input card was valid
        if self.valid_input == True:

            # Calculate number of decks remaining 
            self.total_cards -= 1
            for i in range(self.deck_count):
                if i*52 == self.total_cards:
                    self.deck_count -= 1
            
            # Calculate true count if cards are remaining
            if self.total_cards > 0:
                self.running_true_count = self.run_count/self.deck_count
                print('True Count: ', self.running_true_count)
                print('Cards Total: ', self.total_cards)
                print('Deck Total: ', self.deck_count)
        
        # Don't increment Total Cards Remaining, Total Decks Remaining
        # or True count if users card input was invalid.
        if self.valid_input == False:
            pass

        # End the game if there are no cards left
        if self.total_cards == 0:
            print('True Count: ', self.running_true_count)
            print('Cards Total: ', self.total_cards)
            print('Deck Total: ', self.deck_count)    
            print('\n'+'-'*15+'\n---Game Over---\n'+'-'*15+'\n')
            quit()

def main():
    '''
    Instantiate our object and necessary methods
    Loop until program exits.

    '''
    play = CountCards(deck, 1)

    while True:
        play.user_input()
        play.running_count()
        play.true_count()


if __name__ == '__main__':
    main()
