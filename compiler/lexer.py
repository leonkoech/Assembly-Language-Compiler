from __future__ import print_function
import sys

# following two must remain in the same order
 
tk_EOI, tk_Mul, tk_Div, tk_Mod, tk_Add, tk_Sub, tk_Negate, tk_Not, tk_Lss, tk_Leq, tk_Gtr, \
tk_Geq, tk_Eq, tk_Neq, tk_Assign, tk_And, tk_Or, tk_If, tk_Else, tk_While, tk_Print,       \
tk_Putc, tk_Lparen, tk_Rparen, tk_Lbrace, tk_Rbrace, tk_Semi, tk_Comma, tk_Ident,          \
tk_Integer,tk_Rboxbrace,tk_LboxBrace,tk_period, tk_String ,tk_annotation,tk_println,       \
tk_hash,tk_colon,tk_PreDirective,tk_IntegerType,tk_CharacterType, tk_ShortType,tk_LongType,\
tk_FloatType,tk_DoubleType,tk_StringType,tk_BooleanType,tk_ByteType,tk_ArrayType,          \
tk_ClassType,tk_Public,tk_Private,tk_Static,tk_void,tk_import,tk_package ,tk_mainmethod,    \
tk_scanner,tk_new= range(59)
 
all_syms = ["End_of_input", "Op_multiply", "Op_divide", "Op_mod", "Op_add", "Op_subtract",
    "Op_negate", "Op_not", "Op_less", "Op_lessequal", "Op_greater", "Op_greaterequal",
    "Op_equal", "Op_notequal", "Op_assign", "Op_and", "Op_or", "Keyword_if",
    "Keyword_else", "Keyword_while", "Keyword_input", "Keyword_putc", "LeftParen",
    "RightParen", "LeftBrace", "RightBrace", "Semicolon", "Comma", "Identifier",
    "Integer","RightBoxBrace","LeftBoxBrace","Period", "String","Annotation","Keyword_println",
    "Hash","Colon","Preprocessor","Type_int","Type_char","Type_short","Type_long","Type_float","Type_double",
    "Type_String","Type_boolean","Type_Byte","Type_Arrays","Type_Class",'Dec_Public',"Dec_private","Dec_static",
    'Dec_void','Dec_import','Dec_package','Dec_mainmethod','Type_Scanner','Type_new']
 
# single character only symbols
symbols = { '{': tk_Lbrace, '}': tk_Rbrace, '(': tk_Lparen, ')': tk_Rparen, '+': tk_Add, '-': tk_Sub,
    '*': tk_Mul, '%': tk_Mod, ';': tk_Semi, ',': tk_Comma ,']':tk_Rboxbrace,'[':tk_LboxBrace,'.':tk_period,'@':tk_annotation,
    '#':tk_hash,':':tk_colon}
 
key_words = {'if': tk_If, 'else': tk_Else, 'in': tk_Print, 'putc': tk_Putc, 'while': tk_While,'println':tk_println}

data_types={'int':tk_IntegerType,'char':tk_CharacterType,'short':tk_ShortType,'long':tk_LongType,'float':tk_LongType,'double':tk_DoubleType,
    'String':tk_StringType,'boolean':tk_BooleanType,'byte':tk_ByteType,'Array':tk_ArrayType,'class':tk_ClassType,'Scanner':tk_scanner,'new':tk_new}

decalrative={'public':tk_Public,'Private':tk_Private,'static':tk_Static,'void':tk_void,'import':tk_import,'package':tk_package}

the_ch = " "    # dummy first char - but it must be a space
the_col = 0
the_line = 1
input_file = None
 
#*** show error and exit
def error(line, col, msg):
    print(line, col, msg)
    exit(1)
 
#*** get the next character from the input
def next_ch():
    global the_ch, the_col, the_line
 
    the_ch = input_file.read(1)
    the_col += 1
    if the_ch == '\n':
        the_line += 1
        the_col = 0
    return the_ch
 
#*** 'x' - character constants
def char_lit(err_line, err_col):
    n = ord(next_ch())              # skip opening quote
    if the_ch == '\'':
        error(err_line, err_col, "empty character constant")
    elif the_ch == '\\':
        next_ch()
        if the_ch == 'n':
            n = 10
        elif the_ch == '\\':
            n = ord('\\')
        else:
            error(err_line, err_col, "unknown escape sequence \\%c" % (the_ch))
    if next_ch() != '\'':
        error(err_line, err_col, "multi-character constant")
    next_ch()
    return tk_Integer, err_line, err_col, n
 
#*** process divide or comments
def div_or_cmt(err_line, err_col):
    if next_ch() != '*':
        return tk_Div, err_line, err_col
 
    # comment found
    next_ch()
    while True:
        # for multiline comments and single line comments
        if the_ch == '*' or the_ch=='/':
            if next_ch() == '/':
                next_ch()
                return gettok()
        elif len(the_ch) == 0:
            error(err_line, err_col, "EOF in comment")
        else:
            next_ch()
# process preprocessor directives
def cmt_or_init(err_line, err_col):
    # ignore preprocessor directive
    next_ch()
    while True:
        # for preprocessor directives
        pd='nclude <stdio.h>'
        if the_ch=='i':
            for b in pd:
                next_ch()
                if next_ch()==b:
                    next_ch()
                 
            
            return tk_PreDirective, err_line, err_col
    
        if len(the_ch)==0:
            # meaning the comment is empty
            error(err_line,err_col, "EOF in preprocessor directive")
        else:
            #try return gettok()
            next_ch()
# check if import or package
def check_word(word):
    # wordss=[]
    # for c in word:
    #     wordss.append(c)
    # l1=wordss[0]
    # l2=wordss[1]
    # word=word.replace(l1, '', 1)
    # word= word.replace(l2, '', 1)
    for b in word:
        next_ch()
        if next_ch()==b:
            next_ch()
            return True
def annotate(err_line, err_col):
    next_ch()
    while True:
        for b in range(0,20):
            if the_ch==')':
                next_ch()
                return tk_annotation,err_line, err_col
            else:
                next_ch()
    while False:
        return tk_annotation,err_line, err_col
def importpkg(err_line,err_col):
    next_ch()
    while True:
        # for preprocessor directives
        for g in range(0,20):
                next_ch()
                if the_ch==';':
                    next_ch()
                    return gettok()
      
def decpkg(err_line,err_col):
    next_ch()
    while True:
        # for preprocessor directives
        for g in range(0,20):
                next_ch()
                if the_ch==';':
                    return gettok()
def check_print(err_line,err_col):
    next_ch()
    while True:
        # for preprocessor directives
            pt='.out.println'
            next_ch()
            while True:
                if the_ch=='t':
                    for n in pt:
                        if the_ch==n:
                            next_ch()
                            for g in range(0,20):
                                
                                    if the_ch=='(':
                                        return gettok()
                                    else:
                                        next_ch()
            while False:
                for g in range(0,20):
                    if the_ch==')':
                        return gettok()
                    else:
                        next_ch()

def mainbrac(err_line,err_col):
    next_ch()
    while True:
        # for multiline comments and single line comments
        # check if the next line is a class
        if the_ch=='c':
            return tk_Public,err_line,err_col
        if the_ch=='s':
            strd='public static void main(String[] args)'
            for g in strd:
                    next_ch()
                    if the_ch=='s':
                        next_ch()
                        return gettok()
        else:
            #try return gettok()
            return ident_or_int(err_line,err_col)
#*** "string"
def string_lit(start, err_line, err_col):
    text = ""
 
    while next_ch() != start:
        if len(the_ch) == 0:
            error(err_line, err_col, "EOF while scanning string literal")
        if the_ch == '\n':
            error(err_line, err_col, "EOL while scanning string literal")
        text += the_ch
 
    next_ch()
    return tk_String, err_line, err_col, text
def mainmethod(err_line, err_col):
    is_number=True
    text = ""
 
    while the_ch.isalnum() or the_ch == '_':
        text += the_ch
        if not the_ch.isdigit():
            is_number = False
        next_ch()
    if len(text) == 0:
        error(err_line, err_col, "ident_or_int: unrecognized character: (%d) '%c'" % (ord(the_ch), the_ch))
 
    if text[0].isdigit():
        if not is_number:
            error(err_line, err_col, "invalid number: %s" % (text))
        n = int(text)
        return tk_Integer, err_line, err_col, n
    return text
#*** handle identifiers and integers
def ident_or_int(err_line, err_col):
    is_number = True
    text = ""
 
    while the_ch.isalnum() or the_ch == '_':
        text += the_ch
        if not the_ch.isdigit():
            is_number = False
        next_ch()
 
    if len(text) == 0:
        error(err_line, err_col, "ident_or_int: unrecognized character: (%d) '%c'" % (ord(the_ch), the_ch))
 
    if text[0].isdigit():
        if not is_number:
            error(err_line, err_col, "invalid number: %s" % (text))
        n = int(text)
        return tk_Integer, err_line, err_col, n
    # operators
    if text in key_words:
        return key_words[text], err_line, err_col
    #handling data types
    if text in data_types:
        if text == 'new':# make a dictionary for these words
            return gettok()
        if text == 'Scanner':
                
                if  next_ch() =='S':
                    return data_types[text],err_line,err_col
                else:
                    return gettok()
        else:
            return data_types[text],err_line,err_col
    if text=='class':
            return tk_ClassType,err_line,err_col
    if text in decalrative:
        if text == 'import':
            importpkg( err_line, err_col)
            return tk_import, err_line, err_col
        elif text=='package':
            decpkg( err_line, err_col)
            return tk_package, err_line, err_col
        elif text=='public':
            mainbrac(err_line, err_col)
            return tk_mainmethod, err_line, err_col
        else:
            return decalrative[text],err_line,err_col
    # if ident begins with system
    if text == 'System':
        
        next_ch()
        next_ch()
        # print(the_ch)
        if the_ch=='n':
            gettok()
            return tk_Print,err_line,err_col
        elif the_ch=='u':
            for g in range(0,20):
                if the_ch=='n':
                    next_ch()
                    for b in range(0,10):
                        if the_ch=='(':
                            return tk_println,err_line,err_col
                        else:
                            next_ch()
                else:
                    next_ch()

     
 
    return tk_Ident, err_line, err_col, text
 
#*** look ahead for '>=', etc.
def follow(expect, ifyes, ifno, err_line, err_col):
    if next_ch() == expect:
        next_ch()
        return ifyes, err_line, err_col
 
    if ifno == tk_EOI:
        error(err_line, err_col, "follow: unrecognized character: (%d) '%c'" % (ord(the_ch), the_ch))
 
    return ifno, err_line, err_col
 
#*** return the next token type
def gettok():
    while the_ch.isspace():
        next_ch()
 
    err_line = the_line
    err_col  = the_col
 
    if len(the_ch) == 0:    return tk_EOI, err_line, err_col
    elif the_ch == '/':     return div_or_cmt(err_line, err_col)
    elif the_ch == '#':     return cmt_or_init(err_line,err_col)
    elif the_ch == '\'':    return char_lit(err_line, err_col)
    elif the_ch == '<':     return follow('=', tk_Leq, tk_Lss,    err_line, err_col)
    elif the_ch == '>':     return follow('=', tk_Geq, tk_Gtr,    err_line, err_col)
    elif the_ch == '=':     return follow('=', tk_Eq,  tk_Assign, err_line, err_col)
    elif the_ch == '!':     return follow('=', tk_Neq, tk_Not,    err_line, err_col)
    elif the_ch == '&':     return follow('&', tk_And, tk_EOI,    err_line, err_col)
    elif the_ch == '|':     return follow('|', tk_Or,  tk_EOI,    err_line, err_col)
    elif the_ch == '"':     return string_lit(the_ch, err_line, err_col)
    elif the_ch == "@":     return annotate(err_line, err_col)
    # if statement begins with import or package print the whole line as package_import and package_name
    elif the_ch in symbols:
        sym = symbols[the_ch]
        next_ch()
        return sym, err_line, err_col
    else: return ident_or_int(err_line, err_col)
 
#*** main driver

try:
    input_file = open('code.txt', "r", 4096)
except:
    print("Can't open code.txt")
lex=[]
while True:
    t = gettok()
    tok  = t[0]
    line = t[1]
    col  = t[2]
    # output of the lexer
    
  
    print("%5d  %5d   %-14s" % (line, col, all_syms[tok]), end='')
    b=line, col, all_syms[tok]
    
    
    
    if tok == tk_Integer:  
        print("   %5d" % (t[3]))
        lex.append([line, col, all_syms[tok],str(t[3])])
    elif tok == tk_Ident:  
        print("  %s" %   (t[3]))
        lex.append([line, col, all_syms[tok],str(t[3])])
    elif tok == tk_String: 
        print('  "%s"' % (t[3]))
        lex.append([line, col, all_syms[tok],str(t[3])])
    else:                  
        print("")
        lex.append([line, col, all_syms[tok]])
    if tok == tk_EOI:
        break

def arrtostr(ite):
    strr=''
    for b in ite:
        strr+=str(b)+'   '
    return strr
print('writing to lexeroutput.txt.................................')
with  open('lexeroutput.txt', 'w+') as doc:
    for line in lex[:-1]:
        doc.write(arrtostr(line)+'\n')
    else:
        doc.write(arrtostr(lex[-1]))
    doc.close()
print('sucessfully written to lexeroutput.txt ✔️\n')
# remove empty lines now

