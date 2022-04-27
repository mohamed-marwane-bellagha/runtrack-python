def fizzbuzz(start,end):
    tab = []
    while start<end:
        start = start + 1
        if start%3==0 & start%5==0:
            fizzbizz="Fizzbizz"
            tab.append(fizzbizz)
            start=start+1
        elif start%3==0:
            fizz="Fizz"
            tab.append(fizz)
            start=start+1
        elif start%5==0:
            bizz="Bizz"
            tab.append(bizz)
            start=start+1
        tab.append(start)
        for i in tab:
            print(i)
fizzbuzz(0,100)