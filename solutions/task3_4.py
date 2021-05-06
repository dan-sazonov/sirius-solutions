a, b, d = map(int, input().split())
school_to_club = abs(a - b)
dist_1, dist_2 = -1, 2

if school_to_club > 1:
    dist_1 = school_to_club // 2
    dist_2 = school_to_club - dist_1

point_1, point_2 = min(a, b) + dist_1, min(a, b) + dist_2
tmp_1, tmp_2 = point_1 % d, point_2 % d

dist_to_ice_1 = min(tmp_1, d - tmp_1)
dist_to_ice_2 = min(tmp_2, d - tmp_2)

if dist_to_ice_1 <= dist_to_ice_2:
    print(point_1, dist_to_ice_1)
else:
    print(point_2, dist_to_ice_2)
