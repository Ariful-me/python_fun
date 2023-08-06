num = 0
count = 0
avgvalue = 0

# lets make a loop 
while True :            # loop means to make some thing again and again repeting process
    nvalue = input('Enter a number: ')
    if nvalue == 'done' :           # inputed value make more value until geting done
        break                   # if maching done, make a break
    try :                           # skip the line, if sometin wrong or wrong input getting and shoing in diploay by print fun
        cvalue = float(nvalue) # skip program
    except :                # to make skip end fun. mendataory if try logic use
        print('Please Enter numaric value or Type [done] to finish the program: ')
        continue        # continue means to continue from top but will not repeat the prog
    count = count + 1       # counting the input value
    avgvalue = avgvalue + cvalue # making sum all input rem cvalue is input variable look up side
    
print('You inputed: ', count,'value')
print('Summ value:', avgvalue)
print('Avg value:', avgvalue/count) # avg devide and print out


   