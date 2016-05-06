# function to find square of a number to the closest integer

def sq(inNum): 
    if inNum < 0: 
        raise ValueError 
    if inNum == 1:
        return 1

    low = 0 
    high = 1 + (inNum / 2) 
    
    while (low + 1) < high: 
        mid = low + ((high - low) / 2) 
        square = mid**2

        if square == inNum: 
            return mid 
        elif square < inNum: 
            low = mid 
        else: 
            high = mid 
            
    return low

def main():
    uInput = int(raw_input('Enter number > '))
    print sq(uInput)

if __name__ == '__main__':
    main()