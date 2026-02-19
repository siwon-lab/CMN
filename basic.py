def brainfuck(code):
    code = code.replace('(', '( ').replace(')', ' )')
    code = code.split()
    stack = []
    loops = {}
    for i, cmd in enumerate(code):
        if cmd == '(':
            stack.append(i)
        elif cmd == ')':
            j = stack.pop()
            loops[j] = i
            loops[i] = j

    memory = [0] * 30000
    pointer = 0
    i = 0

    while i < len(code):
        cmd = code[i]
        if cmd == 'R':
            pointer += 1
        elif cmd == 'L':
            pointer -= 1
        elif cmd == 'U':
            memory[pointer] += 1
        elif cmd == 'D':
            memory[pointer] -= 1
        elif cmd == 'F':
            print(chr(memory[pointer]), end="")
        elif cmd == 'B':
            c = input("Additional Input: ")
            memory[pointer] = ord(c[0]) if c else 0
        elif cmd == '(':
            if memory[pointer] == 0:
                i = loops[i]
        elif cmd == ')':
            if memory[pointer] != 0:
                i = loops[i]
        i += 1
    print()

code = input("Initial Input: ")
brainfuck(code)