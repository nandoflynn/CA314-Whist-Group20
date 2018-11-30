from enum import Enum
from enum import IntEnum
from random import *
full_deck=[]
partial_deck=[]
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5 
    SIX = 6 
    SEVEN = 7 
    EIGHT = 8 
    NINE = 9 
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

#suite enum for playing cards
class Suite(Enum):
    SPADES="spades"
    CLUBS="clubs"
    HEARTS="hearts"
    DIAMONDS="diamonds"



#class to hold information to playing cards
class Playing_card():
    def __init__(self, card_value,card_suite):
        self.card = card_value
        self.suite=card_suite

#function to create a deck of card 
def create_deck():
    for suite in Suite:
        for card in Card:
            full_deck.append(Playing_card(Card(card),Suite(suite)))
    return full_deck

#draws cards
def draw_card(deck):
    randCard=randint(0,len(deck)-1)
    return deck.pop(randCard)

player1=["players0"]
player2=["players1"]
player3=["players2"]
player4=["players3"]
players=[player1,player2,player3,player4]
    
def deal_whits():
    while (len(partial_deck)>0 ):
        player1.append(draw_card(partial_deck))
        player2.append(draw_card(partial_deck))
        player3.append(draw_card(partial_deck))
        player4.append(draw_card(partial_deck))


class start_game():
    def __init__(self,trump="",dealer=None,hand=None,team1=0,Team2=0,):
        self.trump=trump
        self.dealer=dealer
    def set_dealer(self):
        if self.dealer==None:
            self.dealer=players[randint(0,3)]
            return self.dealer
        else:
            self.dealer=players[players.index(self.dealer)-3]
            return self.dealer
    #deal cards
    def deal_cards(self):
        create_deck()
        partial_deck=list(full_deck)
        self.set_dealer()
        d=self.dealer
        while (len(partial_deck)>0 ):
            players[players.index(d)-3].append(draw_card(partial_deck))
            players[players.index(d)-2].append(draw_card(partial_deck))
            players[players.index(d)-1].append(draw_card(partial_deck))
            players[players.index(d)].append(draw_card(partial_deck))
    #sets trump
    def set_trump(self):
        self.deal_cards()
        self.trump=self.dealer[-1].suite
        return(self.trump)

    def teams(self):
        team1.append("players0")
        team1.append("players3")
        team2.append("players1")
        team2.append("players2")
        


    #rounds of game
    def round(self):
            # a round for each in hand
            self.set_trump()
            print(self.trump)
            for hand in range(0,13):
                cards_played={}
                # each players card played
                for  j in range(0,2):
                    #printing the cards for each player so they know what cards to chose
                    for k in range(1,len(players[j])):
                        print(players[j][k].card,players[j][k].suite)
                    # input card to play
                    a=input("chose")
                    b =input()
                    #put the card played in a list 
                    cards_played[players[j][0]]=Playing_card(Card(int(a)),Suite(b))

                    #removing the card from the list
                    for c in range(1,len(players[j])):
                        jj=Playing_card(Card(int(a)),Suite(b))
                        if players[j][c].card==jj.card and players[j][c].suite==jj.suite :
                           players[j].pop(c)
                           print("done")
                           break
                        
                print("______________")
                compare1=[]
                compare2=[]
                tcompare1=[]
                tcompare2=[]
                score=0
                #calculating who won
                cp=list(cards_played.values())
                played_by=list(cards_played.keys())
                for i in range(0,len(cp)):
                    first_suite=cp[0].suite
                    if self.trump==cp[i].suite:
                        tcompare1.append(cp[i].card.value)
                        tcompare1.append(cp[i].suite.name)
                    elif cards_played[i].suite==first_suite :
                        compare1.append(str(cp[i].card.value)+" "+played_by[i])
                        compare2.append(cp[i].suite.name)
              #  if max(
                    
                    
                    print("________________")
                        




                
start_game()
(start_game().round())
        
    



