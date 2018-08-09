n = int(raw_input('n please?') or 30)
character = raw_input('char please?') or '*'

blank_line = ['   ' for _ in range(n)]
blank_canvas = [list(blank_line) for _ in range(n)]

def fill_canvas(coords):
    blank_canvas[coords[0]][coords[1]] = ' {} '.format(character)

row = n/2
col = n/2
fill_canvas((row, col))
n = 0
direction = 'down'
finished = False
while not finished:
    n+=1
    for _ in range(n):
        if direction == 'down':
            row += 1
        elif direction == 'right':
            col += 1
        elif direction == 'up':
            row -= 1
        elif direction == 'left':
            col -= 1
        try:
            fill_canvas((row, col))
        except IndexError:
            finished = True
    direction = { 'down': 'right', 'right': 'up', 'up': 'left', 'left': 'down' }[direction]

for row in blank_canvas:
    print ''.join(row)
