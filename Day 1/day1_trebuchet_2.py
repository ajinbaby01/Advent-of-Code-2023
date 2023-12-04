digit_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

class Trie:
    def __init__(self, digit_mapping, reversed=False):
        self.trie = {}
        keys = digit_mapping.keys()
        for num in keys:
            if reversed:
                num = num[::-1]
            node = self.trie
            for c in num:
                if c not in node:
                    node[c] = {}
                node = node[c]
            if reversed:
                num = num[::-1]
            node['word'] = digit_mapping[num]

    def search(self, text):
        node = self.trie
        for c in text:
            if 'word' in node:
                return node['word']
            if c.isdigit():
                return int(c)
            if c not in node:
                return None
            node = node[c]
        return None

        # def recursive_search(node, text):
        #     if len(text) == 0:
        #         return None

        #     if 'word' in node:
        #         return node['word']

        #     if text[0].isdigit():
        #         return int(text[0])

        #     if text[0] not in node:
        #         return None

        #     node = node[text[0]]

        #     return recursive_search(node, text[1:])

        # node = self.trie
        # return recursive_search(node, text)


file_path = "Day 1/day1_trebuchet_input.txt"

with open(file_path, "r") as f:
    total_sum = 0
    trie = Trie(digit_mapping)
    reverse_trie = Trie(digit_mapping, reversed=True)

    for line in f:
        for i in range(len(line)):
            first_number = trie.search(line[i:])
            if first_number is not None:
                break
        line = line[::-1]
        for i in range(len(line)):
            last_number = reverse_trie.search(line[i:])
            if last_number is not None:
                break

        if first_number is None:
            first_number = last_number
        if last_number is None:
            last_number = first_number

        print(first_number, end='')
        print(last_number, end='')
        print()
        total_sum += first_number * 10 + last_number

print(total_sum)
