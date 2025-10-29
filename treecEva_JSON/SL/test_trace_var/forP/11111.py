def main():
    a = 1
    b = 2
    c = 3
    c = a + b
    for i in range(3):
        a = b + 1
        b = b + c
    if a != 0:
        a  = a+1
    if b == 0 :
        b = 1
    print(a)
    return 0

if __name__ == '__main__':
    main()


    