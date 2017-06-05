def lstOfPrimesUptoN(N):
    stri = ""
    
    for i in range(1,N):
        count = 0
        for i1 in range(1,i):
            if i%i1 == 0:
                count += 1

        if count == 1:
           stri += str(i) +"," 
    print(stri)
    
lstOfPrimesUptoN(1000)
