from __future__ import print_function
import os,sys, struct, shlex, operator


os.system('python3 syntaxanalyser.py')
print('code generator is running............................')
nd_Ident, nd_String, nd_Integer, nd_Sequence, nd_If, nd_Prtc, nd_Prts, nd_Prti, nd_While, \
nd_Assign, nd_Negate, nd_Not, nd_Mul, nd_Div, nd_Mod, nd_Add, nd_Sub, nd_Lss, nd_Leq,     \
nd_Gtr, nd_Geq, nd_Eql, nd_Neq, nd_And, nd_Or,nd_Adas,nd_For,nd_Return= range(28)
 
all_syms = {
    "Identifier"  : nd_Ident,    "String"      : nd_String,
    "Integer"     : nd_Integer,  "Sequence"    : nd_Sequence,
    "If"          : nd_If,       "Prtc"        : nd_Prtc,
    "Prts"        : nd_Prts,     "Prti"        : nd_Prti,
    "While"       : nd_While,    "Assign"      : nd_Assign,
    "Negate"      : nd_Negate,   "Not"         : nd_Not,
    "Multiply"    : nd_Mul,      "Divide"      : nd_Div,
    "Mod"         : nd_Mod,      "Add"         : nd_Add,
    "Subtract"    : nd_Sub,      "Less"        : nd_Lss,
    "LessEqual"   : nd_Leq,      "Greater"     : nd_Gtr,
    "GreaterEqual": nd_Geq,      "Equal"       : nd_Eql,
    "NotEqual"    : nd_Neq,      "And"         : nd_And,
    "Or"          : nd_Or,       "AddAssign"   : nd_Adas,
    "For"         : nd_For,      "Return"      : nd_Return}
 
FETCH, STORE, PUSH, ADD, SUB, MUL, DIV, MOD, LT, GT, LE, GE, EQ, NE, AND, OR, NEG, NOT, \
JMP, JZ, PRTC, PRTS, PRTI, HALT,AA,RTRN = range(26)
 
operators = {nd_Lss: LT, nd_Gtr: GT, nd_Leq: LE, nd_Geq: GE, nd_Eql: EQ, nd_Neq: NE,
    nd_And: AND, nd_Or: OR, nd_Sub: SUB, nd_Add: ADD, nd_Div: DIV, nd_Mul: MUL, nd_Mod: MOD,nd_Adas:AA,nd_Return:RTRN}
 
unary_operators = {nd_Negate: NEG, nd_Not: NOT}
 
input_file  = None
code        = bytearray()
string_pool = {}
globals     = {}
string_n    = 0
globals_n   = 0
word_size   = 4
 
#*** show error and exit
def error(msg):
    print("%s" % (msg))
    exit(1)
 
def int_to_bytes(val):
    return struct.pack("<i", val)
 
def bytes_to_int(bstr):
    return struct.unpack("<i", bstr)
 
class Node:
    def __init__(self, node_type, left = None, right = None, value = None):
        self.node_type  = node_type
        self.left  = left
        self.right = right
        self.value = value
 
#***
def make_node(oper, left, right = None):
    return Node(oper, left, right)
 
#***
def make_leaf(oper, n):
    return Node(oper, value = n)
 
#***
def emit_byte(x):
    code.append(x)
 
#***
def emit_word(x):
    s = int_to_bytes(x)
    for x in s:
        code.append(x)
 
def emit_word_at(at, n):
    code[at:at+word_size] = int_to_bytes(n)
 
def hole():
    t = len(code)
    emit_word(0)
    return t
 
#***
def fetch_var_offset(name):
    global globals_n
 
    n = globals.get(name, None)
    if n == None:
        globals[name] = globals_n
        n = globals_n
        globals_n += 1
    return n
 
#***
def fetch_string_offset(the_string):
    global string_n
 
    n = string_pool.get(the_string, None)
    if n == None:
        string_pool[the_string] = string_n
        n = string_n
        string_n += 1
    return n
 
#***
def code_gen(x):
    if x == None: return
    elif x.node_type == nd_Ident:
        emit_byte(FETCH)
        n = fetch_var_offset(x.value)
        emit_word(n)
    elif x.node_type == nd_Integer:
        emit_byte(PUSH)
        emit_word(x.value)
    elif x.node_type == nd_String:
        emit_byte(PUSH)
        n = fetch_string_offset(x.value)
        emit_word(n)
    elif x.node_type == nd_Assign:
        n = fetch_var_offset(x.left.value)
        code_gen(x.right)
        emit_byte(STORE)
        emit_word(n)
    elif x.node_type == nd_If:
        code_gen(x.left)              # expr
        emit_byte(JZ)                 # if false, jump
        p1 = hole()                   # make room for jump dest
        code_gen(x.right.left)        # if true statements
        if (x.right.right != None):
            emit_byte(JMP)            # jump over else statements
            p2 = hole()
        emit_word_at(p1, len(code) - p1)
        if (x.right.right != None):
            code_gen(x.right.right)   # else statements
            emit_word_at(p2, len(code) - p2)
    elif x.node_type == nd_While:
        p1 = len(code)
        code_gen(x.left)
        emit_byte(JZ)
        p2 = hole()
        code_gen(x.right)
        emit_byte(JMP)                       # jump back to the top
        emit_word(p1 - len(code))
        emit_word_at(p2, len(code) - p2)
    elif x.node_type== nd_For:
        p1 = len(code)
        code_gen(x.left)
        emit_byte(JZ)
        p2 = hole()
        code_gen(x.right)
        emit_byte(JMP)                       # jump back to the top
        emit_word(p1 - len(code))
        emit_word_at(p2, len(code) - p2)
    elif x.node_type == nd_Return:
        code_gen(x.left)
        emit_byte(RTRN)
    elif x.node_type == nd_Sequence:
        code_gen(x.left)
        code_gen(x.right)
    elif x.node_type == nd_Prtc:
        code_gen(x.left)
        emit_byte(PRTC)
    elif x.node_type == nd_Prti:
        code_gen(x.left)
        emit_byte(PRTI)
    elif x.node_type == nd_Prts:
        code_gen(x.left)
        emit_byte(PRTS)
    elif x.node_type in operators:
        code_gen(x.left)
        code_gen(x.right)
        emit_byte(operators[x.node_type])
    elif x.node_type in unary_operators:
        code_gen(x.left)
        emit_byte(unary_operators[x.node_type])
    else:
        error("error in code generator - found %d, expecting operator" % (x.node_type))
 
#***
def code_finish():
    emit_byte(HALT)
 
#***
codegenarr=[]
def list_code():
    print("Datasize: %d Strings: %d" % (len(globals), len(string_pool)))
    codegenarr.append(['Datasize:',len(globals),'Strings:',len(string_pool)])
    for k in sorted(string_pool, key=string_pool.get):
        print(k)
        codegenarr.append([k])
    pc = 0
    while pc < len(code):
        print("%4d " % (pc), end='')
        op = code[pc]
        pc += 1
        if op == FETCH:
            x = bytes_to_int(code[pc:pc+word_size])[0]
            print("fetch [%d]" % (x))
            codegenarr.append([pc-1,"fetch" ,[x]])
            pc += word_size
        elif op == STORE:
            x = bytes_to_int(code[pc:pc+word_size])[0]
            print("store [%d]" % (x))
            if pc-1<10:
                codegenarr.append([pc-1," store" ,[x]])
            else:
                codegenarr.append([pc-1,"store" ,[x]])
            
            pc += word_size
        elif op == PUSH:
            x = bytes_to_int(code[pc:pc+word_size])[0]
            print("push  %d" % (x))
            if pc-1<10:
                codegenarr.append([pc-1," push ",x])
            else:
                codegenarr.append([pc-1,"push ",x])
            pc += word_size
        elif op == ADD:   
            print("add")
            codegenarr.append([pc-1,'add'])
        elif op == SUB:   
            print("sub")
            codegenarr.append([pc-1,'sub'])
        elif op == MUL:   
            print("mul")
            codegenarr.append([pc-1,'mul'])
        elif op == DIV:   
            print("div")
            codegenarr.append([pc-1,'div'])
        elif op == MOD:   
            print("mod")
            codegenarr.append([pc-1,'mod'])
        elif op == LT:    
            print("lt")
            codegenarr.append([pc-1,'lt'])
        elif op == GT:    
            print("gt")
            codegenarr.append([pc-1,'gt'])
        elif op == LE:    
            print("le")
            codegenarr.append([pc-1,'le'])
        elif op == GE:    
            print("ge")
            codegenarr.append([pc-1,'ge'])
        elif op == EQ:    
            print("eq")
            codegenarr.append([pc-1,'eq'])
        elif op == NE:    
            print("ne")
            codegenarr.append([pc-1,'ne'])
        elif op == AND:   
            print("and")
            codegenarr.append([pc-1,'and'])
        elif op == OR:    
            print("or")
            codegenarr.append([pc-1,'or'])
        elif op == NEG:   
            print("neg")
            codegenarr.append([pc-1,'neg'])
        elif op == NOT:   
            print("not")
            codegenarr.append([pc-1,'not'])
        elif op == JMP:
            x = bytes_to_int(code[pc:pc+word_size])[0]
            print("jmp    (%d) %d" % (x, pc + x))
            codegenarr.append([pc-1,'jmp  ',(x), pc + x])
            pc += word_size
        elif op == JZ:
            x = bytes_to_int(code[pc:pc+word_size])[0]
            print("jz     (%d) %d" % (x, pc + x))
            codegenarr.append([pc-1,'jz   ',(x), pc + x])
            pc += word_size
        elif op == PRTC:  
            print("prtc")
            codegenarr.append([pc-1,'prtc'])
        elif op == PRTI:  
            print("prti")
            codegenarr.append([pc-1,'prti'])
        elif op == PRTS:  
            print("prts")
            codegenarr.append([pc-1,'prts'])
        elif op == HALT:  
            print("halt")
            codegenarr.append([pc-1,'halt'])
        elif op == AA:    
            print("aa")
            codegenarr.append([pc-1,'ne'])
        else: 
            error("list_code: Unknown opcode"+str(op))
 
def load_ast():
    line = input_file.readline()
    line_list = shlex.split(line, False, False)
 
    text = line_list[0]
    if text == ";":
        return None
    node_type = all_syms[text]
 
    if len(line_list) > 1:
        value = line_list[1]
        if value.isdigit():
            value = int(value)
        return make_leaf(node_type, value)
 
    left = load_ast()
    right = load_ast()
    return make_node(node_type, left, right)
 
#*** main driver

try:
    input_file = open('analyseroutput.txt', "r", 4096)
except IOError as e:
    error("Can't open analyseroutput.txt")
 
n = load_ast()
code_gen(n)
code_finish()
list_code()
def arrtostr(ite):
    strr=''
    for b in ite:
        strr+=str(b)+'   '
    return strr
print(codegenarr)
print('\nwriting to codeoutput.txt...............................')
with  open('codeoutput.txt', 'w+') as doc:
    for line in codegenarr:
        doc.write(arrtostr(line)+'\n')
    doc.close()
print('code generator output sucessfully written to codeoutput.txt ✔️')