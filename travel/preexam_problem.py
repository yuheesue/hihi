def solution(expression):

    i = 0
    num = []
    n = 4 * (i+1)
    
    for num in expression:
        num[i]=expression[i]
        i =+ 1
    

    # - > * > +
    for n in num:
        if num[n] == "-" :
            expression.insert( n-3 , "(" )
            expression.insert( n+3 , ")" )
        elif n == i-3:
            break
        
        answer1 = abs(expression)            
                
        # - > + > *
    for n in i:
        if num[n] == "-" :
            expression.insert( n-3 , "(" )
            expression.insert( n+3 , ")" )
                
            if num[n+4] == "+":
                expression.insert( n-3 , "(" )
                expression.insert( n+4+3 , ")" )
                
            elif num[n-4] == "+":
                expression.insert( n-4-3 , "(" )
                expression.insert( n+3 , ")" )
        elif n == i-3:
            break
        answer2 = abs(expression) 

        # + > * > -
    for n in i:
        if num[n] == "+" :
                expression.insert( n-3 , "(" )
                expression.insert( n+3 , ")" )
                answer1 = abs(expression)
        elif n == i-3:
            break    
        answer3 = abs(expression)         
                
        # + > - > *
    for n in i:
        if num[n] == "+" : 
                expression.insert( n-3 , "(" )
                expression.insert( n+3 , ")" )
                
                if num[n+4] == "-":
                    expression.insert( n-3 , "(" )
                    expression.insert( n+4+3 , ")" )
                
                elif num[n-4] == "-":
                    expression.insert( n-4-3 , "(" )
                    expression.insert( n+3 , ")" )
        elif n == i-3:
            break
        answer4 = abs(expression) 

        # * > - > +
    for n in i:
        if num[n] == "*" :
                expression.insert( n-3 , "(" )
                expression.insert( n+3 , ")" )
                
                if num[n+4] == "-":
                    expression.insert( n-3 , "(" )
                    expression.insert( n+4+3 , ")" )
                
                elif num[n-4] == "-":
                    expression.insert( n-4-3 , "(" )
                    expression.insert( n+3 , ")" )
        elif n == i-3:
            break
        answer5 = abs(expression)            
                
        # * > + > -
    for n in i:
        if num[n] == "*" : 
                expression.insert( n-3 , "(" )
                expression.insert( n+3 , ")" )
                
                if num[n+4] == "+":
                    expression.insert( n-3 , "(" )
                    expression.insert( n+4+3 , ")" )
                
                elif num[n-4] == "+":
                    expression.insert( n-4-3 , "(" )
                    expression.insert( n+3 , ")" )
        elif n == i-3:
            break
        answer6 = abs(expression) 

    fin_ans = max(answer1, answer2, answer3, answer4, answer5, answer6)
    print(fin_ans)

    return fin_ans