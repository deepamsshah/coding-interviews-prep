
def InfixtoPostfix(exp):
    #code here
    import string
    stack = []
    prec = {'^':4,'*':3,'/':3,'+':2,'-':2,'(':1}
    postfixexp = []
    tokens = list(exp)
    for token in tokens:
        if ((token in string.ascii_lowercase) | (token in "0123456789") | (token in string.ascii_uppercase)):
            postfixexp.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            if len(stack)!=0:
                topToken = stack.pop()
                while topToken != '(':
                    postfixexp.append(topToken)
                    topToken = stack.pop()
        else:
            if len(stack) != 0:
                while (len(stack)!=0) and (prec[stack[-1]] >= prec[token]):
                    postfixexp.append(stack.pop())
            stack.append(token)
    while len(stack)!=0:
        postfixexp.append(stack.pop())
    return "".join(postfixexp)
