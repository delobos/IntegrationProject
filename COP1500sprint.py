# Sprint 1
quick_maths = (2+2-1) ** 3 //3 * 10 / 5 % 5

# Sprint 2
rows = int(input('Enter a number'))
def sprint2(rows):
    for x in range(1, rows + 1):
        rows -= 1
        for x in range(1, rows + 2):
            print(x, end=' ')
        print()

sprint2(8)
sprint2(rows)
