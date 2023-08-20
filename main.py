import rotatescreen, time

rotate = rotatescreen

primary = rotate.get_primary_display()

start = primary.current_orientation

for i in range(0, 15):
    final_display = abs((start - i*90) % 360)
    primary.rotate_to(final_display)
    time.sleep(1)
