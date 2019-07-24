from random import randint


los = randint(1, 100)

while True:

    try:
        number = input("Zgadnij liczbę od 1 do 100: ")
        number = int(number)

        if type(number) == int:
            if number < los:
                print("Za mało!")

            elif number > los:
                print("Za dużo!")

            else:
                print("Wow! Zgadłeś!")
                break
    except ValueError:
        print("Helloł - to nie jest liczba...")