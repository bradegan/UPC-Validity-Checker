# UPC_Validity_Checker


Checks if a given UPC is valid using checksum.

## Usage:


```>python3 upc.py```


Utilizes following algorithm:
1) Sum the odd-numbered digits 
2) Multiply the result by 3
3) Add the even-numbered digits 
4) Find the result modulo 10
