def find_depth(family, key):
    d = 0
    while family[key]:
        try:
            key = family[key]
            d += 1
        except KeyError:
            break
    return d


n = int(input())
tree = dict()

for _ in range(n - 1):
    child, parent = input().split()
    tree[child] = parent
    if parent not in tree:
        tree[parent] = 0
for name, _ in sorted(tree.items()):
    print(name, find_depth(tree, name))
