from Game import Game
from Player import *
from random import shuffle


#game happens here
if __name__ == "__main__":
    game = Game(10)
    players = [Cheater(), Cooperator(), Grudger(), Copycat(), Detective()]
    shuffle(players)
    for i, player1 in enumerate(players):
        for player2 in players[i:]:
            if player2 != player1:
                game.play(player1, player2)
                # print(f"{player1.name} Plays with {player2.name}: {game.registry[player1.name]} {game.registry[player2.name]}")

    game.top3()
