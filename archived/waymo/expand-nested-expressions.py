def expandExpression(s):
    stack = []
    current = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == '(':
            stack.append(current)
            current = []
            i += 1
        elif ch == ')':
            group = "".join(current)
            i += 1
            
            # parse {k}
            i += 1
            k = 0
            while i < n and s[i].isdigit():
                k = k * 10 + int(s[i])
                i += 1
            i += 1
            expanded = group * k

            prev = stack.pop()
            prev.append(expanded)
            current = prev

        else:
            current.append(ch)
            i += 1
    return "".join(current)


print(expandExpression("abs(cs){3}g"))
print(expandExpression("a(b(c){2}){2}"))