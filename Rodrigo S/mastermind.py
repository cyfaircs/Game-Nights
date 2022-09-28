import os

def input_validation(num, ref):
    while num not in ref:
        num = int(input('RUHROE, please select an int between 1-6: '))
    return num


class Game:
    # Class variable to hold range of acceptable numbers
    code_range = [1, 2, 3, 4, 5, 6]

    # constructor method to initialize lives
    def __init__(self):
        self.lives = 8
        self.game_over = False
        self.game_won = False
        self.game_board = []
        self.guess_board = []

    # Setter Function
    def set_secret_code(self, secret_code):
        self.secret_code = secret_code

    # function to decrease number of lives
    def life_decreaser(self):
        self.lives -= 1

    def game_over_check(self):
        if self.lives == 0:
            self.game_over = True

    def game_won_check(self, guess_array):
        if guess_array == ['A', 'A', 'A', 'A']:
            self.game_won = True
            self.game_over = True

    # function to append letter to guessboard
    def guessboard_appender(self, game):
        self.game_board.append(game)

    # function to append letter to gameboard
    def gameboard_appender(self, guess):
        self.guess_board.append(guess)

    # compound func to append to both boards
    def comp_board_appender(self, game, guess):
        Game.guessboard_appender(self, game)
        Game.gameboard_appender(self, guess)

    def display(self):
        print("The gameboard is:          the guessboard is :")
        for index, item in enumerate(self.game_board):
            print("{}               {}".format(
                self.game_board[index], self.guess_board[index]))


class Codemaker:
    # Initializes list to hold secret code
    def __init__(self):
        self.secret_code_array = []

    # Function to print text
    def code_maker_intro():
        print('\nHello Codemaker, you will now be prompted to input an int from 1 to 6')

    # function to get input for secret code with validation
    def secret_code_setter(self):
        while len(self.secret_code_array) != 4:
            num = int(input('Please input a number between 1-6: '))
            num = input_validation(num, Game.code_range)
            self.secret_code_array.append(num)
        return self.secret_code_array

    # Function that bundles all of Codemaker's first turn func
    def first_turn_function(self):
        Codemaker.code_maker_intro()
        return self.secret_code_setter()

    # Function to find number of perfect matches in codebreakers guess array
    def perfect_match_checker(self, guess_array):
        # Note: We will use value 'C' as default value as next functions will add perfect & alright guesses, thus left over is incorrect
        result_array = ['C', 'C', 'C', 'C']
        position = 0
        for index, item in enumerate(self.secret_code_array):
            if guess_array[index] == item:
                result_array[position] = 'A'
                position += 1
        return result_array

    # Function to find number of alright elements in guess array
    def alright_match_checker(self, guess_array):
        secret_code_copy = self.secret_code_array.copy()
        alright_guess_elements = 0
        for index, item in enumerate(guess_array):
            for ind, ele in enumerate(secret_code_copy):
                if item == ele:
                    alright_guess_elements += 1
                    secret_code_copy.pop(ind)
        return alright_guess_elements

    def guess_checker(self, guess):
        perf_guess_array = Codemaker.perfect_match_checker(self, guess)
        alright_guess_ele = Codemaker.alright_match_checker(self, guess)
        # Find number of elements that are a perfect guess
        perf_guess_elements = perf_guess_array.count('A')
        # Find diffrence bewteen perfect elements and alright ones to find number of 'B's to add to array
        ele_to_add = alright_guess_ele - perf_guess_elements
        while ele_to_add > 0:
            # We want to start adding elements at postion after A's. So if 2 A's, then next element to add at index postion 2 so use this variable as proxy for starting position
            perf_guess_array[perf_guess_elements] = 'B'
            perf_guess_elements += 1
            ele_to_add -= 1
        return perf_guess_array


class Codebreaker:

    # function to store intro and rules for codebreaker
    def code_breaker_intro(self):
        print(
            "\nHello Codebreaker, the Codemaker has just finished inputting the secret code")
        print(
            'It is your job to crack it. The code will be 4 digits from 1-6 with repitition')
        print('Each guess will provide feedback. The letter A indiactes one your letters is in the exact spot')
        print('The letter B indicates a letter is in the code, but not in the correct spot')
        print('Finally, the letter C indicates the letter is not in the code at all')
        print("The letters do not correspond to letter placement, so just focus on number of A's, B's, and C's")
        print("Goodluck Codebreaker, you'll need it")

    # function to take in input from user and then validate using pre-made function
    def code_breaker_input():
        num = int(input("\nPlease select a number between 1 - 6 as your guess: "))
        num = input_validation(num, Game.code_range)
        return num

    # Compund func that takes in input and loops until guess array filled up and returns that
    def code_breaker_guessor(self):
        guess_array = []
        while len(guess_array) != 4:
            guess_element = Codebreaker.code_breaker_input()
            guess_array.append(guess_element)
        print(guess_array)
        return guess_array


juego = Game()
john = Codemaker()
jane = Codebreaker()
secret_code = john.first_turn_function()
juego.set_secret_code(secret_code)
os.system("cls")
jane.code_breaker_intro()

while juego.game_over == False:
    temp = jane.code_breaker_guessor()
    jojo = john.guess_checker(temp)
    juego.comp_board_appender(temp, jojo)
    juego.game_won_check(jojo)
    juego.life_decreaser()
    juego.game_over_check()
    juego.display()

if juego.game_won == True:
    print("Congrats, you have won the game!")
else:
    print("\nDisgraceful Codebreaker, you have lost the game")
