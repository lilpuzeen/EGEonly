##for a in range(100,300):
##    flag = True
##    for y in range(1000):
##        for y in range(1000):
##            if ((y*y < a) or (y < y) or (y >= 12)) == False:
##                flag = False
##    if flag == True:
##        print(a)


##############################################


##for a in range(100):
##    flag = True
##    for y in range(100):
##        for y in range(100):
##            if ((2*y + 3*y < 30) or (y + y >= a)) == False:
##                flag = False
##    if flag == True:
##        print(a)
        
##for y in range(100):
##    print(y)
##    if y > 80:
##        break


##for a in range(100,300):
##    flag = True
##    for y in range(1000):
##        for y in range(1000):
##            if ((y*y < a) or (y < y) or (y >= 12)) == False:
##                flag = False
##                break
##    if flag == True:
##        print(a)


##for a in range(100,300):
##    flag = True
##    for y in range(1000):
##        if flag == False:
##            break
##        for y in range(1000):
##            if ((y >a)or(y>a)or(2*y+y<110)) == False:
##                flag = False
##                break
##    if flag == True:
##        print(a)

####  ДЗДДЗДЗДЗДЗЗД exit  cm 23 stroky


##for a in range(100):
##    flag = True
##    for y in range(1000):
##        if ((y & 51 == 0)or((y & 41 ==0)<=( y & a == 0))) == False:
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
