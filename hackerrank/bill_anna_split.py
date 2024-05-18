def bonAppetit(bill, k, b):
    # Write your code here
    temp = bill[k]
    res = sum(bill)
    res -= temp
    an = res/2
    if b==an:
        print("Bon Appetit")
    else:
        print(int(b-an))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
