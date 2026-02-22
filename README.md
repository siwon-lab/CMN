# CMN (Cube Move Notation) Programming Language
CMN is an esoteric programming language inspired by Rubik's Cube move notations.

## CMN Classic
CMN Classic is the first version of the CMN family. It features 8 commands that map 1:1 with Brainfuck's.

### Commands
|cmd|in bf|meaning|
|:---:|:---:|:---|
|**R**|>|Move the pointer to the right.|
|**L**|<|Move the pointer to the left.|
|**U**|+|Increment the byte at the pointer.|
|**D**|-|Decrement the byte at the pointer.|
|**F**|.|Output the byte at the pointer.|
|**B**|,|Input a byte and store it at the pointer.|
|**(**|[|Jump forward to `)` if the byte at the pointer is 0.|
|**)**|]|Jump backward to `(` if the byte at the pointer is nonzero.|

### How to Run
To Run:
```
python3.14 interpreter/classic.py <<< "(code)"
```
else,
```
cd interpreter
python3.14 classic.py <<< "(code)"
```
Example:
```
python3.14 converter/bf_to_cmn_classic.py <<< "B R F"
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
python3.14 converter/bf_to_cmn_classic.py <<< "(code)"
```
else,
```
cd converter
python3.14 bf_to_cmn_classic.py <<< "(code)"
```

## CMN Double
CMN Double is the second version of the CMN family. It features 21 commands and two pointers sharing the same tape.

### Commands
|cmd|in bf|meaning|
|:---:|:---:|:---|
|**R**|>+ (ptr1)|Move the pointer1 to the right and increment the byte.|
|**R2**|>++ (ptr1)|Move the pointer1 to the right and increment the byte by 2.|
|**R'**|>- (ptr1)|Move the pointer1 to the right and decrement the byte.|
|**L**|<- (ptr1)|Move the pointer1 to the left and decrement the byte.|
|**L2**|<-- (ptr1)|Move the pointer1 to the left and decrement the byte by 2.|
|**L'**|<+ (ptr1)|Move the pointer1 to the left and increment the byte.|
|**U**|>+ (ptr2)|Move the pointer2 to the right and increment the byte.|
|**U2**|>++ (ptr2)|Move the pointer2 to the right and increment the byte by 2.|
|**U'**|>- (ptr2)|Move the pointer2 to the right and decrement the byte.|
|**D**|<- (ptr2)|Move the pointer2 to the left and decrement the byte.|
|**D2**|<-- (ptr2)|Move the pointer2 to the left and decrement the byte by 2.|
|**D'**|<+ (ptr2)|Move the pointer2 to the left and increment the byte.|
|**F**|. (ptr1)|Output the byte at the pointer1.|
|**F2**|-|Copy the byte from pointer1 to pointer2.|
|**F'**|, (ptr1)|Input a byte and store it at the pointer1.|
|**B**|. (ptr2)|Output the byte at the pointer2.|
|**B2**|-|Copy the byte from pointer2 to pointer1.|
|**B'**|, (ptr2)|Input a byte and store it at the pointer2.|
|**(**|[ (ptr1, ptr2)|Jump forward to `)` or `)2` if the byte at the pointer is 0.|
|**)**|] (ptr1)|Jump backward to `(` if the byte at the pointer1 is nonzero.|
|**)2**|] (ptr2)|Jump backward to `(` if the byte at the pointer2 is nonzero.|

### How to Run
To Run:
```
python3.14 interpreter/double.py <<< "(code)"
```
else,
```
cd interpreter
python3.14 double.py <<< "(code)"
```
Example:
```
python3.14 interpreter/double.py <<< "F' R L' R' L' R L' R' L2 F"
```

### Example Code
|code|result|
|---|---|
|R2 R L R' L|Move the pointer1 to the right. (`>` in bf)|
|L' R2 L R' L' R' L|Move the pointer1 to the left. (`<` in bf)|
|R L' R' L'|Increment the byte at the pointer1 by 2. (`++` in bf)|
|R L' R' L2|Decrement the byte at the pointer1. (`-` in bf)|
