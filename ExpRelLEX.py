import ply.lex as lex

tokens = (
    'NUM',
    'MOD',
    'NOTEQUAL',
    'GREATEREQUAL',
    'GREATER',
    'LESSEQUAL',
    'LESS',
    'EQUAL',
    'VARIABLE',
    'VAR'
)

literals= ['/','*','+','-','!','@',':',';']

def t_NUM(t):
    r'\d+'
    return t

def t_MOD(t):
    r'(?i)mod'
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
    r'[a-zA-Z]\w*'
    return t

t_ignore = ' \t\n' #ignora espaços, tabs e paragrafos

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()