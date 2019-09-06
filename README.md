# UPC_Validity_Checker


Checks if a given UPC is valid using checksum.

## Usage:


```>python3 upc.py```

\n
Utilizes following algorithm:
1) Sum the odd-numbered digits 
2) Multiply the result by 3
3) Add the even-numbered digits to this sum
4) IF sum modulo 10 is 0 then UPC is Valid!

