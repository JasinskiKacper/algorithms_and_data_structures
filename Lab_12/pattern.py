
import time

with open("lotr.txt", encoding='utf-8') as f:

        text = f.readlines()

S = ' '.join(text).lower()

def naive(S: str, W: str) -> tuple:
    m = 0
    i = 0

    match = 0
    comparison = 0
    idx = []
    while i < len(S) - len(W) + 1:
        comparison +=1
        if S[m: len(W) + m] == W:
            match += 1
            idx.append(m)
            
        m += 1
        i += 1

    return (match, comparison, idx)

def hash(word):
    hw = 0
    d = 256
    q = 101
    for i in range(len(word)):
        hw = (hw * d + ord(word[i])) % q  
        
    return hw

def rabin(S: str, W: str) -> tuple:
    hW = hash(W)
    
    match = 0
    comparison = 0
    collision = 0
    idx = []
    for m in range(len(S) - len(W) + 1):
        
        hS = hash(S[m: m + len(W)])
    
        if hS == hW:
            if S[m: m + len(W)] == W:
                match += 1
                idx.append(m)
            else:
                collision += 1
        comparison += 1
    
    return (match, comparison, idx, collision)

def rabin_roll(S: str, W: str) -> tuple:
    d = 256
    q = 101
    hW = hash(W)
    
    match = 0
    comparison = 0
    collisions = 0
    idx = []

    h = 1

    for _ in range(len(W) - 1):
        h = (h * d) % q

    hS = hash(S[0: 0 + len(W)])
    for m in range(len(S) - len(W) + 1):
    
        if hS == hW:
            if S[m: m + len(W)] == W:
                match += 1
                idx.append(m)
            else:
                collisions += 1
        comparison += 1
    
        if m < len(S) - len(W):
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m+len(W)])) % q
            if hS < 0:
                hS += q
    
    return (match, comparison, idx, collisions)
    
def main():
    t_start = time.perf_counter()
    match_1, comparison_1, idx_1 = naive(S, 'time.')
    t_stop = time.perf_counter()
    time_1 = t_stop - t_start
    print('=== NAIVE ===')
    print(f'{match_1}; {comparison_1}; {time_1:.7f}')
    
    t_start = time.perf_counter()
    match_2, comparison_2, idx_2, collisions_2 = rabin(S, 'time.')
    t_stop = time.perf_counter()
    time_2 = t_stop - t_start
    print('=== RABIN ===')
    print(f'{match_2}; {comparison_2}; {time_2:.7f}; {collisions_2}')
    
    t_start = time.perf_counter()
    match_3, comparison_3, idx_3, collisions_3 = rabin_roll(S, 'time.')
    t_stop = time.perf_counter()
    time_3 = t_stop - t_start
    print('=== RABIN  ROLL ===')
    print(f'{match_3}; {comparison_3}; {time_3:.7f}; {collisions_3}')

if __name__ == '__main__':
    main()