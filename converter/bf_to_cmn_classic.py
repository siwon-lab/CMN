def bf_to_cmn_classic(code):
   table = {
      '>': 'R',
      '<': 'L',
      '+': 'U',
      '-': 'D',
      '.': 'F',
      ',': 'B',
      '[': '(',
      ']': ')',
   }
   result = []
   for cmd in code:
      if cmd in table:
         result.append(table[cmd])
    
   converted = ' '.join(result)
   converted = converted.replace('( ', '(').replace(' )', ')')
   return converted

if __name__ == '__main__':
   code = input("Input: ")
   print(bf_to_cmn_classic(code))