def math(a,b,i):
    if i == '+':
        return int(a)+int(b)
    elif i == '-':
        return int(a)-int(b)
    elif i == '*':
        return int(a)*int(b)
    elif i == '/':                    
        return int(a)/int(b)

def check_brace (con):
    con = con.replace(' ','')
    if '(' in con:
        con_part = con[con.find('(')+1:con.find(')')]
        new_con = con.replace(str(con[con.find('('):con.find(')')+1]), str(calc(con_part)))
        return calc(new_con)
    else:
        return calc(con)

def calc(con):
        oper = ['+', '-', '*', '/']
        for i in oper:
            if (j := con.find(i)) >= 0:
                left = con[:j]
                right = con[j+1:]
                if left.isdigit() and right.isdigit():
                    return math(left, right, i)
                elif left.isdigit() and not right.isdigit():
                    return math(left, calc(right), i)
                elif not left.isdigit() and right.isdigit():
                    return math(calc(left), right, i)
                else: 
                    return math(calc(left), calc(right), i)


con = input('Задайте арифмитическое выражение строкой: ')
print(f'Ответ: {check_brace(con)}')