##for a in range(100,300):
##    flag = True
##    for x in range(1000):
##        for y in range(1000):
##            if ((x*y < a) or (x < y) or (x >= 12)) == False:
##                flag = False
##    if flag == True:
##        print(a)


##############################################


##for a in range(100):
##    flag = True
##    for x in range(100):
##        for y in range(100):
##            if ((2*x + 3*y < 30) or (x + y >= a)) == False:
##                flag = False
##    if flag == True:
##        print(a)
        
##for x in range(100):
##    print(x)
##    if x > 80:
##        break


##for a in range(100,300):
##    flag = True
##    for x in range(1000):
##        for y in range(1000):
##            if ((x*y < a) or (x < y) or (x >= 12)) == False:
##                flag = False
##                break
##    if flag == True:
##        print(a)


##for a in range(100,300):
##    flag = True
##    for x in range(1000):
##        if flag == False:
##            break
##        for y in range(1000):
##            if ((x >a)or(y>a)or(2*y+x<110)) == False:
##                flag = False
##                break
##    if flag == True:
##        print(a)

####  ДЗДДЗДЗДЗДЗЗД exit  cm 23 stroky


##for a in range(100):
##    flag = True
##    for x in range(1000):
##        if ((x & 51 == 0)or((x & 41 ==0)<=( x & a == 0))) == False:
##            flag = False
##            break
##    if flag == True:
##        print(a)


for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        if ( (x % a != 0) <= ( (x % 6 ==0) <= (x % 4 != 0) )) == False:
            flag = False
            break
    if flag == True:
        print(a) 
