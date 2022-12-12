with open("C:\\Users\\nicoh\\advent_of_code_2022\\day_10\\input.txt") as f: 
    lines = f.readlines()

def determine_pixel(X, middle_pixel):
    if (X == middle_pixel) or (X == middle_pixel-1) or (X == middle_pixel + 1):
        return '#'
    else:
        return '.'

cycle = 0
X = 1
crt_screen = {}
current_crt_line = 0
for line in lines:
    line = line.rstrip()
    if line == "noop":
        cycle += 1
        if (cycle % 40) == 1:
            current_crt_line += 1
            crt_screen[current_crt_line] = '.' * 40
        rel_pos = ((cycle - 1) % 40)
        pixel_art = determine_pixel(X, rel_pos)
        crt_screen[current_crt_line] = crt_screen[current_crt_line][:rel_pos] + pixel_art + crt_screen[current_crt_line][rel_pos+1:]

    else:
        cycle += 1
        if (cycle % 40) == 1:
            current_crt_line += 1
            crt_screen[current_crt_line] = '.' * 40
        rel_pos = ((cycle - 1) % 40)
        pixel_art = determine_pixel(X, rel_pos)
        crt_screen[current_crt_line] = crt_screen[current_crt_line][:rel_pos] + pixel_art + crt_screen[current_crt_line][rel_pos+1:]
        
        cycle += 1
        if (cycle % 40) == 1:
            current_crt_line += 1
            crt_screen[current_crt_line] = '.' * 40
        rel_pos = ((cycle - 1) % 40)
        pixel_art = determine_pixel(X, rel_pos)
        crt_screen[current_crt_line] = crt_screen[current_crt_line][:rel_pos] + pixel_art + crt_screen[current_crt_line][rel_pos+1:]
        
        split_line = line.split(' ')
        V = int(split_line[1])

        X += V
    
for line in crt_screen:
    print(crt_screen[line])