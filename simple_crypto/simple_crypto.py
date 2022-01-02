from random import randint

cipher_text = [125, 131, 120, 126, 146, 138, 140, 135, 74, 137,
               118, 74, 120, 145, 144, 118, 122, 137, 144, 135, 139, 71, 148]

rand_env = 0
for test in range(128):
    for add in range(51):
        if not test+add != cipher_text[0]:
            if (test == ord('f')): # cause first word of flag is 'f'
                print('found key: ' + str(add))
                rand_env = add

result = []
for test in cipher_text:
    print(chr(test - rand_env), end='')
