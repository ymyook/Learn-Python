def collatz(number):
        if number%2 == 0:
            print(number // 2)
            return number // 2
        else:
            print(3*number+1)
            return 3*number+1

print('Enter your number: ')

try:
    mynumber = int(input())
    while mynumber != 1:                                           
        mynumber = collatz(mynumber)
except:
    print('Enter a integer.')
