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
    """Frase : Frase Atrib"""
    p[0] = p[1]+p[2]

def p_Frase2(p):
    """Frase : """
    p[0] = ''

def p_Atrib(p):
    """Atrib : VAR '=' Exp"""
    if p[1] in parser.tabVAR.keys():
        p[0] = p[3]+'storeg '+str(parser.tabVAR[p[1]])+'\n'
    else:
        parser.tabVAR[p[1]] = parser.nextAdr
        parser.nextAdr+=1
        p[0] = p[3]+'storeg '+str(parser.tabVAR[p[1]])+'\n'

def p_Exp1(p):
    """Exp : Termo"""
    p[0] = p[1]

def p_Exp2(p): 
    """Exp : Exp Termo '+'"""
    p[0] = p[1]+p[2]+'add\n'

def p_Exp3(p): 
    """Exp : Exp Termo '-'"""
    p[0] = p[1]+p[2]+'sub\n'

def p_Termo(p):
    """Termo : Fator"""
    p[0] = p[1]

def p_Termo2(p): 
    """Termo : Termo Fator '*'"""
    p[0] = p[1]+p[2]+'mul\n'

def p_Termo3(p): 
    """Termo : Termo Fator '/'"""
    p[0] = p[1]+p[2]+'div\n'

def p_Termo4(p): 
    """Termo : Termo Fator MOD"""
    p[0] = p[1]+p[2]+'mod\n'

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
    print("Parsing terminou com sucesso")
    print(result)