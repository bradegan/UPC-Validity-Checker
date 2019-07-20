'''
    CS5001
    Fall 2018
    HW3
    Brad Egan
'''


'''
Test Input: 9781491939369
Expected Output: "Valid UPC!!!"

Test Input: 1
Expected Output: "Not a valid UPC"

Test Input: 762111198464
Expected Output: "Valid UPC!!!"

Test Input: 070972362000
Expected Output: "Valid UPC!!!"

Test Input: 0709723620001
Expected Output: "Not a valid UPC"

'''


def main():
    
    # User inputs UPC code.
    upc = input("Please enter your UPC code.\n")
    
    # UPC string is reversed as position zero is defined as far right
    # and python considers position zero to be on far left.
    upc_reverse = upc[::-1]

    # Initializes total variable.
    total = 0

    # Loops through the upc string and if the index number is even then
    # corresponding value is added to total. Otherwise, (when odd) the
    # corresponding value is multiplied by 3 and added to total.
    
    for i in range(len(upc_reverse)):
        if i % 2 == 0:
            total += int(upc_reverse[i])
        else:
            total += int(upc_reverse[i]) * 3
              
    # If the total is divisable by ten prints as valid otherwise, otherwise not
    # valid.
    if total % 10 == 0:
        print("Valid UPC!!!")
    else:
        print("Not a valid UPC")

main()
