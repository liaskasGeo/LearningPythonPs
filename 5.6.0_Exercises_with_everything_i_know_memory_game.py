hidden = [2, 1, 4, 3, 1, 3, 2, 4]
N = 8

state = ["closed","closed","closed","closed","closed","closed","closed","closed",]
#open states: open, temp_open

active_game = True
while active_game:
    #read first position
    first_position = int(input("Give first position(0-(N-1) and closed: "))
    while (first_position < 0 or first_position >= N) or state[first_position] == "open":
        print("Error!")
        first_position = input("Give first position(0-(N-1) and closed: ")
    #read second position

    #change state: both temp_open

    #print current state

    #check if same then open,else closed




