from collections import deque

with open('input.txt') as input:
  n_players, last_marble = [int(num) for num in input.read().split(' ') if num.isdigit()]

  players = dict.fromkeys([p for p in range(n_players)], 0)

  marbles = deque([0])
  for i in range(1, (last_marble * 100)+1):
    if i % 23 is 0:
      marbles.rotate(7)
      players[i%len(players)] += i + marbles.pop()
      marbles.rotate(-1)
    else:
      marbles.rotate(-1)
      marbles.append(i)
  
  result = max(players.values())
  print(result)