# CMN (Cube Move Notation) Programming Language
CMN is an esoteric programming language inspired by Rubik's Cube move notations.

## CMN Classic
CMN Classic is the first version of the CMN family. It features 8 commands that map 1:1 with Brainfuck's.

### Commands
|cmd|meaning|
|---|---|
|**R**|Move the pointer to the right.|
|**L**|Move the pointer to the left.|
|**U**|Increment the byte at the pointer.|
|**D**|Decrement the byte at the pointer.|
|**F**|Output the byte at the pointer.|
|**B**|Input a byte and store it at the pointer.|
|**(**|Jump forward to `)` if the byte at the pointer is 0.|
|**)**|Jump backward to `(` if the byte at the pointer is nonzero.|

### How to Run
To Run:
```
python3 interpreter/classic.py
```
else,
```
cd interpreter
python3 classic.py
```

### Example Code
Input:
```
U U U U U U U U U U (R U U U U U U U R U U U U U U U U U U R U U U R U L L L L D) R U U F R U F U U U U U U U F F U U U F R U U U U U U U U U U U U U U F D D D D D D D D D D D D F L L U U U U U U U U U U U U U U U F R F U U U F D D D D D D F D D D D D D D D F R U F R F
```
Output:
```
Hello, World!
```

### Brainfuck to CMN Classic Converter
A tool to convert Brainfuck code to CMN Classic.
To Run:
```
python3 converter/bf_to_cmn_classic.py
```
else,
```
cd converter
python3 bf_to_cmn_classic.py
```
