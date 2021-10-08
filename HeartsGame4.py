# This is the Hearts Game.
# Four players compete for the least amount of points.
# The user is Player 1 or p1.

# Import Deck File, which includes the Deck class.
import DeckFile1
import random

def main():
    # Explain the game rules to the user
    print('You are playing Hearts!')
    print('You always get to lead in this version of Hearts.')
    print('Is that an advantage or disadvantage? You decide!')
    print('The GOAL of the game is to get the FEWEST points.')
    print('Each HEART (H) is worth 1 point')
    print('The QUEEN of SPADES (12 S) is worth 13 points!')
    print('ACES are HIGH.')
    print('One more thing:')
    print('You can SHOOT THE MOON by getting 26 points in a round.')
    print('If you Shoot the Moon, all other players get 26 points,')
    print('and you get ZERO. But beware, others can reach the Moon too....')
    print('\nGood luck!')

    thisTrick = [] # List to track current trick
    keepGoing = 1
    
    p1Hand = [] # List for user
    p2Hand = [] # List for computer 1
    p3Hand = [] # List for computer 2
    p4Hand = [] # List for computer 3
    
    # Establish scores
    p1Score = 0
    p2Score = 0
    p3Score = 0
    p4Score = 0

    
    # thisDeck is an object of the Deck class.
    # The Deck will need to be reshuffled when there are 0 cards left
    thisDeck = DeckFile1.Deck(0)
    print('The Dealer will start now.')
    # Deal 13 cards to each player
    while len(p1Hand) < 13:
        thisCard = thisDeck.deal()
        p1Hand.append(thisCard)
    while len(p2Hand) < 13:
        thisCard = thisDeck.deal()
        if thisCard not in p1Hand:
            p2Hand.append(thisCard)
    while len(p3Hand) < 13:
        thisCard = thisDeck.deal()
        if thisCard not in p1Hand and thisCard not in p2Hand:
            p3Hand.append(thisCard)
    while len(p4Hand) < 13:
        thisCard = thisDeck.deal()
        if thisCard not in p1Hand and thisCard not in p2Hand and thisCard not in p3Hand:
            p4Hand.append(thisCard)


    while keepGoing == 1:
        # Tell user their hand
        thisTrick.clear()
        print('\nYour hand is: ',p1Hand)

        # Get user to play first card of the trick
        print('Enter the location of the card you wish to play from 1 to',
              len(p1Hand),'below: ')
        p1Play = int(input())
        p1Play -= 1
        # Add p1Play to thisTrick
        thisTrick.append(p1Hand[p1Play])

        # Identify lead suit
        p1Split = p1Hand[p1Play].split()
        trickSuit = p1Split[1]
        p1Hand.remove(p1Hand[p1Play])
    
        # Get cards from the computer players, matching suit if possible
        # Player 2 play
        p2SuitMatch = []
        p2CardNum = 0
        while p2CardNum <= (len(p2Hand)-1):
            if trickSuit in p2Hand[p2CardNum]:
                p2SuitMatch.append(p2Hand[p2CardNum])
            p2CardNum += 1
        if len(p2SuitMatch) > 0:
            # Random method is used once cards of the trick suit are identified
            p2Play = random.randint(0,(len(p2SuitMatch)-1))
            thisTrick.append(p2SuitMatch[p2Play])
            q = p2Hand.index(p2SuitMatch[p2Play])
            p2Hand.remove(p2Hand[q])
        # If Player 2 has no cards of the lead suit, play a random card
        else: 
            p2Play = random.randint(0,(len(p2Hand)-1))
            thisTrick.append(p2Hand[p2Play])
            p2Hand.remove(p2Hand[p2Play])

        # Player 3 play, identical logic to player 2 play
        p3SuitMatch = []
        p3CardNum = 0
        while p3CardNum <= (len(p3Hand)-1):
            if trickSuit in p3Hand[p3CardNum]:
                p3SuitMatch.append(p3Hand[p3CardNum])
            p3CardNum += 1
        if len(p3SuitMatch) > 0:
            p3Play = random.randint(0,(len(p3SuitMatch)-1))
            thisTrick.append(p3SuitMatch[p3Play])
            q = p3Hand.index(p3SuitMatch[p3Play])
            p3Hand.remove(p3Hand[q])
        else:
            p3Play = random.randint(0,(len(p3Hand)-1))
            thisTrick.append(p3Hand[p3Play])
            p3Hand.remove(p3Hand[p3Play])

        # Player 4 Play, identical logic to player 2 play
        p4SuitMatch = []
        p4CardNum = 0
        while p4CardNum <= (len(p4Hand)-1):
            if trickSuit in p4Hand[p4CardNum]:
                p4SuitMatch.append(p4Hand[p4CardNum])
            p4CardNum += 1
        if len(p4SuitMatch) > 0:
            p4Play = random.randint(0,(len(p4SuitMatch)-1))
            thisTrick.append(p4SuitMatch[p4Play])
            q = p4Hand.index(p4SuitMatch[p4Play])
            p4Hand.remove(p4Hand[q])
        else:
            p4Play = random.randint(0,(len(p4Hand)-1))
            thisTrick.append(p4Hand[p4Play])
            p4Hand.remove(p4Hand[p4Play])
        
        # Show user the trick
        print ('\nHere is the trick ', thisTrick)

        # Call calcTaker function to calculate trick winner
        trickTaker = calcTaker(thisTrick)
        # Call calcPoints function to calculate trick points
        trickPoints = calcPoints(thisTrick)

        # Tell user who takes the trick
        if trickTaker == 'p1':
            print ('\nYou take the trick!')
            p1Score += trickPoints
        elif trickTaker == 'p2':
            print ('\nPlayer 2 takes the trick!')
            p2Score += trickPoints
        elif trickTaker == 'p3':
            print ('\nPlayer 3 takes the trick!')
            p3Score += trickPoints
        elif trickTaker == 'p4':
            print ('\nPlayer 4 takes the trick!')
            p4Score += trickPoints

        # Tell user the current score
        print ('\nThe current score is...',\
               '\nYou:      ', p1Score, \
               '\nPlayer 2: ', p2Score, \
               '\nPlayer 3: ', p3Score, \
               '\nPlayer 4: ', p4Score)

        # Shooting the moon
        # A player shoots the moon if they get all 26 points in a round
        # All other players get 26 points and the moon shooter gets 0
        if p1Score == 26 and p2Score == 0 and p3Score == 0 and p4Score == 0:
            p1Score == 0
            p2Score == 26
            p3Score == 26
            p4Score == 26
            print('You shot the moon!!!!!!!!!!!!!!!!!!! Blasting off in...3...2...1..')
            print ('\nThe new score is...',\
               '\nYou:      ', p1Score, \
               '\nPlayer 2: ', p2Score, \
               '\nPlayer 3: ', p3Score, \
               '\nPlayer 4: ', p4Score)
        if p2Score == 26 and p1Score == 0 and p3Score == 0 and p4Score == 0:
            p1Score == 26
            p2Score == 0
            p3Score == 26
            p4Score == 26
            print('Player 2 shot the  moon!!!!!!!!!!!!!!!!!!! Blasting off in...3...2...1..')
            print ('\nThe new score is...',\
               '\nYou:      ', p1Score, \
               '\nPlayer 2: ', p2Score, \
               '\nPlayer 3: ', p3Score, \
               '\nPlayer 4: ', p4Score)
        if p3Score == 26 and p1Score == 0 and p2Score == 0 and p4Score == 0:
            p1Score == 26
            p2Score == 26
            p3Score == 0
            p4Score == 26
            print('Player 3 shot the  moon!!!!!!!!!!!!!!!!!!! Blasting off in...3...2...1..')
            print ('\nThe new score is...',\
               '\nYou:      ', p1Score, \
               '\nPlayer 2: ', p2Score, \
               '\nPlayer 3: ', p3Score, \
               '\nPlayer 4: ', p4Score)
        if p4Score == 26 and p1Score == 0 and p2Score == 0 and p3Score == 0:
            p1Score == 26
            p2Score == 26
            p3Score == 26
            p4Score == 0
            print('Player 4 shot the  moon!!!!!!!!!!!!!!!!!!! Blasting off in...3...2...1..')
            print ('\nThe new score is...',\
               '\nYou:      ', p1Score, \
               '\nPlayer 2: ', p2Score, \
               '\nPlayer 3: ', p3Score, \
               '\nPlayer 4: ', p4Score)
            
        # End of deck, ask user if they want to reshuffle and redeal
        if len(p1Hand) > 0:
            keepGoing = int(input('\nPress 1 to play another trick: '))
        else:
            keepGoing = int(input('\nThe hand is over. Press 1 to reshuffle: '))
            if keepGoing == 1:
                # Reshuffle
                thisDeck = DeckFile1.Deck(0)
                # Deal 13 cards to each player
                while len(p1Hand) < 13:
                    thisCard = thisDeck.deal()
                    p1Hand.append(thisCard)
                while len(p2Hand) < 13:
                    thisCard = thisDeck.deal()
                    p2Hand.append(thisCard)
                while len(p3Hand) < 13:
                    thisCard = thisDeck.deal()
                    p3Hand.append(thisCard)
                while len(p4Hand) < 13:
                    thisCard = thisDeck.deal()
                    p4Hand.append(thisCard)
        
    # Game ending
    print('\nChickening out so soon? Too bad!')
    print('The final score is...',\
          '\nYou:      ', p1Score, \
          '\nPlayer 2: ', p2Score, \
          '\nPlayer 3: ', p3Score, \
          '\nPlayer 4: ', p4Score)
    
    # Call calcWinner function
    winner = calcWinner(p1Score, p2Score, p3Score, p4Score)
    # Tell user who won
    print(winner)
    print('Bye Bye!')

# calcTaker function to calculate which player takes the trick        
def calcTaker(trick):
    lead = trick[0] #assign lead card
    leadSplit = lead.split() #split lead card value
    leadSuit = leadSplit[1] #identify lead suit
    finalists = [] #create list for finalists
    for x in trick: #add finalists to list
        if leadSuit in x:
            finalists.append(x)
    item = len(finalists)-1
    numerals = [] #create list for finalists numerals only
    while item > -1:
        finalistSplit = finalists[item].split()
        if finalistSplit[0] == 1:
            finalistSplit[0] == 14
        numerals.append(int(finalistSplit[0]))
        item -= 1
    numerals.sort()
    winner = str(str(numerals[-1]) + " " + leadSuit)
    
    if trick[0] == winner:
        return 'p1'
    elif trick[1] == winner:
        return 'p2'
    elif trick[2] == winner:
        return 'p3'
    elif trick[3] == winner:
        return 'p4'
       
# clacPoints function to calculate how many points were in the trick    
def calcPoints(trick):
    points = 0
    for x in trick:
        if 'H' in x:
            points += 1
        if x == "12 S":
            points += 13
    return points

def calcWinner(p1, p2, p3, p4):
    pointsList = []
    pointsList.append(p1)
    pointsList.append(p2)
    pointsList.append(p3)
    pointsList.append(p4)
    pointsList.sort()
    winScore = pointsList[0]
    if pointsList[0] == pointsList[1]:
        return '\nTie'
    elif p1 == winScore:
        return '\nYou win!!! Congratulations'
    elif p2 == winScore:
        return '\nPlayer 2 wins'
    elif p3 == winScore:
        return '\nPlayer 3 wins'
    elif p4 == winScore:
        return '\nPlayer 4 wins'
    
    
    

main()
            
        

