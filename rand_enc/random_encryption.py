import os
from random import getstate, random, seed, randint, setstate

rands = [[391, 51, 237, 583],
         [306, 627, 887, 596],
         [532, 691, 429, 151],
         [887, 778, 707, 733],
         [645, 176, 993, 751],
         [980, 640, 868, 879],
         [900, 592, 378, 855],
         [244, 571, 415, 110],
         [57, 256, 279, 79],
         [556, 748, 440, 893],
         [312, 860, 44, 965],
         [239, 387, 845, 409],
         [754, 14, 445, 767],
         [522, 424, 35, 287],
         [310, 882, 256, 957],
         [319, 902, 172, 513],
         [114, 665, 768, 287],
         [564, 846, 622, 28],
         [39, 200, 353, 806],
         [900, 972, 874, 506],
         [379, 907, 604, 259],
         [340, 366, 450, 193],
         [796, 989, 826, 694],
         [563, 864, 199, 343],
         [442, 913, 190, 667],
         [615, 815, 73, 551],
         [950, 384, 308, 588],
         [549, 926, 869, 117]]

ct = [619, 433, 83, 775, 408, 142, 602, 291, 84, 566, 435, 330, 808, 503,
      75, 117, 984, 832, 337, 758, 833, 485, 25, 124, 572, 336, 877, 505]


def find_state(num):
    init_state = []
    state = []
    for r in range(100000):
        seed(r)
        if randint(0, 1000) == rands[num][0]:
            init_state.append(getstate())
    for s in init_state:
        setstate(s)
        if randint(0, 1000) == rands[num][1]:
            setstate(getstate())
            if randint(0, 1000) == rands[num][2]:
                setstate(getstate())
                if randint(0, 1000) == rands[num][3]:
                    setstate(getstate())
                    print(chr(randint(0, 1000) ^ ct[num]), end='')
                    return s
        # good_state = False
        # setstate(s)
        # for i in range(1, 3):
        #     setstate(getstate())
        #     if randint(0, 1000) == rands[num][i]:
        #         good_state = True
        #     else:
        #         good_state = False
        #         break
        # if good_state:
        #     return s


for i in range(len(ct)):
    state = find_state(i)
    setstate(state)
