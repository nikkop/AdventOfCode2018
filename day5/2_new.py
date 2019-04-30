with open('input.txt') as input:
    chars = [char for char in input.read()]
    pairs = set([(char.upper(), char.lower()) for char in chars])

    best_nums = float("Inf") 

    for lower, upper in pairs:
        without_pair = [char for char in chars if char != lower and char != upper]
        should_continue = True

        while should_continue:
            for i in range(len(without_pair)-1):
                c_curr = without_pair[i]
                c_next = without_pair[i+1]
                if c_curr.lower() == c_next.lower() and c_curr != c_next:
                    del without_pair[i]
                    del without_pair[i]
                    break
            else:
                should_continue = False
        
        if len(without_pair) < best_nums:
            best_nums = len(without_pair)
        
    print(best_nums)
