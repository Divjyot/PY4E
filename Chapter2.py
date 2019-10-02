def Variables():
    base = 59
    min = base  # integer
    min = (min/60)  # 0.9833333333333333
    print("Div", min)  # float
    min = (min//60)  # floor division
    print("Floor Div", min)
    min = 2**2+1  # 2^2 + 1
    print("Expo", min)
    min = base
    min = 598 % 100
    print("Mod", min)
    a = '123-'
    b = '=456'
    print(a + b)
    print(3 * a + b)


def UserInput():
    # Input
    userInput = input('What is the name of country you are in now?\n')
    userInputStr = str(userInput).lower()
    print('Right answer' if userInputStr == 'australia' or userInputStr ==
          'aus' else (f'Lying your country is not {userInputStr}'))


def printWords():
    words = {123, 345, 567, 9}
    for word in words:
        print(word)


def FtoC(celcius):
    cel = -1
    fahr = float(celcius)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
    return cel


inp = input('Enter Fahrenheit Temperature:')
isValid = True
while isValid:
    try:
        FtoC(inp)
        break
    except:
        print('Please enter a number. ', inp, 'is not valid input.')
