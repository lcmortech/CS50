score = int(input("Score: "))

'''
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 90:
    print("Grade B")
elif 70 <= score <= 80:
    print("Grade C")
elif 60 <= score <= 70:
    print("Grade D")
else:
    print("Grade F")
'''

# elif makes the conditional mutually exclusive
if score >= 100:
    print("Grade A")
elif score >= 90:
    print("Grade B")
elif score >= 80:
    print("Grade C")
elif score >= 70:
    print("Grade D")
else:
    print("Grade F")