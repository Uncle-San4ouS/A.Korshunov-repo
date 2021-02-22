for procent in range(32):
    if procent % 10 == 1 and procent % 100 != 11:
        print(procent, 'процент,', end=" ")
    elif 1 < procent % 10 < and not 11 < procent % 100 < 15:
        print(procent, 'процента,', end=" ")
    else:
        print(procent, 'процентов,', end=" ")