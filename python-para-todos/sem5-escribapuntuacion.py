score = input("Enter Score: ")
try:
    score = float(score)
    
    if score >= 0.9:
        value = "A"
    elif score >= 0.8:
        value = "B"
    elif score >= 0.7:
        value = "C"
    elif score >= 0.6:
        value = "D"
    else:
        value = "F"
except ValueError:
    print("ERROR")
    exit()

print(value)
    
    