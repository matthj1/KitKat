def kitkat_no_mod_div(kit, kat):
#populate a list with numbers from 1-100
    number_list = [x for x in range(1, 101)]

#function for populating sets with multiples of numbers up to a limit
    def populate_multiples(increment, limit):
        multiples = set()
        num = increment
        while num <= limit:
            multiples.add(num)
            num += increment
        return multiples

#populate sets with kit, kat and kitkat numbers
    kitkat_set = populate_multiples(kit*kat, 100)
    kat_set = populate_multiples(kat, 100).difference(kitkat_set)
    kit_set = populate_multiples(kit, 100).difference(kat_set).difference(kitkat_set)

#iterate over number list, if number is in kit, kat or kitkat sets replace
    for index, number in enumerate(number_list):
        if number in kitkat_set:
            number_list[index] = "KitKat"
        elif number in kit_set:
            number_list[index] = "Kit"
        elif number in kat_set:
            number_list[index] = "Kat"

#print each number from the list
    for number in number_list:
        print(number)


if __name__ == "__main__":
    kitkat_no_mod_div(3, 5)
