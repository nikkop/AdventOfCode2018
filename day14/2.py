with open('input.txt') as input:
    recipe_val = [int(x) for x in input.read()]
    recipe_l = 10

    elves = [{'c': 3, 'i': 0}, {'c': 7, 'i': 1}]
    scores = [e['c'] for e in elves]

    should_continue = True
    while should_continue:
        score = [int(x) for x in str(sum([e['c'] for e in elves]))]
        for s in score:
            scores.append(s)
            last_recipes = scores[-len(recipe_val):]
            print(last_recipes)
            if last_recipes == recipe_val:
                should_continue = False
                break

        for e in elves:
            e_i = (e['c'] + e['i'] + 1) % len(scores)
            e['c'] = scores[e_i]
            e['i'] = e_i

    recipes = scores[:len(scores)-len(recipe_val)]
    result = len(recipes)
    print(result)