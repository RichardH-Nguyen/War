import itertools
import random

class Cards:
    def __init__(self):
        self.suits = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
        self.values = {'Ace': 14, 'King': 13, 'Queen': 12, 'Jack': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
                       '4': 4, '3': 3, '2': 2}
        self.actualCards = list(itertools.product(self.suits, self.values))

    def GetRandomCard(self):
        randomDeal = random.randint(0, len(self.actualCards) - 1)
        cardDealt = self.actualCards[randomDeal]  # Generate random card
        self.actualCards.pop(randomDeal)  # Remove card from deck
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
        self.deckOfCards = Cards()

    def StartGame(self):
        for playerID in range(0, self.numberOfPlayers):
            cardForPlayer = self.deckOfCards.GetRandomCard() #Deal card
            newPlayer = Player(playerID, cardForPlayer) #Save player and card
            self.players.append(newPlayer)
        self.DecideWinner()

    def DecideWinner(self):
        winningID = self.players[0]  # Choose potential winner
        print("Player 0 Card: " + str(winningID.cardForPlayer))
        print("Player 1 Card: " + str(self.players[1].cardForPlayer))

        if self.players[1].cardForPlayer[1] > winningID.cardForPlayer[1]:
            # TODO For some reason 10 is lower than everything.
            winningID = self.players[1]  # find highest card
        print("The winner is player " + str(winningID.playerID) + "!")
        print("The winning card is the " + str(winningID.cardForPlayer[1]) + " of " + str(winningID.cardForPlayer[0]) + ".")

    def CheckForTie(self, player0, player1):
        if player0.cardForPlayer[1] == player1.cardForPlayer[1]:
            while player0.cardForPlayer[1] == player1.cardForPlayer[1]:
                # TODO deal card to player 0 and 1 then print.
                return


if __name__ == "__main__":
    newGame = War(2)
    newGame.StartGame()
    print()
