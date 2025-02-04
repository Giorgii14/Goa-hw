def list_info(numbers):
    if len(numbers) < 5:
        print("Please enter 5 numbers : ")
        return
    
    max_number = max(numbers)
    min_number = min(numbers)
    total = sum(numbers)
    length = len(numbers)

    print( max_number)
    print( min_number)
    print( total)
    print(length)


list = [777, 23, 15, 55, 14, 105]
list_info(list)