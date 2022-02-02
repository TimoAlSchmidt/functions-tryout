
# print [INPUT] getallen van fibonacci

def fibonacci(maxGetal, vorig=0, getal=1):
    getal2 = getal + vorig
    if maxGetal == 0:
        return
    print(getal)
    maxGetal -= 1
    fibonacci(maxGetal, getal, getal2)
    
getal = int(input("Hoeveel getallen van fibonacci wil je?\n"))

print("\n")
fibonacci(getal)