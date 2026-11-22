#A
score = 8
classification = None
if score>=8:
    classification = "Tot"
elif score>=5:
    classification = "Dat"
else:
    classification = "Can co gang"
#B
n = 10
even_total = 0
for i in range(1,n):
    if i%2==0:
        even_total += i
print(even_total);
#C
counter = 5
turns = 0
while counter>0:
    counter -= 1
    turns += 1
print(counter)
print(turns)
#D
secret = 7
for i in range(5):
    guess = int(input("Nhap so ban doan: "))
    if guess == secret:
        print("Chuc mung ban doan dung")
        break
    elif guess > secret:
        print("So ban doan cao hon")
    else:
        print("So ban doan thap hon")