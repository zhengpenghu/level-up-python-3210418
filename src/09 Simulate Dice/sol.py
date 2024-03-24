# actual testing point is randint and Counter


def roll_dice(*args):
    total = 1
    for num in args:
        total *= num

    def getcomb(num, args):
        if num == 0 and len(args) == 0:
            return 1
        if num == 0 or len(args) == 0:
            return 0

        cnt = 0
        for can in range(1, min(num, args[0])+1, 1):
            cnt += getcomb(num-can, args[1:])
        return cnt

    print("OUTCOME PROBABILITY")
    print(args)

    for target in range(len(args), sum(args), 1):
        prob = getcomb(target, args)/total
        print(f'{target}     {prob*100:.2f}%')


# commands used in solution video for reference
if __name__ == '__main__':
    roll_dice(4, 6, 6)
    # roll_dice(4, 6, 6, 20)

    # OUTCOME PROBABILITY
# 3       0.69%
# 4       2.06%
# 5       4.14%
# 6       6.95%
# 7       9.70%
# 8       12.55%
# 9       13.93%
# 10      13.85%
# 11      12.52%
# 12      9.70%
# 13      6.95%
# 14      4.17%
# 15      2.09%
# 16      0.70%
