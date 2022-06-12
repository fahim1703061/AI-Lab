def fibonacci(val):
    n1 = 0
    n2 = 1
    count = 0
    if(val <= 0):
        print("not valid input")
        return
    elif val ==1:
        print(n2)
        return
    else:

        # while count < val:
        #     print(n1)
        #     n2 = n2 + n1
        #     n1 = n2
        #     count = count + 1
        for i in range(1, val):
            print(n2)
            c = n1 + n2
            n1 = n2
            n2 = c
        return n2

val = int(input("intput value for fibonacci: "))
print(fibonacci(val))
