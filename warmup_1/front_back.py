# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str
    
    front = str[0]
    back = str[-1]
    mid = str[1 : -1]
    
    return back + mid + front

print(front_back('code')) # → 'eodc'
print(front_back('a')) # → 'a'
print(front_back('ab')) # → 'ba'