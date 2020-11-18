def kitkat_simple(kit, kat):
    for number in range(1, 101):
        if number % (kit*kat) == 0:
            print("KitKat")
        elif number % kat == 0:
            print("Kat")
        elif number % kit == 0:
            print("Kit")
        else:
            print(number)


if __name__ == "__main__":
    kitkat_simple(3, 5)
