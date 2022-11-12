array = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]
while True:
    try:
        a = int(input("Введите число от 1 до 999: "))
        if a < 0 or a > 999:
            raise Exception("Неправильный диапазон!")
        break
    except ValueError:
        print("Нужно ввести число!")



def bi_search(a: int, array: list) -> int:
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left

print((bi_search(a, array)))
