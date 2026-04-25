for i in range(2, 2000):
    primo = True

    for d in range(2, i):
        if i % d == 0:
            primo = False
            break

    if primo:
        print(i)