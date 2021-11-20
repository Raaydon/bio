source = input()

source = source.split(' ')

def is_pat(potential_pat):
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
    if not is_pat(reversed(left)) or not is_pat(reversed(right)):
        return False
    
    
    
            

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
    