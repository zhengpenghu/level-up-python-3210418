import heapq

# testing point: regex to process text input
# counter to efficiently count

def count_words(input_path):
    word_count = dict()
    total_cnt = 0
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                if not word.isalnum():
                    continue
                if word.lower() not in word_count:
                    word_count[word.lower()] = 0
                word_count[word.lower()] += 1
                total_cnt += 1

    top20 = []
    for word, cnt in word_count.items():
        heapq.heappush(top20, (cnt, word))
        if len(top20) > 20:
            heapq.heappop(top20)

    ans = [(item[1], item[0]) for item in top20]

    print(f"Total Words: {total_cnt}")
    print("Top 20 Words:")
    for t in reversed(ans):
        print(f'{t[0]}    {t[1]}')

# output inconsistent with standard solution
# Fail to consider - and comma: twenty-two, that's

if __name__ == '__main__':
    count_words('shakespeare.txt')
