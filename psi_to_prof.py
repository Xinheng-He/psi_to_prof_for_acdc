import sys
def count_freq(aa,line_num,text):
    count_tot = len(text)
    count_u = 0
    for line in  text:
        if line.split()[1][line_num] == aa:
            count_u+=1
    return float(count_u/count_tot)
inp_file = sys.argv[1]
out_file = sys.argv[2]
w = open(out_file,'w')
w.write('POS A C D E F G H I K L M N P Q R S T V W Y -\n')
need_strs = 'A C D E F G H I K L M N P Q R S T V W Y -'.split()
text = open(inp_file).readlines()
for num,str_x in enumerate(text[0].split('pdb')[1].strip()):
    w.write(str(num+1)+' ')
    for strs in need_strs:
        w.write(str(count_freq(strs,num,text))+' ')
    w.write('\n')

