def extract_meta(nodes):
    values = 0

    n_c = nodes[0]
    n_m = nodes[1]

    meta_end_index = 2
    children = list()

    if n_c is 0:
        meta_values = nodes[meta_end_index:meta_end_index+n_m]
        values += sum(meta_values)
    else:
        for i in range(n_c):
            child = nodes[meta_end_index:]
            children.append(child)
            index = extract_meta(child)[0]
            meta_end_index += index

    for m in nodes[meta_end_index:meta_end_index+n_m]:
        if m <= n_c and m <= len(children):
            child = children[m-1]
            vals = extract_meta(child)[1]
            values += vals

    return (meta_end_index + n_m, values)

with open('input.txt') as input:
    nodes = list(map(int, input.readline().split(' ')))
    result = extract_meta(nodes)[1]
    print(result)



