
run=True

while run==True:
    cmd=input("}")
    if cmd == "write":
        block=input("type in the block you would like to access ")
        if block == "1":
            data1=input("please enter data ")
        if block == "2":
            data2=input("please enter data ")
        if block == "3":
            data3=input("please enter data ")
    if cmd == "read":
        Rblock=input("what block would you like to read ")
        if block == "1":
            print(data1,)
        if block == "2":
            print(data2,)
        if block == "3":
            print(data3,)
    if cmd=="read all":
        print(data1, data2, data3,)
    if cmd=="write all":
        data1=input("please enter data ")
        data2=input("please enter data ")
        data3=input("please enter data ")
        
        print("done!")
    if cmd=="end":
        exit()
    if cmd=="help":
        print("hello what you are reading is the help article: write alllows you to enter data into a block, read allows you to read what was in the block, read all reads the data in evrey block, write all allows you to write in all blocks in only 1 command, end exits the terminal oh and there are 3 blocks")
    if cmd=="caculate":
            def calculate(n1,n2,op):
                if op == '+':
                    result = n1+n2
                elif op == '-':
                    result = n1-n2
                elif op == '*':
                    result =  n1*n2
                elif op == '/':
                    result = n1/n2
                elif op=='^':
                    result =  n1**n2
                else:
                    raise ValueError('Invalid operator')
    
                if result.is_integer():
                    result = int(result)
        
                return result
            
        number1 = float(input('Enter first number: '))
        op = input('Enter operator (+,-,*,/,^): ')
        number2 = float(input('Enter second number: '))
        print(number1,op,number2)
        result=calculate(number1,number2,op)
        print('=',result)
