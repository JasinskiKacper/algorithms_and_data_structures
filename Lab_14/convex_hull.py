
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'[{self.x}, {self.y}]'
        
       
def direction(p1: Point, p2: Point, p3: Point) -> str:
    res = ((p2.y - p1.y) * (p3.x - p2.x)) - ((p3.y - p2.y) * (p2.x - p1.x))

    if res > 0:
        return 'right'
    elif res < 0:
        return 'left'
    else:
        return 'collinear'
    
def jarvis(points: list) -> list:
    res = []
    min_val = float('inf')
    min_idx = None
    
    for idx, point in enumerate(points):

        if point.x < min_val:
            min_val = point.x
            min_idx = idx
        elif point.x == min_val:
            if point.y < points[min_idx].y:
                min_val = point.x
                min_idx = idx
                
    p = points[min_idx]
    
    while True:
        res.append(p)

        if points[0] != p:
            q = points[0]
        else:
            q = points[1]

        for r in points:
            if r != p and r !=q:
                dire = direction(p, q, r)
                
                if dire == 'right':
                    q = r

                elif dire == 'collinear':
                    dist_pq = (q.x - p.x)**2 + (q.y - p.y)**2
                    dist_pr = (r.x - p.x)**2 + (r.y - p.y)**2
                    
                    if dist_pr > dist_pq:
                        q = r    
        
        if q == res[0]:
            break
        
        p = q
        
    return res
    
def graham(points: list) -> list:
    res = []
    min_val = float('inf')
    min_idx = None
    
    for idx, point in enumerate(points):

        if point.y < min_val:
            min_val = point.y
            min_idx = idx
        elif point.y == min_val:
            if point.x < points[min_idx].x:
                min_val = point.y
                min_idx = idx
                
    p0 = points[min_idx]
    res.append(p0)

    others = [p for p in points if p != p0]
    for _ in range(len(others)):
        for j in range(len(others) - 1):
            p1 = others[j]
            p2 = others[j + 1]
            
            dire = direction(p0, p1, p2)
            
            swap = False
            if dire == 'right':
                swap = True
            elif dire == 'collinear':
                dist1 = (p1.x - p0.x)**2 + (p1.y - p0.y)**2
                dist2 = (p2.x - p0.x)**2 + (p2.y - p0.y)**2
                if dist1 > dist2:
                    swap = True
                    
            if swap:
                others[j], others[j + 1] = others[j + 1], others[j]

    sorted_p = [p0] + others
    filtered = [sorted_p[0]]
    i = 1

    while i < len(sorted_p):
        while (i < len(sorted_p) - 1 and direction(p0, sorted_p[i], sorted_p[i + 1]) == 'collinear'):
            i += 1

        filtered.append(sorted_p[i])
        i += 1

    if len(filtered) < 3:
        return []

    stack = [filtered[0], filtered[1], filtered[2]]

    for i in range(3, len(filtered)):
        while (len(stack) >= 2 and direction(stack[-2], stack[-1], filtered[i]) != 'left'):
            stack.pop()

        stack.append(filtered[i])

    return stack


def main():
    print('=== Jarvis ===')
    p1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    points1 = []
    for x, y in p1:
        points1.append(Point(x, y))
        
    print(jarvis(points1))
    
    p2 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    points2 = []
    for x, y in p2:
        points2.append(Point(x, y))
        
    print(jarvis(points2))

    print('=== Graham ===')
    g1 = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    graham1 = []
    for x, y in g1:
        graham1.append(Point(x, y))
        
    print(graham(graham1))

if __name__ == '__main__':
    main()
    