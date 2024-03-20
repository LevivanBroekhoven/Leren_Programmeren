import random
kleuren = ('harten', 'klaven', 'schoppen', 'ruiten')
soorten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","koning","aas")
Deck = []
jouw_Deck = []

for a in kleuren:
    for b in soorten:
        Deck.append(f"{a} {b}")

Deck.append("joker")
Deck.append("joker")
random.shuffle(Deck)
print(Deck)
for x in range(1,8):
    jouw_Deck = Deck.pop(0)
    print(f" Kaart {x} {jouw_Deck}") 

print("\n")
print("Deck (47 kaarten):", Deck) 