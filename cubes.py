def add_cubes(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        sum+=i**3
    return sum
add_cubes(4,9)