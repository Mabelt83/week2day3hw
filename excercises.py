def negative_nums(numbers):
    new_number = []
    
    for num in numbers:
        num*= -1
        new_number.append(num)
        
    print(new_number) 
    
negative_nums([10, 20, 30, 40, 50])

