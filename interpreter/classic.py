import sys

def cmn_classic(code):
    code = code.replace("(", " ( ").replace(")", " ) ")
    code = code.split()
    stack = []
    loops = {}
    for i, cmd in enumerate(code):
        if cmd == "(":
            stack.append(i)
        elif cmd == ")":
            j = stack.pop()
            loops[j] = i
            loops[i] = j

    memory = [0] * 30000
    pointer = 0
    i = 0

    while i < len(code):
        cmd = code[i]
        match cmd:
            case "R":
                pointer += 1
                if pointer >= 30000:
                    print("Undefined")
                    break
            case "L":
                pointer -= 1
                if pointer < 0:
                    print("Undefined")
                    break
            case "U":
                memory[pointer] = (memory[pointer] + 1) % 256
            case "D":
                memory[pointer] = (memory[pointer] - 1) % 256
            case "F":
                print(chr(memory[pointer]), end="")
            case "B":
                c = sys.stdin.read(1)
                memory[pointer] = ord(c[0]) if c else 0
            case "(":
                if memory[pointer] == 0:
                    i = loops[i]
            case ")":
                if memory[pointer] != 0:
                    i = loops[i]
            case _:
                print("Undefined")
                break
        i += 1
    print()

if __name__ == "__main__":
    code = input("Input: ")
    cmn_classic(code)