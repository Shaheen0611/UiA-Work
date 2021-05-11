
word = 0
NumWord = 0
unique = 0
store = {}
countWord = 0


while word != 'stop': #LETS THE USER WRITE UNTIL STOP IS WRITTEN
    word = input("Enter your word:")
    if word == 'stop':
        break
    if not word in store: #IF THE WORD DOESNT EXIST IN DICTIONARY THEN THIS WILL HAPPEN
        store[word] = 0
        countWord += 1

    store[word] += 1

    NumWord += 1 #COUNTS THE NUMBER OF UNIQE WORDS

print("Unique :",countWord)
print("Total :",NumWord)

for pair in store.items(): #THE WORD TRIES TO FIND ITS PAIR(THE SAME WORD)
        print(f"{pair[0]} : {pair[1]}")



