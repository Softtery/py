def pow_recurs(num, counter, temp):
    #result = num
    num = num * temp
    counter -= 1
    print(num)
    if counter <= 1: 
        #print(num)
        return
    return pow_recurs(num, counter, temp)



pow_recurs(2, 3, 2)
