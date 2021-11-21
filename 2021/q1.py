source = input()

source = source.split(' ')

def left_right_split(potential_pat):
    left = ''
    right = ''
    if len(potential_pat) % 2 == 0: # if there are an even number of characters
        
        for i,char in enumerate(potential_pat):
            if i + 1 <= len(potential_pat)/2:
                left += char
            else:
                right += char
            
    else: # if there are odd characters
        
        for i,char in enumerate(potential_pat):
            if i <= len(potential_pat)/2:
                left += char
            else:
                right += char
    return left, right
def is_pat(potential_pat):
    potential_pat = potential_pat.upper()
    
    left, right = left_right_split(potential_pat)
    
    list_left, list_right = list(left), list(right)
    
    if list_right: # if longer than 1 char
        max_right = max(list_right)
    else: # otherwise it is a pat
        return True
    
    for char in list_left:
        if char < max_right:
            return False
    
    
    left, right = left[::-1], right[::-1]
    
    return is_pat(left) and is_pat(right)
    
            

s1 = source[0]
s2 = source[1]

if is_pat(s1):
    print('YES')
else:
    print('NO')
    
    
if is_pat(s2):
    print('YES')
else:
    print('NO')
    
    
if is_pat(s1+s2):
    print('YES')
else:
    print('NO')
    