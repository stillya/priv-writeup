string_code_list = ['cat flag.txt']
charset = "!#%&()*+,-/:;<=>?@[]^_{|}~"

for string_code in string_code_list:
    obfuscate_str_final = ""

    for i in string_code:
        is_found_obfs = False
        for j in charset:
            for k in charset:
                if ord(j)^ord(k) == ord(i):
                    obfuscate_str_final += ".('%s'^'%s')" % (j,k)
                    is_found_obfs = True
                if is_found_obfs:
                    break
            if is_found_obfs:
                break
        if not is_found_obfs:
            obfuscate_str_final += ".'%s'" % i
    print("%s = %s" % (string_code, obfuscate_str_final[1:]))


# ('#!'^'@@').(')['^']{').('&,'^'@@').('!:'^'@]').'.'.(')#'^'][').(')'^']')    -  cat flag.txt

# (')%!:&),%'^'[@@^@@@@').'('.('[&,!:'^'|@@@]').'.'.(')#)'^'][]').('['^'|').')'  - readfile('flag.txt')