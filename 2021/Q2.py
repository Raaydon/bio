from collections import defaultdict, deque

snake_length, instructions, num_loops = input().split()
snake_length, num_loops = int(snake_length), int(num_loops)

lenInst = len(instructions)

N = (0,1)
S = (0,-1)
W = (-1,0)
E = (1,0)

turns = {
    'L': {N:W, W:S, S:E, E:N}, # if turning left, facing north -> facing west
    'R': {N:E, E:S, S:W, W:N},
    'F': {N:N, E:E, S:S, W:W}
    }

explorer = (0,0) # x,y
heading = N # dx, dy

# Choose your implementation!
# 1) A queue of locations
# 2) A grid of time values

trail = deque(maxlen=snake_length) # when the length is more than snake_length the first item gets removed
trail.append(explorer)


for i in range(num_loops):
    curr_instruction = instructions[i%lenInst] # 0,1,0,1,0,1,0
    heading = turns[curr_instruction][heading]
    next_explorer = (explorer[0] + heading[0],
                     explorer[1]  +heading[1])
    if next_explorer in trail:
        for _ in range(4):
            heading = turns['R'][heading]
            next_explorer = (explorer[0] + heading[0],
                            explorer[1]  +heading[1])
            if next_explorer not in trail:
                break
        else:
            print('no possible moves')
            break
    explorer = next_explorer
    trail.append(explorer)
    
print(explorer)