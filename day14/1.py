with open('input.txt') as input:
    n_recipes = int(input.read())
    recipe_l = 10

    elves = [{'c': 3, 'i': 0}, {'c': 7, 'i': 1}]
    scores = [e['c'] for e in elves]

    while len(scores) <= n_recipes + recipe_l:
        score = [int(x) for x in str(sum([e['c'] for e in elves]))]
        for s in score:
            scores.append(s)
        
        for e in elves:
            e_i = (e['c'] + e['i'] + 1) % len(scores)
            e['c'] = scores[e_i]
            e['i'] = e_i

    recipes = scores[n_recipes:n_recipes+recipe_l]
    result = "".join(str(x) for x in recipes)

    print(result)
