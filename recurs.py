def asds(counter):
    print("!")
    counter -= 1
    if counter == 0:
        return
    return asds(counter)


asds(4)
