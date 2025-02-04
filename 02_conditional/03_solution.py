std_score = input("Enter your score: ")
std_score = int(std_score)

if std_score > 100 or std_score < 0:
    print("Invalid score")
    exit()

if std_score >= 90:
    print("Grade A")
    
elif std_score >= 80:
    print("Grade B")
elif std_score >= 70:
    print("Grade C")
elif std_score >= 60:
    print("Grade D")
else:
    print("Grade F")