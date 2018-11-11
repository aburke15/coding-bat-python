# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).

# I guess they don't care if n exceeds the bounds of the arr str?


def missing_char(str, n):
    beg = str[:n]       # from 0 to n but not including char at index n
    end = str[n + 1:]   # from n + 1 (so not including n) to the end of the string
    return beg + end


print(missing_char('kitten', 1))  # → 'ktten'
print(missing_char('kitten', 0))  # → 'itten'
print(missing_char('kitten', 4))  # → 'kittn'
