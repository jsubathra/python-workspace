with open('test2.txt', 'w') as f:  # if file not present it will create one
    f.write('test')
    f.seek(0)
    f.write('R')  # will overwrite as position set to 0

# read write image files it should be done with binary file rb,wb
with open('Suba.jpeg', 'rb') as rj:
    with open('Suba1.jpeg', 'wb') as wj:
        wj.write(rj.read())

# or can do in chunks also
