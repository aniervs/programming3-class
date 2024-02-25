games = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
         'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
         'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
         'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
         'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
# f = open('task2', 'r')
# games = []
# line = f.readline()
# while line != '':
#     games.append(line)
#     line = f.readline()

max_r = 12
max_g = 13
max_b = 14
games_s = 0
k = 0
for game in games:
    if k < 9:
        game_num = int(game[5])
    elif k == 99:
        game_num = int(game[5:8])
    else:
        game_num = int(game[5:7])
    game_inf = game.split(': ')[1]
    sets = game_inf.split('; ')
    game_good = True
    for set_inf in sets:
        cubes = set_inf.split(', ')
        for i in range(len(cubes)):
            n, color = cubes[i].split(' ')
            if color == 'red':
                if int(n) > max_r:
                    game_good = False
            elif color == 'green':
                if int(n) > max_g:
                    game_good = False
            else:
                if int(n) > max_b:
                    game_good = False
    if game_good:
        print(game)
        games_s += game_num
    k += 1
print(games_s)