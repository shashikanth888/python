def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok[0] == 'y' or ok[0] == 'Y':
            print('You say yes.')
            return 
        if ok[0] in ('n', 'N'):
            print('You say no.')
            return 
        retries = retries-1
        if retries < 0:
            print('I give up.')
            return
        print(reminder)
