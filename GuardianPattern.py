

def GurdianPatt():
    # Guardian pattern
    x = 10
    y = 0
    #z = x > 2 and (x/y) #--> Error:
    z = x > 2 and (y!=0) and (x/y) #--> Guard present (y!=0) : since y = 0 then it is returned from there.
    print(z)
    
print(min("hellowozrlad"))
print(str(12.3)) # --> '12.3'


        

        

