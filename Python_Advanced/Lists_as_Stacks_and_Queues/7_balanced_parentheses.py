input_text = input()
open_brackets = []
closed_brackets = []


def balance_checker(arg):
    for x in arg:
        if x in '{[(':
            open_brackets.append(x)
        elif x in '}])':
            closed_brackets.append(x)
    if len(open_brackets) != len(closed_brackets):
        """ test against not even count of symbols. probably not needed though """
        return False
    else:
        for i in range(len(closed_brackets)-1):
            open_br = open_brackets.pop()
            if closed_brackets[i] == ')' and open_br != '(':
                return False
            elif closed_brackets[i] == '}' and open_br != '{':
                return False
            elif closed_brackets[i] == ']' and open_br != '[':
                return False
        return True


if balance_checker(input_text):
    print('YES')
else:
    print('NO')
