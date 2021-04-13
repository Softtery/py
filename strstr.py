def strstr(stroke, x):
    i = 0
    while i < len(stroke):
        i += 1
        if x in stroke:
            return i
        else:
            i = -1
            return i
#stroke = input("Введите строчку/текст для поиска: ")



#x = "two, one"
print("123one".find("one"))
print(strstr('123one', 'one'))


#print(strstr("one"))
