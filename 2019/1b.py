start = 100000
palindromes = []
while start > 1:
    start -= 1
    if str(start) == str(start)[::-1]:
        palindromes.append(start)
print(palindromes)

memo = {}
for i in range(1,100000):
    pali_in = False
    for pali in palindromes:
        if i - pali in palindromes:
            pali_in = True
    memo[i] = pali_in
print(memo)
count = 0
for i in memo.values():
    if not i:
        count += 1
print(count)