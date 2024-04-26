import ply.yacc as yacc
import sys
from ExpRelLEX import tokens

def p_Prog(p):
    """Prog : Frase"""
    p[0] = 'pushn '+str(parser.nextAdr)+'\n'
    p[0] += 'start\n'
    p[0] += p[1]
    p[0] += 'stop\n'

def p_Frase1(p):
    """Frase : Frase Decl"""
    p[0] = p[1]+p[2]

def p_Frase2(p):
    """Frase : Frase Atrib"""
    p[0] = p[1]+p[2]

def p_Frase3(p):
    """Frase : Frase Exp"""
    p[0] = p[1]+p[2]

def p_Frase4(p):
    """Frase : """
    p[0] = ''

def p_Decl(p):
    """Decl : VARIABLE VAR """
    if p[2] in parser.tabVAR.keys():
        print(f"Erro semântico: Variável {p[2]} já declarada.")
        parser.success = False
    else:
        parser.tabVAR[p[2]] = parser.nextAdr
        parser.nextAdr += 1
        p[0] = ''

def p_Atrib(p):
    """Atrib : Exp VAR '!'"""
    if p[2] in parser.tabVAR.keys():
        p[0] = p[1]+'storeg '+str(parser.tabVAR[p[2]])+'\n'
    else:
        print(f"Erro semântico: Variável {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_Exp1(p):
    """Exp : Fator"""
    p[0] = p[1]

def p_Exp2(p): 
    """Exp : Exp Exp '+'"""
    p[0] = p[1]+p[2]+'add\n'

def p_Exp3(p): 
    """Exp : Exp Exp '-'"""
    p[0] = p[1]+p[2]+'sub\n'

def p_Exp4(p): 
    """Exp : Exp Exp '*'"""
    p[0] = p[1]+p[2]+'mul\n'

def p_Exp5(p): 
    """Exp : Exp Exp '/'"""
    p[0] = p[1]+p[2]+'div\n'

def p_Exp6(p): 
    """Exp : Exp Exp MOD"""
    p[0] = p[1]+p[2]+'mod\n'

def p_Exp7(p): 
    """Exp : Exp Exp GREATEREQUAL"""
    p[0] = p[1]+p[2]+'supeq\n'

def p_Exp8(p): 
    """Exp : Exp Exp GREATER"""
    p[0] = p[1]+p[2]+'sup\n'

def p_Exp9(p): 
    """Exp : Exp Exp LESSEQUAL"""
    p[0] = p[1]+p[2]+'infeq\n'

def p_Exp10(p): 
    """Exp : Exp Exp LESS"""
    p[0] = p[1]+p[2]+'inf\n'

def p_Exp11(p): 
    """Exp : Exp Exp EQUAL"""
    p[0] = p[1]+p[2]+'equal\n'

def p_Exp12(p): 
    """Exp : Exp Exp NOTEQUAL"""
    p[0] = p[1]+p[2]+'equal\n'+'not\n'

def p_Fator(p):
    """Fator : NUM"""
    p[0] = 'pushi '+p[1]+'\n'

def p_Fator2(p): 
    """Fator : VAR"""
    if p[1] in parser.tabVAR.keys():
        p[0] = 'pushg '+str(parser.tabVAR[p[1]])+'\n'
    else:
        print(f"Erro semântico: Variável {p[1]} não declarada.")
        parser.success = False
        p[0]=''

def p_error(p):
    print("Erro sintático no input!")
    parser.success = False


# Instância do parser
parser = yacc.yacc()
parser.success = True
parser.tabVAR = dict() #Espaços de memória reservados para as diversas variáveis
parser.nextAdr = 0

# Parse da entrada
fonte = ""
for linha in sys.stdin:
    fonte += linha

result = parser.parse(fonte)

# Verifica se o parse foi bem-sucedido e imprime o resultado formatado
if parser.success:
    print(result)