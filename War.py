import itertools
import random

class Cards:
    def __init__(self):
        self.suits = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
        self.values = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.actualCards = list(itertools.product(self.suits, self.values))

    def GetRandomCard(self):
        randomDeal = random.randint(0, 51)
        cardDealt = self.actualCards[randomDeal] #Generate random card
        return (cardDealt)

class Player:
    def __init__(self, id, card):
        self.playerID = id
        self.cardForPlayer = card

class Game:
    def __init__(self, gameOfWar):
        self.name = gameOfWar

class War(Game):
    def __init__(self, numberOfPlayers):
        self.numberOfPlayers = numberOfPlayers
        self.players = []

    def StartGame(self):
        deckOfCards = Cards()
        for playerID in range(0, self.numberOfPlayers):
            cardForPlayer = deckOfCards.GetRandomCard() #Deal card
            newPlayer = Player(playerID, cardForPlayer) #Save player and card
            self.players.append(newPlayer)
        self.DecideWinner()

    def DecideWinner(self):
        winningID = self.players[0]  # Choose potential winner
        print("Player 0 Card: " + str(winningID.cardForPlayer))
        print("Player 1 Card: " + str(self.players[1].cardForPlayer))
        for playerID in self.players:
            if (playerID.cardForPlayer[1] > winningID.cardForPlayer[1]):
                winningID = playerID  # find highest card
        print("The winner is player " + str(winningID.playerID) + "!")
        print("The winning card is the " + str(winningID.cardForPlayer[1]) + " of " + str(
            winningID.cardForPlayer[0]) + ".")


if __name__=="__main__":
    newGame = War(2)
    newGame.StartGame()
