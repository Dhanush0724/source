def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    length = len(string)

    for i in range(length):
        if string[i] in  vowels:
           kevin += length - i
        else :
            stuart += length - i

    if stuart > kevin:
        print("Stuart",stuart)

    elif kevin > stuart :
        print("Kevin",kevin)

    else :
        print("Draw")

if __name__ == '__main__':
    string = input()
    minion_game(string)
