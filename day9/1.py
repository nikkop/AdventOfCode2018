with open('input.txt') as input:
    n_players, last_marble = [int(num) for num in input.read().split(' ') if num.isdigit()]

    players = dict.fromkeys([p for p in range(1, n_players+1)], 0)

    marbles = list([0])
    curr_marble = marbles[0]
 
    for i in range(1, (last_marble)+1):
        marble = i
       
        curr_index = marbles.index(curr_marble)
        if marble % 23 is 0:
            marble_index = (curr_index - 7) % len(marbles)
            marble_to_remove = marbles.pop(marble_index)
            players[i%len(players)+1] += marble + marble_to_remove
            curr_marble = marbles[marble_index]
        else:
            next_index = (curr_index + 2) % len(marbles)
            curr_marble = marble
            marbles.insert(next_index, curr_marble)
        
    result = max(players.values())
    print(result)