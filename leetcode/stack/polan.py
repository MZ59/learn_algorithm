def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i not in ["+", "-", "*", "/"]:
            stack.append(int(i))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            num = int(eval(str(num2) + i + str(num1)))
            stack.append(num)
    return stack.pop()

# import pdb; pdb.set_trace()
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
