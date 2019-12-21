# Night at the Museum
word = [1] + list(input())

i = 1
while i < len(word):
    word[i] = ord(word[i]) - 96
    i += 1

count = 0
i = 1
while i < len(word):
    turn = word[i] - word[i-1]
    count += min(turn % 26, - turn % 26)
    i += 1

print(count)
