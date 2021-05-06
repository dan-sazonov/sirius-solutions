n = int(input())
words = {}
mistakes = 0

for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in words:
        words[base_form] = set()
    words[base_form].add(word)
for word in input().split():
    base_form = word.lower()
    uppercase_counter = len([l for l in word if l.isupper()])
    if (base_form in words and word not in words[base_form]) or uppercase_counter != 1:
        mistakes += 1

print(mistakes)
