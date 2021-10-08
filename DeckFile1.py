#
# The Deck class - a Deck of cards!
#
import random  # we need this for the randint() call

class Deck:
    #
    # the constructor method of the Deck class...
    # ... this is the method that gets run automatically when the user
    # ... program (like a BlackJack program) instantiates a Deck object!
    #
    def __init__(self, redeal):   # '__init__' signifies that this is the constructor
        # the redeal parameter, above:  stop dealing cards
        #... when there are that many cards left in the deck.

        # set up a list of 52 items that contains a code for
        # ... each card in the deck...
        # ... example: 5 D is a Five of Diamonds
        # we use double underbar __ before the list name
        # ... to make this data member private.
        self.__cards = [
                      '1 D','1 H','1 C','1 S',
                      '2 D','2 H','2 C','2 S',
                      '3 D','3 H','3 C','3 S',
                      '4 D','4 H','4 C','4 S',
                      '5 D','5 H','5 C','5 S',
                      '6 D','6 H','6 C','6 S',
                      '7 D','7 H','7 C','7 S',
                      '8 D','8 H','8 C','8 S',
                      '9 D','9 H','9 C','9 S',
                      '10 D','10 H','10 C','10 S',
                      '11 D','11 H','11 C','11 S',
                      '12 D','12 H','12 C','12 S',
                      '13 D','13 H','13 C','13 S',]

        # set the __redeal data member to the redeal parameter passed in...
        self.__redeal = redeal  # we use double underbar __ before the data member name
                                # ... to make this data member private.

        # we will always start with 52 cards remaining in the deck...
        self.__remaining = 52

        # if the redeal value passed in is invalid, set it to 1
        if self.__redeal < 1 or self.__redeal > 51:
            self.__redeal = 1

        # that's the end of the Deck constructor!            

    #
    # the deal() method of the Deck class...
    # ... the user program (like a BlackJack program) will
    # ... call this method when they want a card from the deck.
    #
    def deal(self):
        theCard = 'X'  # return an 'X' when it's time for a new deck

        # are there cards remaining in the deck?
        if self.__remaining >= self.__redeal:
           # yes, there are cards remaining in the deck...
           needCard = 1

           # loop, randomly looking for an item in the list (card in the deck)
           # ... which has not yet been picked...
           while needCard == 1:
              cardNum = random.randint(0,51)  
              if self.__cards[cardNum] != '0':
                 # this card has not yet been picked...
                 theCard = self.__cards[cardNum]
                 self.__cards[cardNum] = '0'  # mark card as read 
                 needCard = 0               # we can get out of this loop
                 self.__remaining -= 1        # decrement remaining cards count
              # end if card not already taken
           # end while loop
        # end if remaining...
        return(theCard)

# end Deck class... 
