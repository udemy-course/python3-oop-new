numbers = [1, 2, 3, 4, 10, -4, -7, 0]


def all_even(num_list):

    even_numbers = []
    for number in num_list:
        print('number=', number)
        if number % 2 == 0:
            print('发现偶数, number=', number)
            even_numbers.extend([number])

    return even_numbers


print('all even number', all_even(numbers))
