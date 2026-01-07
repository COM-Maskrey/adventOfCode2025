def parse_input(filename):
    with open(filename) as f:
        return [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]


def get_green_tiles(red_tiles):
    # Use the ordered red tile list as the polygon boundary
    boundary = red_tiles[:]
    xs = [x for x, y in boundary]
    ys = [y for x, y in boundary]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    green = set(boundary)
    # Also add all border points (the path between red tiles)
    border = set()
    n = len(boundary)
    for i in range(n):
        x1, y1 = boundary[i - 1]
        x2, y2 = boundary[i]
        border.add((x1, y1))
        if x1 == x2:
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                border.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                border.add((x, y1))
    border.add(boundary[-1])
    green.update(border)
    def point_in_poly(x, y, poly):
        n = len(poly)
        inside = False
        for i in range(n):
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % n]
            if y1 == y2:
                continue
            if min(y1, y2) < y <= max(y1, y2):
                xinters = (y - y1) * (x2 - x1) / (y2 - y1 + 1e-9) + x1
                if xinters >= x:
                    inside = not inside
        return inside
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if point_in_poly(x, y, boundary):
                green.add((x, y))
    return green, x_min, x_max, y_min, y_max

def main():
    red_tiles = parse_input('Day 9/Part 2/Day_9_2_Input.csv')
    green, x_min, x_max, y_min, y_max = get_green_tiles(red_tiles)
    red_set = set(red_tiles)
    # Use a sparse grid and sparse summed-area table
    from collections import defaultdict
    grid = defaultdict(int)
    for (x, y) in green:
        grid[(x, y)] = 1
    for (x, y) in red_set:
        grid[(x, y)] = 1
    # Build sparse summed-area table
    sat = defaultdict(int)
    # Only fill sat for points that exist in grid
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            sat[(x, y)] = grid[(x, y)] + sat[(x - 1, y)] + sat[(x, y - 1)] - sat[(x - 1, y - 1)]
    max_area = 0
    for i, (x1, y1) in enumerate(red_tiles):
        for j in range(i + 1, len(red_tiles)):
            x2, y2 = red_tiles[j]
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            total = sat[(max_x, max_y)] - sat[(min_x - 1, max_y)] - sat[(max_x, min_y - 1)] + sat[(min_x - 1, min_y - 1)]
            if total == area:
                if area > max_area:
                    max_area = area
    print(max_area)

if __name__ == '__main__':
    main()
