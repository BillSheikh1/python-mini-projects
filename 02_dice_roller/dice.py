from random import randrange

def diceRoller(numberOfDice, typeOfDice):
    results = []
    for x in range(numberOfDice):
        result = randrange(1,typeOfDice)
        results.append(result)
    
    return results

def inputParser(input):
    foundD = input.lower().find('d')
    foundNumbers = any(char.isdigit() for char in input)
    if foundD == -1 or not(foundNumbers):
        print('Error! Enter input in the correct format.')
        return
    values = input.lower().split("d")
    results = diceRoller(int(values[0]), int(values[1]))
    totalResults = sum(results)
    print(str(results) + "\nTotal: " + str(totalResults))

input = str(input('>>> Enter number of dice and type of dice. (Eg: 4d6): '))
inputParser(input)