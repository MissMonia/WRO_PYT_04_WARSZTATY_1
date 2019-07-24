print("Pomyśl liczbę od 0 do 1000 , a ja ją zgadnę w max. 10 próbach")
start = input("Pomyślałeś..? To wciśnij enter aby rozpocząć:")

x = 1
min = 0
max = 1000

while x < 11:


    guess = round(int(max - min)/2 + min, 0)

    print("Próba " + str(x) + ". Zgaduję: " + str(guess))
    print("""
    1 = za dużo
    2 = za mało
    3 = zgadłeś!""")
    answer = input("Podpowiedz: ")

    if answer == "1":
        max = guess
        x += 1
    elif answer == "2":
        min = guess
        x += 1
    elif answer == "3":
        print("Wow!Brawo ja!")
        break
    else:
        print("Nie ściemniaj...!")