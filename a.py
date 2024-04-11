def calculate_armstrong_numbers():
    armstrong_numbers = []
    for num in range(0, 100001):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            armstrong_numbers.append(num)
    return armstrong_numbers


if _name_ == "_main_":
    armstrong_numbers = calculate_armstrong_numbers()
    print("Armstrong numbers within the range of 0 to 100,000:")
    print(armstrong_numbers)
