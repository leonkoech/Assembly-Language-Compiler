pt=[['hello','you are'],['hfsdgfjs'],['dsfsdf'],['rtyry'],['ewwewe'],['tyutyuytu'],['eresre'],['sfff'],['you aer']]
def arrtostr(ite):
    strr=''
    for b in ite:
        strr+=str(b)+'   '
    return strr
with  open('test.txt', 'w+') as doc:
    for item in pt[:-1]:
        doc.write(arrtostr(item)+'\n')
        # doc.close()
    else:
        doc.write(arrtostr(pt[-1]))
