
def first():
    global f_n, s_n, id, example, right, left
    while left > -1 and example[left].isdigit() or example[left] == '.':
        f_n += example[left]
        example = example[:left] + example[left + 1:]
        left -= 1
        right -= 1
    f_n = f_n[::-1]
    f_n = float(f_n)
    print(f_n)
    print(example)

def second():
    global f_n, s_n, id, example, right, left
    while example[right].isdigit() or example[right] == '.':
        s_n += example[right]
        example = example[:right] + example[right+1:]
        if(right >= len(example)):
            break
    s_n = float(s_n)
    print(s_n)
    print(example)

def multy():
     global f_n, s_n, example , n_n
     n_n = f_n + s_n
     n_n = str(n_n)
     change = example.find('+')
     example = example[:change] + n_n + example[change + 1:]
     print(example)


id = 0
example = '6.0-40.0-562.5-350.0+5.0'
while(True):
    id = example.find('+')
    if(id == -1):
        break
    f_n = ''
    s_n = ''
    right = id + 1
    left = id - 1
    first()
    second()
    multy()



