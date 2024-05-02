import ply.lex as lex

tokens = (
    'NUM',
    'MOD',
    'DUP',
    'NOTEQUAL',
    'GREATEREQUAL',
    'GREATER',
    'LESSEQUAL',
    'LESS',
    'EQUAL',
    'VARIABLE',
    'VAR',
    'DO',
    'LOOP',
    'BEGIN',
    'UNTIL',
    'STRING'
)

literals= ['/','*','+','-','!','@',':',';','.','i']

def t_NUM(t):
    r'\d+'
    return t

def t_DO(t):
    r'(?i)do'
    return t

def t_LOOP(t):
    r'(?i)loop'
    return t

def t_BEGIN(t):
    r'(?i)begin'
    return t

def t_UNTIL(t):
    r'(?i)until'
    return t

def t_MOD(t):
    r'(?i)mod'
    return t

def t_DUP(t):
    r'(?i)dup'
    return t

def t_NOTEQUAL(t):
    r'<>'
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_GREATER(t):
    r'>'
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_LESS(t):
    r'<'
    return t

def t_EQUAL(t):
    r'='
    return t

def t_VARIABLE(t):
    r'(?i)variable'
    return t

def t_VAR(t):
    r'[a-hj-zA-HJ-Z]\w*'
    return t

def t_STRING(t):
    r'\.".*?"'
    t.value = t.value[1:] 
    return t

t_ignore = ' \t\n' #ignora espaços, tabs e paragrafos

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()