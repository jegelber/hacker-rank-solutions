# Balanced Brackets
# Score: 25/25

# (), {}, []
# {([({})])}


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, value):
        self.items.append(value)

    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def isBalanced(s):
    brackets = {
        ')' :'(',
        ']' :'[',
        '}' :'{'
    }
    openers = ['(', '[', '{']
    stack = Stack()

    for bracket in s:
        if bracket in openers:
            stack.push(bracket)
        else: # bracket is closer
            if brackets[bracket] == stack.peek():
                stack.pop()
            else:
                return "NO"

    if stack.is_empty():
        return "YES"
    else:
        return "NO"

def isBalancedNoStack(s):
    brackets = {
        '(' : ')' ,
        '[' : ']',
        '{' : '}'
    }
    stack = []
    for bracket in s:
        if bracket in brackets.keys():
            stack.append(bracket)
        else: # bracket is closer
            if len(stack):
                if brackets[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return "NO"
    if len(stack):
        return "NO"
    else:
        return "YES"


# Balanced Brackets - HARD

# {{([)]}} is fine

def isBalancedHard(s):
    stacks = {
        ')' : [],
        ']' : [],
        '}' : []
    }
    pairs = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    for bracket in s:
        # Opening bracket
        if bracket in pairs.keys():
            stacks[pairs[bracket]].append(bracket)
        else: # Closing bracket
            if len(stacks[bracket]) != 0:
                stacks[bracket].pop()
            else:
                return "NO"

    for key in stacks:
        if len(stacks[key]) != 0:
            return "NO"

    return "YES"

print(isBalancedNoStack('(())(())'))
