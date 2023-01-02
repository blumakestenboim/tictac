from player import Player
from board import Board


class Game:
    def __init__(self, player1, player2):
        self.player1 = Player(player1, "x")
        self.player2 = Player(player2, "o")
        self.board = Board()
        self.turn = 1

    def play(self):
        while self.board.is_winner("x") is False and self.board.is_winner(
                "o") is False and self.board.is_draw() is False:
            if self.turn == 1:
                place = input(f"{self.player1.name} enter place between 0 to 9")
                while self.board.make_move(self.player1, int(place)) is False:
                    place = input(f"{self.player1.name} enter again place between 0 to 9")
                self.board.__str__()
                if self.board.is_winner("x"):
                    print(f"{self.player1.name} is the winner")
                    return True
                if self.board.is_draw():
                    print("game over!! there is no winner")
                self.turn = 2
            if self.turn == 2:
                place = input(f"{self.player2.name} enter place between 0 to 9")
                while self.board.make_move(self.player2, int(place)) is False:
                    place = input(f"{self.player2.name} enter again place between 0 to 9")
                self.board.__str__()
                if self.board.is_winner("o"):
                    print(f"{self.player2.name} is the winner")
                    return True
                if self.board.is_draw():
                    print("game over!! there is no winner")
                self.turn = 1
