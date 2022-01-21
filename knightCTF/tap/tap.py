

ALPLHABET = [[1,2,3,4,5,6], 
            [1,'A', 'B', 'K', 'D', 'E', 'F'],
            [2,'G', 'H', 'I', 'J', 'L', 'M'],
            [3,'N', 'O', 'P', 'Q', 'R', 'S'],
            [4,'U', 'T', 'V', 'W', 'X', 'Z']]

knock = open('knock.txt', 'r').read()

knock_list = knock.split(' ')
# print(len(knock_list))

for fir, sec in zip(knock_list[0::2], knock_list[1::2]):
    print(ALPLHABET[len(fir)][len(sec)], end='')