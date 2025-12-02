def bekeres():
    print("I/A")
    nev=input("\tJátékos neve: ")
    szerepkor=input("\tszerepkör: ")
    print("I/B")
    if szerepkor=="varázsló":
        print(f"\tÜdvözlünk {nev}, 2 életed van!")
    elif szerepkor=="harcos":
        print(f"\tÜdvözlünk {nev}, 10 életed van!")
    else:
        print(f"\tÜdvözlünk {nev}, 8 életed van!")