class Board:
    def __init__(self):
        self.board = ['?'] * 9

    def __str__(self):
        for i in range(9):
            if (i % 3) == 2:
                print(self.board[i])
            else:
                print(self.board[i], end=" ")

    def move(self, place, player):
        if self.board[place] != '?':
            raise ValueError
        self.board[place] = player.marker

    def make_move(self, player, place):
        try:
            self.move(place, player)
            return True
        except:
            print("this place is already full")
            return False

    def is_same(self, marker, index):
        if self.board[index] == marker:
            return True
        return False

    def is_winner(self, marker):
        if self.is_same(marker, 0) and self.is_same(marker, 1) and self.is_same(marker, 2):
            return True
        if self.is_same(marker, 3) and self.is_same(marker, 4) and self.is_same(marker, 5):
            return True
        if self.is_same(marker, 6) and self.is_same(marker, 7) and self.is_same(marker, 8):
            return True
        if self.is_same(marker, 0) and self.is_same(marker, 3) and self.is_same(marker, 6):
            return True
        if self.is_same(marker, 1) and self.is_same(marker, 4) and self.is_same(marker, 7):
            return True
        if self.is_same(marker, 2) and self.is_same(marker, 5) and self.is_same(marker, 8):
            return True
        if self.is_same(marker, 0) and self.is_same(marker, 4) and self.is_same(marker, 8):
            return True
        if self.is_same(marker, 2) and self.is_same(marker, 4) and self.is_same(marker, 6):
            return True
        return False

    def is_draw(self):
        if self.is_winner("x") is False and self.is_winner("o") is False:
            for i in range(9):
                if self.board[i] == '?':
                    return False
            return True
        return False
