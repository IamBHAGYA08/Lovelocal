def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count


n = 13
total_count = countDigitOne(n)
print(total_count)