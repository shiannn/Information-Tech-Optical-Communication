def decode(a):
    Length = len(a)
    ToStart = []
    for i in range(len(a)):
        if(i+5 < Length):
            #print(i)
            if(a[i]==1 and a[i+1]==1 and a[i+2]==1 and a[i+3]==0 and a[i+4]==0 and a[i+5]==0):
                ToStart.append(i)
    st = ToStart[0]
    myDecode = []
    for i in range(st+6,st+6+2*12,2):
        #print('nothing')
        if(a[i]==0 and a[i+1]==1):
            myDecode.append(1)
        elif(a[i]==1 and a[i+1]==0):
            myDecode.append(0)
        else:
            print('nothing')
    #print("")
    #print(myDecode)
    return myDecode

if __name__=='__main__':
    a = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
     0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 
     1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 
     0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 
     0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 
     1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 
     0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 
     0, 1, 1, 0, 0, 1, 0, 1, 0, 1,
     1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1]
    decode(a)