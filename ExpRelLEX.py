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
    'EMIT',
    'CHAR',
    'IF',
    'ELSE',
    'THEN'
)

literals= ['/','*','+','-','!','@',':',';','.','i']

def t_NUM(t):
    r'\d+'
    return t

def t_DO(t):
    r'(?i)\bdo\b'
    return t

def t_LOOP(t):
    r'(?i)\bloop\b'
    return t

def t_BEGIN(t):
    r'(?i)\bbegin\b'
    return t

def t_UNTIL(t):
    r'(?i)\buntil\b'
    return t

def t_MOD(t):
    r'(?i)\bmod\b'
    return t

def t_DUP(t):
    r'(?i)\bdup\b'
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
    r'(?i)\bvariable\b'
    return t

def t_EMIT(t):
    r'(?i)emit'
    return t

def t_CHAR(t):
    r'(?i)char'
    return t

def t_IF(t):
    r'(?i)if'
    return t

def t_ELSE(t):
    r'(?i)else'
    return t

def t_THEN(t):
    r'(?i)then'
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