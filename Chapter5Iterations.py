def UserInput():
    while True:
        # Input
        userInput = input('What is the name of country you are in now?\n')
        userInputStr = str(userInput).lower()
        if(userInputStr == 'australia'):
            break
        print('Right answer' if userInputStr == 'australia' or userInputStr ==
              'aus' else (f'Lying your country is not {userInputStr}'))
    print("Correct!!")


def for_loop():
    alist = ['a', 'b', 'c']
    for friend in alist:
        print(friend)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        num = int(num)
        if(smallest is None or num < smallest):
            smallest = num
        if(largest is None or num > largest):
            largest = num
    except:
        print("Invalid input")

print("Maximum", largest)
print("Manimum", smallest)
