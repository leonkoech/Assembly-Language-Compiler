from __future__ import print_function
import os,sys, shlex, operator

os.system('python3 lexer.py')
 
tk_EOI, tk_Mul, tk_Div, tk_Mod, tk_Add, tk_Sub, tk_Negate, tk_Not, tk_Lss, tk_Leq, tk_Gtr, \
tk_Geq, tk_Eql, tk_Neq, tk_Assign, tk_And, tk_Or, tk_If, tk_Else, tk_While, tk_Print,      \
tk_Putc, tk_Lparen, tk_Rparen, tk_Lbrace, tk_Rbrace, tk_Semi, tk_Comma, tk_Ident,          \
tk_Integer,tk_Rboxbrace,tk_LboxBrace,tk_period, tk_String ,tk_annotation,tk_println,       \
tk_hash,tk_colon,tk_PreDirective,tk_IntegerType,tk_CharacterType, tk_ShortType,tk_LongType,\
tk_FloatType,tk_DoubleType,tk_StringType,tk_BooleanType,tk_ByteType,tk_ArrayType,          \
tk_ClassType,tk_Public,tk_Private,tk_Static,tk_void,tk_import,tk_package ,tk_mainmethod,   \
tk_scanner,tk_new= range(59)

nd_Ident, nd_String, nd_Integer, nd_Sequence, nd_If, nd_Prtc, nd_Prts, nd_Prti, nd_While, \
nd_Assign, nd_Negate, nd_Not, nd_Mul, nd_Div, nd_Mod, nd_Add, nd_Sub, nd_Lss, nd_Leq,     \
nd_Gtr, nd_Geq, nd_Eql, nd_Neq, nd_And, nd_Or, nd_Print = range(26)
 
# must have same order as above
Tokens = [
    ["EOI"             , False, False, False, -1, -1        ],
    ["*"               , False, True,  False, 13, nd_Mul    ],
    ["/"               , False, True,  False, 13, nd_Div    ],
    ["%"               , False, True,  False, 13, nd_Mod    ],
    ["+"               , False, True,  False, 12, nd_Add    ],
    ["-"               , False, True,  False, 12, nd_Sub    ],
    ["-"               , False, False, True,  14, nd_Negate ],
    ["!"               , False, False, True,  14, nd_Not    ],
    ["<"               , False, True,  False, 10, nd_Lss    ],
    ["<="              , False, True,  False, 10, nd_Leq    ],
    [">"               , False, True,  False, 10, nd_Gtr    ],
    [">="              , False, True,  False, 10, nd_Geq    ],
    ["=="              , False, True,  False,  9, nd_Eql    ],
    ["!="              , False, True,  False,  9, nd_Neq    ],
    ["="               , False, False, False, -1, nd_Assign ],
    ["&&"              , False, True,  False,  5, nd_And    ],
    ["||"              , False, True,  False,  4, nd_Or     ],
    ["if"              , False, False, False, -1, nd_If     ],
    ["else"            , False, False, False, -1, -1        ],
    ["while"           , False, False, False, -1, nd_While  ],
    ["print"           , False, False, False, -1, -1        ],
    ["putc"            , False, False, False, -1, -1        ],
    ["("               , False, False, False, -1, -1        ],
    [")"               , False, False, False, -1, -1        ],
    ["{"               , False, False, False, -1, -1        ],
    ["}"               , False, False, False, -1, -1        ],
    [";"               , False, False, False, -1, -1        ],
    [","               , False, False, False, -1, -1        ],
    ["Ident"           , False, False, False, -1, nd_Ident  ],
    ["Integer literal" , False, False, False, -1, nd_Integer],
    ["]"               , False, False, False, -1, -1        ],
    ["["               , False, False, False, -1, -1        ],
    ["."               , False, False, False, -1, -1        ],
    ["String literal"  , False, False, False, -1, nd_String ],
    ["@"               , False, False, False, -1, -1        ],
    ["println"         , False, False, False, -1, -1        ],
    ["#"               , False, False, False, -1, -1        ],
    [":"               , False, False, False, -1, -1        ],
    ["Preprocessor"    , False, False, False, -1, -1        ],
    ['Int type'        , False, False, False, -1, -1        ],
    ['char type'       , False, False, False, -1, -1        ],
    ['short type'      , False, False, False, -1, -1        ],
    ['long type'       , False, False, False, -1, -1        ],
    ['float type'      , False, False, False, -1, -1        ],
    ['double type'     , False, False, False, -1, -1        ],
    ['String type'     , False, False, False, -1, -1        ],
    ['Boolean type'    , False, False, False, -1, -1        ],
    ['Byte type'       , False, False, False, -1, -1        ],
    ['Array type'      , False, False, False, -1, -1        ],
    ['Class type'      , False, False, False, -1, -1        ],
    ['Public dec'      , False, False, False, -1, -1        ],
    ['Private dec'     , False, False, False, -1, -1        ],
    ['Static dec'      , False, False, False, -1, -1        ],
    ['void dec'        , False, False, False, -1, -1        ],
    ['import dec'      , False, False, False, -1, -1        ],
    ['package dec'     , False, False, False, -1, -1        ],
    ['mainmethod dec'  , False, False, False, -1, -1        ],
    ['scanner dec'     , False, False, False, -1, -1        ],
    ['new key'         , False, False, False, -1, -1        ],
    ['Print lit'       , False, False, False, -1, nd_Print  ]
    ]
 
all_syms = {"End_of_input"   : tk_EOI,     "Op_multiply"    : tk_Mul,
            "Op_divide"      : tk_Div,     "Op_mod"         : tk_Mod,
            "Op_add"         : tk_Add,     "Op_subtract"    : tk_Sub,
            "Op_negate"      : tk_Negate,  "Op_not"         : tk_Not,
            "Op_less"        : tk_Lss,     "Op_lessequal"   : tk_Leq,
            "Op_greater"     : tk_Gtr,     "Op_greaterequal": tk_Geq,
            "Op_equal"       : tk_Eql,     "Op_notequal"    : tk_Neq,
            "Op_assign"      : tk_Assign,  "Op_and"         : tk_And,
            "Op_or"          : tk_Or,      "Keyword_if"     : tk_If,
            "Keyword_else"   : tk_Else,    "Keyword_while"  : tk_While,
            "Keyword_input"  : tk_Print,   "Keyword_putc"   : tk_Putc,
            "LeftParen"      : tk_Lparen,  "RightParen"     : tk_Rparen,
            "LeftBrace"      : tk_Lbrace,  "RightBrace"     : tk_Rbrace,
            "Semicolon"      : tk_Semi,    "Comma"          : tk_Comma,
            "Identifier"     : tk_Ident,   "Integer"        : tk_Integer,
            "RightBoxBrace"  : tk_Rboxbrace,"LeftBoxBrace"  : tk_LboxBrace,
            "Period"         : tk_period,  "String"         : tk_String,
            "Annotation"     : tk_annotation,"Keyword_println": tk_println,
            "Hash"           : tk_hash,     "Colon"         : tk_colon,
            "Preprocessor"   : tk_PreDirective,"Type_int"   : tk_IntegerType,
            "Type_char"      : tk_CharacterType,"Type_short": tk_ShortType,
            "Type_long"      : tk_LongType,"Type_float"     : tk_FloatType,
            "Type_double"    : tk_DoubleType,"Type_String"  : tk_StringType,
            "Type_boolean"   : tk_BooleanType,"Type_Byte"   : tk_ByteType,
            "Type_Arrays"    : tk_ArrayType,"Type_Class"    : tk_ClassType,
            'Dec_Public'     : tk_Public,"Dec_private"      : tk_Private,
            "Dec_static"     : tk_Static,'Dec_void'         : tk_void,
            'Dec_import'     : tk_import,'Dec_package'      : tk_package,
            'Dec_mainmethod' : tk_mainmethod,"Type_Scanner"  : tk_scanner,
            'Type_new'       : tk_new,}
 
Display_nodes = ["Identifier","String", "Integer", "Sequence", "If", "Prtc", "Prts",
    "Prti", "While", "Assign", "Negate", "Not", "Multiply", "Divide", "Mod", "Add",
    "Subtract", "Less", "LessEqual", "Greater", "GreaterEqual", "Equal", "NotEqual",
    "And", "Or","Print"]

datatypes={tk_IntegerType,tk_CharacterType,tk_ShortType,tk_LongType,tk_DoubleType,
    tk_StringType,tk_BooleanType,tk_ByteType,tk_ArrayType}
TK_NAME         = 0
TK_RIGHT_ASSOC  = 1
TK_IS_BINARY    = 2
TK_IS_UNARY     = 3
TK_PRECEDENCE   = 4
TK_NODE         = 5
 
input_file = None
err_line   = None
err_col    = None
tok        = None
tok_text   = None
 
#*** show error and exit
def error(msg):
    print("(%d, %d) %s" % (int(err_line), int(err_col), msg))
    exit(1)
 
#***
def gettok():
    global err_line, err_col, tok, tok_text, tok_other
    line = input_file.readline()
    # line = line[:-1]
    if len(line) == 0:
        print(line)
        error("empty line")
 
    line_list = shlex.split(line, False, False)
    # line col Ident var_name
    # 0    1   2     3
 
    err_line = line_list[0]
    err_col  = line_list[1]
    tok_text = line_list[2]
 
    tok = all_syms.get(tok_text)
    if tok == None:
        error("Unknown token %s" % (tok_text))
 
    tok_other = None
    if tok in [tk_Integer, tk_Ident, tk_String]:
        tok_other = line_list[3]
 
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
def expect(msg, s):
    if tok == s:
        gettok()
        return
    error("%s: Expecting '%s', found '%s'" % (msg, Tokens[s][TK_NAME], Tokens[tok][TK_NAME]))
 
#***
def expr(p):
    x = None
 
    if tok == tk_Lparen:
        x = paren_expr()
    elif tok in [tk_Sub, tk_Add]:
        op = (tk_Negate if tok == tk_Sub else tk_Add)
        gettok()
        node = expr(Tokens[tk_Negate][TK_PRECEDENCE])
        x = (make_node(nd_Negate, node) if op == tk_Negate else node)
    elif tok == tk_Not:
        gettok()
        x = make_node(nd_Not, expr(Tokens[tk_Not][TK_PRECEDENCE]))
    elif tok == tk_Ident:
        x = make_leaf(nd_Ident, tok_other)
        gettok()
    elif tok == tk_Integer:
        x = make_leaf(nd_Integer, tok_other)
        gettok()
    elif tok== tk_scanner:
        gettok()
        if tok==tk_Print:
            gettok()
            if tok == tk_Rparen:
                gettok()
    elif tok==tk_Rparen:
       pass
    else:
        error("Expecting a primary, found: %s" % (Tokens[tok][TK_NAME]))
 
    while Tokens[tok][TK_IS_BINARY] and Tokens[tok][TK_PRECEDENCE] >= p:
        op = tok
        gettok()
        q = Tokens[op][TK_PRECEDENCE]
        if not Tokens[op][TK_RIGHT_ASSOC]:
            q += 1
 
        node = expr(q)
        x = make_node(Tokens[op][TK_NODE], x, node)
 
    return x
 
#***
def paren_expr():
    expect("paren_expr", tk_Lparen)
    node = expr(0)
    expect("paren_expr", tk_Rparen)
    return node
 
#***
def stmt():
    t = None
 
    if tok == tk_If:
        gettok()
        e = paren_expr()
        s = stmt()
        s2 = None
        if tok == tk_Else:
            gettok()
            s2 = stmt()
        t = make_node(nd_If, e, make_node(nd_If, s, s2))
    elif tok == tk_Putc:
        gettok()
        e = paren_expr()
        t = make_node(nd_Prtc, e)
        expect("Putc", tk_Semi)
    elif tok==tk_println:
        gettok()
        expect("Print", tk_Lparen)
        while True:
            if tok == tk_String:
                e = make_node(nd_Prts, make_leaf(nd_String, tok_other))
                gettok()
                print(tok)
            if tok==tk_Add:
                for g in range(0,20):
                    if tok == tk_Rparen:
                        e = make_node(nd_Prti, expr(0))
                    else:
                        gettok()
                gettok()
                print(tok)
            else:
                e = make_node(nd_Prti, expr(0))
            t = make_node(nd_Sequence, t, e)
            if tok != tk_Comma or tok!=tk_Add :
                break
            gettok()
         # expect("Print", tk_Rparen)
        print(tok)
        expect("Print", tk_Semi)
    
    elif tok == tk_Semi:
        gettok()
    elif tok == tk_Ident:
        v = make_leaf(nd_Ident, tok_other)
        gettok()
        if tok==tk_Assign:
        # bc it's java we shouldex
            expect("assign", tk_Assign)
            e = expr(0)
            t = make_node(nd_Assign, v, e)
            expect("assign", tk_Semi)
        elif tok==tk_Semi:
            expect("semi", tk_Semi)
            e = expr(0)
            t = make_node(nd_Assign, v, e)
           
        # if the next character is not assignment opoerator
       
    elif tok == tk_While:
        gettok()
        e = paren_expr()
        s = stmt()
        t = make_node(nd_While, e, s)
    elif tok == tk_Lbrace:
        gettok()
        while tok != tk_Rbrace and tok != tk_EOI:
            t = make_node(nd_Sequence, t, stmt())
        expect("Lbrace", tk_Rbrace)
    # elif tok== tk_Rbrace:
        # gettok()
        # while True:
        #     if tok==tk_Rbrace:
        #         gettok()
        #         while tok != tk_Rbrace and tok != tk_EOI:
        #             t = make_node(nd_Sequence, t, stmt())
        #             expect("Lbrace", tk_Rbrace)
        #     elif tok==tk_EOI:
        #         pass
        #     else:
        #         gettok()
        # while False:

        #     pass
    elif tok == tk_LboxBrace:
        gettok()
        while tok != tk_Rboxbrace and tok != tk_EOI:
            t = make_node(nd_Sequence, t, stmt())
        expect("LboxBrace", tk_Rboxbrace)
    # if start is a preprocessor directive
    elif tok == tk_PreDirective:
        # ignore the preprocessor
        gettok()
    elif tok==tk_package or tok==tk_mainmethod or tok==tk_import or tok==tk_annotation:
        gettok()
    elif tok == tk_scanner:
        gettok()
        if tok == tk_Ident:
            v = make_leaf(nd_Ident, tok_other)
            gettok()
            expect("assign", tk_Assign)
            e = expr(0)
            t = make_node(nd_Assign, v, e)
            expect("assign", tk_Semi)
        elif tok==tk_Lbrace:
            gettok()
            while tok != tk_Rbrace and tok != tk_EOI:
                t = make_node(nd_Sequence, t, stmt())
            expect("Lbrace", tk_Rbrace)
        elif tok==tk_Rparen:
            gettok()
    elif tok==tk_import:
        gettok()
    elif tok==tk_Print:
        gettok()
        if tok == tk_Rparen:
            gettok()
            if tok == tk_Semi:
                gettok()
        else:
            print('problem here')

    elif tok==tk_ClassType:
        gettok()
        # after class expect an identifier. Class name
        expect("ident",tk_Ident)
    elif tok==tk_new:
        gettok()
    elif tok == tk_EOI:
        # gettok()
        pass
    elif tok==tok==tk_IntegerType or tok==tk_CharacterType or tok==tk_ShortType or tok==tk_LongType or tok==tk_DoubleType or \
tok==tk_StringType or tok==tk_BooleanType or tok==tk_ByteType or tok==tk_ArrayType:
        gettok()
    else:
       error("Expecting start of statement, found: %s" % (Tokens[tok][TK_NAME]))
 
    return t
 
#***
def parse():
    t = None
    gettok()
    while True:
        t = make_node(nd_Sequence, t, stmt())
        if tok == tk_EOI or t == None:
            break
    return t

analyse=[]
def prt_ast(t):
    if t == None:
        print(";")
        analyse.append([';'])
    else:
        print("%-14s" % (Display_nodes[t.node_type]), end='')
        if t.node_type in [nd_Ident, nd_Integer]:
            print("%s" % (t.value))
            analyse.append([Display_nodes[t.node_type],t.value])
        elif t.node_type == nd_String:
            print("%s" %(t.value))
            analyse.append([Display_nodes[t.node_type],t.value])
        else:
            print("")
            analyse.append([Display_nodes[t.node_type],''])
            prt_ast(t.left)
            prt_ast(t.right)
 
#*** main driver
try:
    input_file = open('lexeroutput.txt', "r", 4096)
except IOError as e:
    error("Can't open lexeroutput.txt")
t = parse()
prt_ast(t)
print('writing to analyseroutput.txt...............................')
def arrtostr(ite):
    strr=''
    for b in ite:
        strr+=str(b)+'   '
    return strr
with  open('analyseroutput.txt', 'w+') as doc:
    for line in analyse:
        doc.write(arrtostr(line)+'\n')
    doc.close()
print('sucessfully written to analyseroutput.txt ✔️\n')
print('code generator is running............................')
print('code generator output:\n')