nthnum=99999                                                        #define what number of the fibb sequence

a,b=1,1                                                         #vars for calculation
count=1

if nthnum<3:
    print("whyda bother, it's 1, u dont need a computer for that")      #insults for a stupid question
elif nthnum>100000:
    print("i cant be stuffed ask some other script to do if for u")     #gets annoyed for asking too much
else:
    for count in range(1,nthnum,1):                                     #calculates valid question        
        count=count+1
        a,b=b,a+b
    print(str(a))                                                       #prints answer for valid question

