# python quiz game

questions = ((" Which player scored the first-ever “Golden Goal” in FIFA World Cup history?: " ,
              "Which club won the first-ever UEFA Champions League (1955–56 season)?: " ,
              "Which country has appeared in the most FIFA World Cup finals matches?: " ,
              "Who is the only goalkeeper to have won the Ballon d’Or?: " ,
              "Which footballer holds the record for the fastest hat-trick in Premier League history?: "))


options = (("A. Oliver Bierhoff" , "B. Laurent Blanc" , "C. Roberto Baggio" , "D. Davor Šuker"),
           ("A. AC Milan" , "B. Benfica" , "C. Real Madrid" , "D. Juventus"),
           ("A. Brazil" , "B. Germany" , "C. Italy" , "D. Argentina"),
           ("A. Gianluigi Buffon" , "B. Lev Yashin" , "C. Manuel Neuer" , "D. Iker Casillas"),
           ("A. Alan Shearer" , "B. Thierry Henry" , "C. Sadio Mané" , "D. Sergio Agüero"))

answers = ("B" , "C" , "B" , "B" , "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
      print(option)

    guess = input("Enter (A , B , C , D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("----------------------------")
print("          RESULTS           ")
print("----------------------------")

print("answers: " , end =" ")
for answer in answers:
    print(answer, end =" ")
    print()
print("guesses: " , end =" ")
for guess in guesses:
    print(guess , end =" ")
    print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")