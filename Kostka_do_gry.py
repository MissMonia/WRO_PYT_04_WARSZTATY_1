from random import randint
import re

kostki = {
    'D3': 3,
    'D4': 4,
    'D6': 6,
    'D8': 8,
    'D10': 10,
    'D12': 12,
    'D20': 20,
    'D100': 100
}

kod = input(str("Wpisz kod:"))
print(kod)
list_kod = list(kod)

# a dalej myślimy...
