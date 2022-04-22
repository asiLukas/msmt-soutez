import random


class Piskvorky(object):
    def __init__(self, board_size, player_name1, player_name2):
        self.board_size = board_size
        self.player_name1 = player_name1
        self.player_name2 = player_name2
        self.current_player_name = self.player_name1
        self.board = []
        self.filled_positions = []

    def create_board(self):
        # vytvoreni hraciho pole podle zadani uzivatele
        if self.board_size > 21:
            print('prosim zadejte mensi hraci pole')
            quit()
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append('-')
            self.board.append(row)

    # nahodne zvoli hrace co zacina
    def get_random_first_player(self):
        return random.randint(0, 1)

    # zapise O nebo X na pozadovanou validni pozici
    def fix_spot(self, row, col, player):
        # pokud je pozice validni, prida ji na hraci plochu, jinak zada hrace o novou pozici
        if (row+1, col+1) in self.filled_positions or (row+1, col+1) == (0, 0):
            print('tam uz neco je, zvol jinou pozici')
            row, col = list(
                map(int, input(f"Zadej pozici pro vlozeni {player} (priklad 1 1 - zapise {player} do leveho horniho rohu): ").split()))
            print()
            self.fix_spot(row - 1, col - 1, player)
        else:
            # prida zadanou pozici do seznamu
            self.filled_positions.append((row+1, col+1))

            # presahnuti hraci plochy
            try:
                self.board[row][col] = player
            except IndexError:
                print('hraci plocha neni tak velka, zvol jinou pozici')
                row, col = list(
                    map(int, input(f"Zadej pozici pro vlozeni {player} (priklad 1 1 - zapise {player} do leveho horniho rohu): ").split()))
                print()
                self.fix_spot(row - 1, col - 1, player)

    # logika na kontrolu zda nekdo vyhral
    def check_win(self, row, col, player):
        # delka pro to, kolik musi byt za sebou O nebo X aby hrac vyhral
        win_len = 4

        # sloupce
        for i in range(self.board_size):
            if (self.board[row-1][i] != player):
                break
            if i == win_len-1:
                return True

        # radky
        for i in range(self.board_size):
            if (self.board[i][col-1] != player):
                break
            if i == win_len-1:
                return True

        # diagonalne
        if row == col:
            for i in range(self.board_size):
                if (self.board[i][i] != player):
                    break
                if i == win_len-1:
                    return True

    # pokud je cele hraci pole zaplnene a nikdo nevyhral - remiza
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    # zmena hrace o je na tahu
    def swap_player(self, player):
        if self.current_player_name == self.player_name1:
            self.current_player_name = self.player_name2
        else:
            self.current_player_name = self.player_name1

        return 'X' if player == 'O' else 'O'

    # zobrazeni hraci plochy
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # hlavni game loop
    def main(self):
        self.create_board()

        # priradi nahodne vybrane X nebo O, ktere se priradi k hraci ktery zacina
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"hrac {self.current_player_name}({player}) je na tahu")

            self.show_board()

            # vstup uzivatele
            row, col = list(
                map(int, input(f"Zadej pozici pro vlozeni {player} (priklad 1 1 - zapise {player} do leveho horniho rohu): ").split()))
            print()

            # zapsani znaku
            self.fix_spot(row - 1, col - 1, player)

            # kontrola zda hrac vyhral
            if self.check_win(row, col, player):
                print(f"hrac {self.current_player_name} - {player} vyhral")
                break

            # kontrola remizy
            if self.is_board_filled():
                print("remiza")
                break

            # zobrazuju hrace, ktery je na tahu
            player = self.swap_player(player)

        # zobrazeni hraciho pole
        print()
        self.show_board()


if __name__ == '__main__':
    # vstup uzivatele
    board_size = int(input('Zadej pozadovanou velikost hraciho pole(priklad vstupu: 7 = pole 7x7): '))
    usr1 = input('Zadej jmeno prvniho hrace: ')
    usr2 = input('Zadej jmeno druheho hrace: ')

    # instance tridy, spusteni hry
    main = Piskvorky(board_size, usr1, usr2)
    main.main()
