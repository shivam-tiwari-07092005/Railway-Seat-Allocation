#insertion
stack = []
top = -1
n = int(input("Enter the number of elements: "))
for i in range(n):
    if top == n-1:
        print("Stack overflow!")
        break
    element = int(input("Enter the element: "))
    stack.append(element)
    top += 1
print("Stack: ", stack)

#deletion
stack = []
top = -1
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter the element: "))
    stack.append(element)
    top += 1
print("Stack before deletion: ", stack)
if top == -1:
    print("Stack overflow!")
else:
    deleted = stack.pop()
print("Stack after deletion: ", stack)

#in->post
stack = []
postfix = " "
infix = input("Enter infix expression: ")
precedence = {"+":1, "-":1, "*":2, "/":2, "^":3}
for ch in infix:
    if ch.isalnum():
        postfix += ch
    elif ch == "(":
        stack.append(ch)
    elif ch == ")":
        while stack and stack[-1] != "(":
            postfix += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != "(" and precedence[ch] <= precedence[stack[-1]]:
            postfix += stack.pop()
        stack.append(ch)
while stack:
    postfix += stack.pop()
print("Postfix expression: ", postfix)

#pre->in
stack = []
prefix = input("Enter prefix expression: ")
is_valid = True
for ch in reversed(prefix):
    if ch.isalnum():
        stack.append(ch)
    else:
        if len(stack) < 2:
            is_valid = False
            break
        op1 = stack.pop()
        op2 = stack.pop()
        exp = "(" + op1 + ch + op2 + ")"
        stack.append(exp)
if is_valid and len(stack) == 1:
    print("Infix expression: ", stack.pop())

#post->pre
exp = input("Enter the postfix expression: ")
stack =[]
for ch in exp:
    if ch.isalnum():
        stack.append(ch)
    else:
        b, a = stack.pop(), stack.pop()
        stack.append(ch + a + b)
print("Prefix expression: ", stack[0])

#post->in
stack = []
postfix = input("Enter postfix expression: ")
for ch in postfix:
    if ch.isalnum():
        stack.append(ch)
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        exp = "(" + op1 + ch + op2 + ")"
        stack.append(exp)
print("Infix expression: ", stack.pop())