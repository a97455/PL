import ply.lex as lex

tokens = (
    'NUM',
    'VAR',
    'MOD'
)

literals= ['=','/','*','+','-']

t_MOD = r'(?i)mod'

def t_NUM(t):
    r'\d+'
    return t

def t_VAR(t):
    r'[a-zA-Z]+'
    return t

t_ignore = ' \t\n' #ignora espaços, tabs e paragrafos

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()