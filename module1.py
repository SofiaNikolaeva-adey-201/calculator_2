

f_n = ''
s_n = ''
id = 0
example = '10+12/3-46.5+9/2-50*7'
id = example.find('*')
right = id + 1
left = id - 1


#def is_multy():
    #global f_n, s_n, id, example, right, left, n_n
    #while "*" in example:
        #id = example.find('*')
        #right = id + 1
        #left = id - 1
        #first()
        #second()
        #multy()
    #return example





def first():
    global f_n, s_n, id, example, right, left
    while example[left].isdigit() or example[left] == '.':
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
    while example[right].isdigit():
        s_n += example[right]
        example = example[:right] + example[right + 1:]
    s_n = float(s_n)
    print(s_n)
    print(example)

def multy():
     global f_n, s_n, example , n_n
     n_n = f_n * s_n
     n_n = str(n_n)
     change = example.find('*')
     example = example[:change] + n_n + example[change + 1:]
     print(example)

first()
second()
multy()
