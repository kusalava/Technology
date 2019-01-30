def reciprocal(num):
    #if num == 0:
     #   raise ZeroDivisionError('Invalid Division')
    try:
        x = 1/num
    except:
        print('Hello')   
    else:
        try:            
            z = 3/num
        except:
            l = 4/num
    finally:
        print('Finalblock:\tDivided by zero error occured')
    return 10

print(reciprocal(0))