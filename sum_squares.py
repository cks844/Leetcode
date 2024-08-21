def sum_squares(num:int):
    sq_list = [i*i for i in range(1,num)]
    new_list =[]
    for i in range(0,len(sq_list)):
        for j in range(1,len(sq_list)):
            if sq_list[i] + sq_list[j] == num:
                new_list.append(sq_list[i])
                new_list.append(sq_list[j])
    
    if not new_list:
        return print("No squares with a sum",num)
    else:
        return print(list(set(new_list)))

        
if __name__ == "__main__":
    num = int(input("Enter the number:"))
    sum_squares(num)
        
       