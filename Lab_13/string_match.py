
def match_rek(P: str, T: str, 
             i: int, j: int) -> int:
    if i == 0:
        return j
    if j == 0:
        return i

    cost_in = 1 + match_rek(P, T, i, (j - 1))
    cost_del = 1 + match_rek(P, T, (i - 1), j)
    cost_trade = match_rek(P, T, (i - 1), (j - 1))

    if P[i] != T[j]:
        cost_trade += 1
            
    return min(cost_in, cost_del, cost_trade)

def match_pd(P: str, T: str, i: int, j: int, p_E: bool = False) -> tuple:
    D = [[0 for _ in range(j)] for _ in range(i)]
    parent = [['X'] * j for _ in range(i)]

    for Tj in range(j):
        D[0][Tj] = Tj
        parent[0][Tj] = 'I'
    for Pi in range(i):
        D[Pi][0] = Pi
        parent[Pi][0] = 'D'
    parent[0][0] = 'X'

    for pi in range(1, len(P)):
        for tj in range(1, len(T)):
            cost_in = D[pi][tj - 1] + 1
            cost_del = D[pi - 1][tj] + 1
            cost_trade = D[pi - 1][tj - 1]

            if P[pi] != T[tj]:
                if p_E:
                    cost_trade += 1000
                else:
                    cost_trade += 1

            D[pi][tj] = min(cost_in, cost_del, cost_trade)

            if cost_trade == min(cost_in, cost_del, cost_trade):
                parent[pi][tj] = 'M' if P[pi] == T[tj] else 'R'
            elif cost_in == min(cost_in, cost_del, cost_trade):
                parent[pi][tj] = 'I'
            else:
                parent[pi][tj] = 'D'

    path = []
    pi = i - 1
    tj = j - 1

    while parent[pi][tj] != 'X':
        op = parent[pi][tj]
        path.append((op, P[pi]))
        if op == 'M' or op == 'R':
            pi -= 1; tj -= 1
        elif op == 'D':
            pi -= 1
        else:
            tj -= 1

    path.reverse()
    lcs = ''.join(litera for op, litera in path if op == 'M')
    return (D[-1][-1], ''.join(op for op, _ in path), lcs)

def match_pd_D(P: str, T: str, i: int, j: int,) -> tuple:
    D = [[0 for _ in range(j)] for _ in range(i)]

    for Tj in range(j):
        D[0][Tj] = 0
    for Pi in range(i):
        D[Pi][0] = Pi

    for pi in range(1, len(P)):
        for tj in range(1, len(T)):
            cost_in = D[pi][tj - 1] + 1
            cost_del = D[pi - 1][tj] + 1
            cost_trade = D[pi - 1][tj - 1]

            if P[pi] != T[tj]:
                cost_trade += 1
            
            D[pi][tj] = min(cost_in, cost_del, cost_trade)

    min_last_row = min(D[-1])
    end_P = D[-1].index(min_last_row)

    return ((end_P - len(P) + 1), min_last_row)

def main():
    # === Podpunkt A ===
    print('=== Podpunkt A ===')
    print(match_rek(' kot', ' koń', i=3, j=3))
    print(match_rek(' kot', ' pies', i=3, j=4))
    
    # === Podpunkt B ===
    print('=== Podpunkt B ===')
    res, _, _ = match_pd(' kot', ' koń', i=4, j=4)
    print(res)

    res, _, _ = match_pd(' kot', ' pies', i=4, j=5)
    print(res)

    # === Podpunkt C ===
    print('=== Podpunkt C ===')
    res, path, _ = match_pd(' thou shalt not', ' you should not', i=15, j=15)
    print(path)

    # === Podpunkt D ===
    print('=== Podpunkt D ===')
    P = ' ban'
    T = ' mokeyssbanana'

    print(match_pd_D(P, T, len(P), len(T)))
    print(match_pd_D(' bin', T, len(P), len(T)))

    # === Podpunkt E ===
    print('=== Podpunkt E ===')
    P = ' democrat'
    T = ' republican'

    print(match_pd(P, T, len(P), len(T), p_E=True))

    # === Podpunkt F ===
    print('=== Podpunkt F ===')
    T = ' 243517698'
    P = ' ' + ''.join(sorted(T.strip()))
    _, _, lcs = match_pd(P, T, len(P), len(T), p_E=True)
    print(lcs)

if __name__ == '__main__':
    main()