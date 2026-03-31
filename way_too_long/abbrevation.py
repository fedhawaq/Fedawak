n = int(input())
words = [input().strip() for i in range(n)]
for word in words:
    if len(word) > 10:
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        print(abbreviation)
    else:
        print(word)
     


