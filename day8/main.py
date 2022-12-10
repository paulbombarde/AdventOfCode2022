import sys


def visible_range(map, ibeg, iend, jbeg, jend, ref):
    for i in range(ibeg, iend):
        for j in range(jbeg, jend):
            if ref <= map[i][j]:
                return False
    return True


def visible_north(map, i, j):
    return visible_range(map, i+1, len(map), j, j+1, map[i][j])


def visible_south(map, i, j):
    return visible_range(map, 0, i, j, j+1, map[i][j])


def visible_east(map, i, j):
    return visible_range(map, i, i+1, j+1, len(map[0]), map[i][j])


def visible_west(map, i, j):
    return visible_range(map, i, i+1, 0, j, map[i][j])


def view_distance_range(map, ibeg, iend, jbeg, jend, ref):
    idelta = 1 if ibeg <= iend else -1
    jdelta = 1 if jbeg <= jend else -1
    #print("wdr", ibeg, iend, jbeg, jend, ref)

    dist = 0
    for i in range(ibeg, iend, idelta):
        for j in range(jbeg, jend, jdelta):
            dist += 1
            #print(i, j, ref, map[i][j])
            if ref <= map[i][j]:
                return dist
    return dist


def view_distance_south(map, i, j):
    return view_distance_range(map, i+1, len(map), j, j+1, map[i][j])


def view_distance_north(map, i, j):
    return view_distance_range(map, i-1, -1, j, j+1, map[i][j])


def view_distance_east(map, i, j):
    return view_distance_range(map, i, i+1, j+1, len(map[0]), map[i][j])


def view_distance_west(map, i, j):
    return view_distance_range(map, i, i+1, j-1, -1, map[i][j])


def visible(map, i, j):
    return visible_west(map, i, j) or \
           visible_east(map, i, j) or \
           visible_south(map, i, j) or \
           visible_north(map, i, j)


def scenic_score(map, i, j):
    return view_distance_west(map, i, j) * \
           view_distance_east(map, i, j) * \
           view_distance_north(map, i, j) * \
           view_distance_south(map, i, j)


def scenic_scores(map):
    for i in range(1, len(map)-1):
        for j in range(1, len(map[0])-1):
            yield scenic_score(map, i, j)


if __name__ == '__main__':
    map = [[int(c) for c in l.strip()] for l in open(sys.argv[1])]

    H = len(map)
    W = len(map[0])
    visible_count = 2*(W-1) + 2*(H-1)

    for i in range(1, H-1):
        for j in range(1, W-1):
            if visible(map, i, j):
                visible_count += 1

    print("Part 1:", visible_count)
    print("Part 2:", max(scenic_scores(map)))

