# >>> example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# >>> index_all(example, 2)
# [[0, 0, 1], [0, 1], [1, 1]]
# >>> print(index_all(example, [1, 2, 3]))
# [[0, 0], [1]]

# recursion
def index_all(examples, target):
    ans = []
    for idx, val in enumerate(examples):
        if val == target:
            ans.append([idx])
        elif isinstance(val, list):
            for x in index_all(val, target):
                ans.append([idx]+x)
    return ans


if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))
# [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))
# [[0, 0], [1]]
