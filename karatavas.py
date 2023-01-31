import random

words = ["viens", "divi", "trīs", "cits"]

while True:
    word = random.choice(words)
    guessedWord = list("_" for _ in word)
    lives = 5

    while lives > 0 and "".join(guessedWord) != word:
        inp = input("Burts: ")
    
        if inp == "":
            continue
        inp = inp[0]
        # Pārbaude

        guessed = False
        for i in range(0, len(word)):
            if inp == word[i]:
                guessedWord[i] = inp
                guessed = True

        if not guessed:
            lives -= 1

        print(f"Dzīvības: {lives}")
        print(guessedWord)
    


        print(inp)
    if lives > 0:
        print("uzvarējāms")
    else:
        print("zaudējāms")
    if input("Vai sākt jaunu spēli? y/n").lower() == "y":
        break

