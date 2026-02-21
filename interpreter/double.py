import sys
import re

def cmn_double(code):
   code = re.sub(r'\)2', ' )2 ', code)
   code = re.sub(r'\(', ' ( ', code)
   code = re.sub(r'\)(?!2)', ' ) ', code)
   code = code.split()
   stack = []
   loops = {}
   loop_type = {}
   for i, cmd in enumerate(code):
         if cmd == "(":
            stack.append(i)
         elif cmd in (")", ")2"):
            if not stack:
               print("Undefined")
               return
            j = stack.pop()
            loops[j] = i
            loops[i] = j
            loop_type[j] = cmd
   if stack:
      print("Undefined")
      return

   memory = [0] * 30000
   ptr1 = 0
   ptr2 = 0
   i = 0

   while i < len(code):
      cmd = code[i]
      match cmd:
            case "R" | "R2" | "R'":
               ptr1 += 1
               if ptr1 >= 30000:
                  print("Undefined")
                  return
               match cmd:
                  case "R":
                     memory[ptr1] = (memory[ptr1] + 1) % 256
                  case "R2":
                     memory[ptr1] = (memory[ptr1] + 2) % 256
                  case "R'":
                     memory[ptr1] = (memory[ptr1] - 1) % 256
            case "L" | "L2" | "L'":
               ptr1 -= 1
               if ptr1 < 0:
                  print("Undefined")
                  return
               match cmd:
                  case "L":
                     memory[ptr1] = (memory[ptr1] - 1) % 256
                  case "L2":
                     memory[ptr1] = (memory[ptr1] - 2) % 256
                  case "L'":
                     memory[ptr1] = (memory[ptr1] + 1) % 256
            case "U" | "U2" | "U'":
               ptr2 += 1
               if ptr2 >= 30000:
                  print("Undefined")
                  return
               match cmd:
                  case "U":
                     memory[ptr2] = (memory[ptr2] + 1) % 256
                  case "U2":
                     memory[ptr2] = (memory[ptr2] + 2) % 256
                  case "U'":
                     memory[ptr2] = (memory[ptr2] - 1) % 256
            case "D" | "D2" | "D'":
               ptr2 -= 1
               if ptr2 < 0:
                  print("Undefined")
                  return
               match cmd:
                  case "D":
                     memory[ptr2] = (memory[ptr2] - 1) % 256
                  case "D2":
                     memory[ptr2] = (memory[ptr2] - 2) % 256
                  case "D'":
                     memory[ptr2] = (memory[ptr2] + 1) % 256
            case "F":
               print(chr(memory[ptr1]), end="")
            case "F2":
               if ptr1 != ptr2:
                  memory[ptr2] = memory[ptr1]
            case "F'":
               c = sys.stdin.read(1)
               memory[ptr1] = ord(c[0]) if c else 0
            case "B":
               print(chr(memory[ptr2]), end="")
            case "B2":
               if ptr1 != ptr2:
                  memory[ptr1] = memory[ptr2]
            case "B'":
               c = sys.stdin.read(1)
               memory[ptr2] = ord(c[0]) if c else 0
            case "(":
               t = loop_type[i]
               ptr = ptr1 if t == ")" else ptr2
               if memory[ptr] == 0:
                  i = loops[i]
            case ")":
               if memory[ptr1] != 0:
                  i = loops[i]
            case ")2":
               if memory[ptr2] != 0:
                  i = loops[i]
            case _:
               print("Undefined")
               return
      i += 1
   print()

if __name__ == "__main__":
   code = input("Input: ")
   cmn_double(code)