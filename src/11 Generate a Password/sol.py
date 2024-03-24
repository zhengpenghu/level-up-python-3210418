import random

# testing point: 
# 1. in security or cryptography using secrets > random
# 2. how to process text in file -- WAI: brittle hardcode based on file pattern, never adaptive.

def generate_passphrase(word_num):
    word_set = set()
    with open('diceware.wordlist.asc', 'r') as file:
        for line in file:
            if len(line.split()) == 2:
                word_set.add(line.split()[1])
    ans = []
    ans.extend(random.choices(list(word_set), k=word_num))
    return ' '.join(ans)


if __name__ == "__main__":
    print(generate_passphrase(4))
# 'correct horse battery staple'
