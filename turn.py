def play_human_turn(n):

    while True:
        user_move = input("What's your move? ")
        valid = [1, 2, 3]
        if int(user_move) == 1 or int(user_move) == 2 or int(user_move) == 3:
            n -= int(user_move)
            break
        else: 
            print('Only pick 1, 2 or 3 coins from the table.')
    
    print(f'There are {n} coins left on the table.')
    
    if n == 0:
        return 0
    
    return n

def play_computer_turn(n):
    from random import randint
    a = randint(1, 3)
    
    if n <= 3:
        n -= n
        print(f'Computer took out all coins, you lose!')
        return n

    print('Computer\'s turn.')
    if n % 4 == 0:
        n -= a
    else:
        n -= n % 4
   
    if n == 0:
        return 0
    
    print(f'Computer took out {a} coins.')
    
    return n
