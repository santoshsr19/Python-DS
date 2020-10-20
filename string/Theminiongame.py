def minion_game(string):
    vowels = set('AEIOU')
    Stuart = Kevin = 0
    for i, c in enumerate(string):
        if c in vowels:
            Kevin += len(string)-i
        else:
            Stuart += len(string)-i
    if Stuart > Kevin:
        print('Stuart', Stuart)
    elif Kevin > Stuart:
        print('Kevin', Kevin)
    else:
        print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)