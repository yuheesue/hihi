expression = input()
i = 0
n = 3 + (4*i)
ex = 0

for n in range(len(expression)):
        if expression[n] == "-" :
            ex = expression[:n-3] + "(" + expression[n-3:n+4] +")" + expression[n+4:] 
            print(n)
        elif n == i-3:

            break
print(ex) 
ans = int(ex)
if ex == "-":
        result *= -1
print (ans)

        # - > + > *
'''for n in i:
        if num[n] == "-" :
            expression = expression[:n-2] + "(" + expression[n-3:n+4] + expression[n+3:] 
                
            if num[n+4] == "+":
                expression = expression[:n-2] + "(" + expression[n-3:n+4+4] + expression[n+4+3:] 
                
            elif num[n-4] == "+":
                expression = expression[:n-4-2] + "(" + expression[n-4-3:n+4] + expression[n+3:] 
        
        elif n == i-3:
            break
        answer2 = abs(expression) 

        # + > * > -
    for n in i:
        if num[n] == "+" :
            expression = expression[:n-2] + "(" + expression[n-3:n+4] + expression[n+3:] 

        elif n == i-3:
            break    
        answer3 = abs(expression)         
                
        # + > - > *
    for n in i:
        if num[n] == "+" : 
            expression = expression[:n-2] + "(" + expression[n-3:n+4] + expression[n+3:] 
                
            if num[n+4] == "-":
                expression = expression[:n-2] + "(" + expression[n-3:n+4+4] + expression[n+4+3:]
                
            elif num[n-4] == "-":
                expression = expression[:n-4-2] + "(" + expression[n-4-3:n+4] + expression[n+3:]
        elif n == i-3:
            break
        answer4 = abs(expression) 

        # * > - > +
    for n in i:
        if num[n] == "*" :
            expression = expression[:n-2] + "(" + expression[n-3:n+4] + expression[n+3:]
                
            if num[n+4] == "-":
                expression = expression[:n-2] + "(" + expression[n-3:n+4+4] + expression[n+4+3:]
                
            elif num[n-4] == "-":
                expression = expression[:n-4-2] + "(" + expression[n-4-3:n+4] + expression[n+3:]
        elif n == i-3:
            break
        answer5 = abs(expression)            
                
        # * > + > -
    for n in i:
        if num[n] == "*" : 
            expression = expression[:n-2] + "(" + expression[n-3:n+4] + expression[n+3:]
                
            if num[n+4] == "+":
                expression = expression[:n-2] + "(" + expression[n-3:n+4+4] + expression[n+4+3:]
                
            elif num[n-4] == "+":
                expression = expression[:n-4-2] + "(" + expression[n-4-3:n+4] + expression[n+3:]
        elif n == i-3:
            break
        answer6 = abs(expression) 

    fin_ans = max(answer1, answer2, answer3, answer4, answer5, answer6)
    print(fin_ans)

    return fin_ans'''


clac()