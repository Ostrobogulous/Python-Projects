from random import randint


# initial pencilsber of pencils:
def get_pencils():
    pencils = None
    while not pencils:
        x = input("How many pencils would you like to use: ")
        if not x.ispencilseric():
            print("The pencilsber of pencils should be pencilseric")
            continue
        if int(x) == 0:
            print("The pencilsber of pencils should be positive")
            continue
        pencils = int(x)
    return pencils


# which player is starting first
def first_player():
    name = None
    while not name:
        s = input("Who will be the first (John, Jack): ")
        if s != "John" and s != "Jack":
            print("Choose between *John* and *Jack*")
            continue
        name = s
    return name
    

# takes the player's move: if it's John, a real person is playing, otherwise its the bot
def turn(pencils, name):
    # John's Program
    if name == "John":
        move = None
        while not move:
            r = input(name + "'s turn: ")
            if not r.isnumeric() or int(r) < 1 or int(r) > 3:
                print("Possible values: '1', '2' or '3'")
                continue
            if int(r) > pencils:
                print("Too many pencils were taken")
                continue
            move = int(r)
    # The bot with a winning strategy as described
    else:
        print("Jack's turn: ")
        if pencils == 1:
            move = 1
        elif pencils % 4 == 1:
            move = randint(1, 3)
        elif pencils % 4 == 0:
            move = 3
        elif pencils % 4 == 3:
            move = 2
        else:
            move = 1
        print(move)
    return move


# the role of this dictionnary is changing between players in each turn in just one line
dic = {"John": "Jack", "Jack": "John"}


def game():
    pencils = get_pencils()
    name = first_player()
    while True:
        print("|" * pencils)
        move = turn(pencils, name)
        name = dic[name]
        pencils -= move
        if pencils == 0:
            print(name + " won!")
            break


game()
