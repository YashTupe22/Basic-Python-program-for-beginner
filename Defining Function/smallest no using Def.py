def smallest_no(numbers):
    smallest = numbers[0]
    for number in numbers:
        if numbers[0] < smallest:
            smallest = number[0]
        print(smallest)

l = [1,2,3,4,5,6,7,8]
small = smallest_no(l)
print(small)

