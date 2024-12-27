
import random 
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUpper =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUpper=lettersUpper
numbers=[0,1,2,3,4,5,6,7,8,9]

randomLetters=random.sample(letters,10)
randomNumbers=random.sample(numbers,10)

randomNumbersStr = list(map(str, randomNumbers))

passwordList = randomLetters+ randomNumbersStr
# Shuffle the combined list to mix letters and numbers
random.shuffle(passwordList)
password = "".join(passwordList)

print("".join(randomLetters))
print(str("".join(randomNumbersStr)))
#letters and numbers combined
print(password)