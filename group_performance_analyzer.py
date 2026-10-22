scores=[]
while True:
    user_input = input("შეიყვანე ქულა (ან 'stop' ): ")
    if user_input.strip().lower() == 'stop':
        break
    try:
     user_input = float(user_input)
     if 0 <= user_input <= 10:
                scores.append(user_input)
    
    except ValueError:
        print("Invalid input შეიყვანეთ რიცხვი ან 'stop' გამოსასვლელად.")

if scores:
     print("მინიმალური ქულა:", min(scores))
     print("მაქსიმალური ქულა:", max(scores))
     print("საშუალო ქულა:", sum(scores) / len(scores))
     print("ქულები ზრდადობით:", sorted(scores))
     for score in set(scores):
         print(f"ქულა {score} გამეორდა {scores.count(score)}-ჯერ")
else:
     print("არ არის შეყვანილი ქულები.")