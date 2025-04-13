#JOHN KARL TORIO
#SAMPLE SCORE AVERAGE CALCULATOR
# Hi! This is my second upload here in GitHub, I've been practicing to code in python step by step
# I used visual studio for this

score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
score3 = int(input("Enter the third score: "))

avg = (score1 + score2 + score3) / 3
avg_round = round(avg, 2)
print(avg)

if avg_round >= 85:
    print("Passed!")

else:
    print("Try again!")
