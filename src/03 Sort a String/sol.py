
def sort_words(strs):
    # Use casefold instead of lowercase to enhance case insensitivity, for multi-lang support.
    return " ".join(sorted(strs.split(), key=str.casefold))


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
