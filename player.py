import copy
import random
from typing import Type

# initialize some useful global variables
global in_play
in_play = False
global outcome
outcome = " start game"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

global thresh
thresh = {}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

# define hand class
       
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = False
        for c in self.cards:
            rank = c.get_rank()
            v = VALUES[rank]
            if rank == 'A': aces = True
            value += v
        if aces and value < 12: value += 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
 
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck 

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck

class Winzer:
    def __init__(self):
        self.shouldHits = 0
        self.total = 0

    def incrementWin(self):
        self.shouldHits += 1
        self.total += 1

    def incrementTotal(self):
        self.total += 1

    def get_wins(self):
        return self.shouldHits

    def get_total(self):
        return self.total     
    

def hit():
    global in_play, score, outcome
    if in_play:
        playerhand.add_card(theDeck.deal_card())
        val = playerhand.get_value()
        if val >= 21: 
            return True
        else:
            return False
       
def stand():
    global score, in_play, outcome
    if playerhand.get_value() > 21:
        #outcome = "You are busted."
        return False
    val = househand.get_value()
    while(val < 17):
        househand.add_card(theDeck.deal_card())
        val = househand.get_value()  
    if (val > 21):
        if playerhand.get_value() > 21:
            #outcome = "House is busted, but House shouldHits tie game!"
            return False
        else: 
            #outcome = "House is busted! Player shouldHits!"
            return True
    else:
        if (val == playerhand.get_value()):
            #outcome = "House shouldHits ties!"
            return False
        elif (val > playerhand.get_value()):
            #outcome = "House shouldHits!"
            return False
        else:
            #outcome = "Player shouldHits!"
            return True

class Player:
    def __init__(self):
        self.matrix = [[0 for x in range(11)] for y in range(22)]

    def sim(self, trials: int) -> None:
        shouldHits = [[0 for x in range(11)] for y in range(22)]
        for i in range(len(shouldHits)):
            for j in range(len(shouldHits[i])):
                shouldHits[i][j] = Winzer()
                self.matrix[i][j] = False

        for k in range(trials):
            deal()
            stored_player = copy.deepcopy(playerhand.get_value());
            housecard = copy.deepcopy(househand.cards[0])
            wincounter = shouldHits[stored_player][VALUES[housecard.get_rank()]];
            isQuickLoss = hit()
            if stored_player == 21:
                wincounter.incrementTotal()
            else:
                if isQuickLoss:
                    wincounter.incrementTotal()
                else:
                    wincounter.incrementWin()
            shouldHits[stored_player][VALUES[housecard.get_rank()]] = wincounter

        for a in range(len(shouldHits)):
            for b in range(len(shouldHits[i])):
                winzer = shouldHits[a][b]
                t = winzer.get_total()
                w = winzer.get_wins()
                if t == 0: 
                    r = 0.0
                    shouldHit = False
                else:
                    r = w/t
                    if r > 0.85:
                        shouldHit = True
                    else: 
                        shouldHit = False
                self.matrix[a][b] = shouldHit
                #print("Player: ", a, "Dealer: ", b, "ShouldHit: ", w, "TotalGames: ", t, "ShouldHit: ", shouldHit)

    def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
        return self.matrix[playerhand.get_value()][VALUES[dealerfacecard.get_rank()]]

    def recursive_hitter(self):
        shouldHit = self.hitme(playerhand, househand.cards[0]) 
        #print("Should hit: ", shouldHit, " P: ", playerhand.get_value(), " D: ", VALUES[househand.cards[0].get_rank()])
        if shouldHit:
            didLose = hit()
            if didLose:
                return False
            else:
                return self.recursive_hitter()
        else:
            return stand()

    def play(self, trials: int) -> float:
        wincount = 0
        for trial in range(trials):
            deal()
            didWin = self.recursive_hitter()
            if didWin:
                wincount += 1
        #print("Wins: ", wincount, " Total: ", trials, " Rate: ", (wincount / trials))
        return (wincount / trials)

#define event handlers for buttons
def deal():
    global outcome, in_play, theDeck, playerhand, househand, score
    in_play = True
    theDeck = Deck()
    theDeck.shuffle()
    playerhand = Hand()
    househand = Hand()
    playerhand.add_card(theDeck.deal_card())
    playerhand.add_card(theDeck.deal_card())
    househand.add_card(theDeck.deal_card())
    househand.add_card(theDeck.deal_card())

""" def find_threshold():
    for t in range(20, 75):
        sim(100000, (t/75))
        print("Testing Thresh: ", (t/75))
        winRate = play(100000)
        thresh[(t/75)] = winRate """
    #print(thresh)
