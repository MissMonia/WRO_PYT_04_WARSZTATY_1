from random import shuffle

coupon = []

x = 6

while x > 0:
    try:
        number = input("Wprowadź liczbę od 1-49: ")
        number = int(number)

        if number in range(1, 50):
            if number in coupon:
                print("Ale to już było... Wybierz inną liczbę. ")
            else:
                coupon.append(number)
                x = x - 1
        elif number > 49 or number < 1:
            print("Miało być od 1 do 49! ")
    except ValueError:
        print("Podaj liczbę! ")

coupon.sort()
print("Twoje liczby: " + str(coupon))

lotto_range = range(1, 50)
lotto = list(lotto_range)
shuffle(lotto)
lotto_done = (lotto[:6])
lotto_done.sort()
print("Wylosowane liczby: " + str(lotto_done))

count = 0

for item in coupon:
    if item in lotto_done:
        count += 1

options = {6: "Trafiłeś szóstkę!", 5: "Trafiłeś piątkę!", 4: "Trafiłeś czwórkę!", 3: "Trafiłeś trójkę!"}
result = options.get(count, "Peszek...może hazard nie jest dla Ciebie..?")
print(result)
