import random

class Main:
    attempts = 0
    list_word = None
    word = ''
    set_word = None
    list_word_success = ''
    word_suggested = ''
    results_data = None

    def __init__(self):
        self.attempts = 8
        self.list_word = 'python', 'java', 'swift', 'javascript'
        self.results_data = {"won": 0, "lost": 0}
        print(*"HANGMAN", sep=" ")

    def reset_play(self):
        self.attempts = 8
        self.word = random.choice(self.list_word)
        self.set_word = set(self.word)
        self.list_word_success = [*'-' * len(self.word)]
        self.word_suggested = ""

    def start(self):
        self.reset_play()
        menu = self.get_menu_select()
        while True:
            if menu == "play":
                self.play()
            elif menu == "results":
                self.results()
            elif menu == "exit":
                exit()
            else:
                self.start()

    def play(self):
        while self.attempts > 0:

            letter = self.get_letter()

            if len(letter) != 1:
                print("Please, input a single letter.")
                continue

            if not letter.isalpha() or not letter.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if letter in self.word_suggested:
                print("You've already guessed this letter.")
                continue

            self.word_suggested += letter

            if letter in self.set_word:
                indexs = [index for index, value in enumerate(self.word) if value == letter]

                for index in indexs:
                    self.list_word_success[index] = letter

                if '-' not in self.list_word_success:
                    print()
                    print(f"You guessed the word {self.word}!")
                    break
            else:
                self.attempts -= 1
                print("That letter doesn't appear in the word.")

        if '-' not in self.list_word_success:
            print('You survived!')
            self.results_data['won'] = 1 + self.results_data['won']
            self.start()
        elif self.attempts == 0:
            print("You lost!")
            self.results_data['lost'] = 1 + self.results_data['lost']
            self.start()

    def results(self):
        print(f"You won: {self.results_data['won']} times.")
        print(f"You lost: {self.results_data['lost']} times.")
        self.start()

    def get_menu_select(self):
        menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        return menu

    def get_letter(self):
        print()
        print("".join(self.list_word_success))
        letter = input("Input a letter:")
        return letter


play = Main()
play.start()




