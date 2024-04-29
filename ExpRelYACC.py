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
    """Frase : """
    p[0] = ''

def p_Frase2(p):
    """Frase : Frase Exp"""
    p[0] = p[1]+p[2]

def p_Frase3(p):
    """Frase : Frase Decl"""
    p[0] = p[1]+p[2]

def p_Frase4(p):
    """Frase : Frase Atrib"""
    p[0] = p[1]+p[2]

def p_Frase5(p):
    """Frase : Frase FuncDecl"""
    p[0] = p[1]+p[2]

def p_Frase6(p):
    """Frase : Frase FuncAtrib"""
    p[0] = p[1]+p[2]

def p_Frase7(p):
    """Frase : Frase Ciclo"""
    p[0] = p[1]+p[2]

def p_Decl(p):
    """Decl : VARIABLE VAR """
    if p[2] in parser.tabVAR.keys():
        print(f"Erro semântico: Variável {p[2]} já declarada.")
        parser.success = False
    else:
        parser.tabVAR[p[2]] = parser.nextAdr
        parser.nextAdr += 1
        p[0] = ''

def p_Atrib1(p):
    """Atrib : Fatores VAR '!'"""
    if p[2] in parser.tabVAR.keys():
        p[0] = p[1]+'storeg '+str(parser.tabVAR[p[2]])+'\n'
    else:
        print(f"Erro semântico: Variável {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_Atrib2(p):
    """Atrib : Exp VAR '!'"""
    if p[2] in parser.tabVAR.keys():
        p[0] = p[1]+'storeg '+str(parser.tabVAR[p[2]])+'\n'
    else:
        print(f"Erro semântico: Variável {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_FuncDecl(p):
    """FuncDecl : ':' VAR FuncCont ';'"""
    if p[2] in parser.tabFunc.keys():
        print(f"Erro semântico: Função {p[2]} já declarada.")
        parser.success = False
    else:
        parser.tabFunc[p[2]] = (parser.nextAdr,p[3])
        parser.nextAdr+=1
        p[0] = ''

def p_FuncCont1(p):
    """FuncCont : """
    p[0] = list()

def p_FuncCont2(p):
    """FuncCont : FuncCont Fator"""
    p[0] = p[1] + [p[2]]

def p_FuncCont3(p):
    """FuncCont : FuncCont '+'"""
    p[0] = p[1] + ['add\n']

def p_FuncCont4(p):
    """FuncCont : FuncCont '-'"""
    p[0] = p[1] + ['sub\n']

def p_FuncCont5(p):
    """FuncCont : FuncCont '*'"""
    p[0] = p[1] + ['mul\n']

def p_FuncCont6(p):
    """FuncCont : FuncCont '/'"""
    p[0] = p[1] + ['div\n']

def p_FuncCont7(p):
    """FuncCont : FuncCont MOD"""
    p[0] = p[1] + ['mod\n']

def p_FuncCont8(p):
    """FuncCont : FuncCont GREATEREQUAL"""
    p[0] = p[1] + ['supeq\n']

def p_FuncCont9(p):
    """FuncCont : FuncCont GREATER"""
    p[0] = p[1] + ['sup\n']

def p_FuncCont10(p):
    """FuncCont : FuncCont LESSEQUAL"""
    p[0] = p[1] + ['infeq\n']

def p_FuncCont11(p):
    """FuncCont : FuncCont LESS"""
    p[0] = p[1] + ['inf\n']

def p_FuncCont12(p):
    """FuncCont : FuncCont EQUAL"""
    p[0] = p[1] + ['equal\n']

def p_FuncCont13(p):
    """FuncCont : FuncCont NOTEQUAL"""
    p[0] = p[1] + ['equal\n'+'not\n']

def p_FuncAtrib1(p):
    """FuncAtrib : Fatores VAR"""
    if p[2] in parser.tabFunc.keys():
        p[0]=p[1]
        for cont in parser.tabFunc[p[2]][1]:
            p[0]+=cont
        p[0]+='storeg '+str(parser.tabFunc[p[2]][0])+'\n'
    else:
        print(f"Erro semântico: Função {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_FuncAtrib2(p):
    """FuncAtrib : Exp VAR"""
    if p[2] in parser.tabFunc.keys():
        p[0]=p[1]
        for cont in parser.tabFunc[p[2]][1]:
            p[0]+=cont
        p[0]+='storeg '+str(parser.tabFunc[p[2]][0])+'\n'
    else:
        print(f"Erro semântico: Função {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_Ciclo(p):
    """Ciclo : NUM NUM DO Exp LOOP """

    p[0]=''
    for i in range(int(p[2]),int(p[1])):
        p[0] += p[4]

def p_Exp1(p):
    """Exp : Fatores"""
    p[0] = p[1]

def p_Exp2(p): 
    """Exp : Exp '+'"""
    p[0] = p[1]+'add\n'

def p_Exp3(p): 
    """Exp : Exp '-'"""
    p[0] = p[1]+'sub\n'

def p_Exp4(p): 
    """Exp : Exp '*'"""
    p[0] = p[1]+'mul\n'

def p_Exp5(p): 
    """Exp : Exp '/'"""
    p[0] = p[1]+'div\n'

def p_Exp6(p): 
    """Exp : Exp MOD"""
    p[0] = p[1]+'mod\n'

def p_Exp7(p): 
    """Exp : Exp GREATEREQUAL"""
    p[0] = p[1]+'supeq\n'

def p_Exp8(p): 
    """Exp : Exp GREATER"""
    p[0] = p[1]+'sup\n'

def p_Exp9(p): 
    """Exp : Exp LESSEQUAL"""
    p[0] = p[1]+'infeq\n'

def p_Exp10(p): 
    """Exp : Exp LESS"""
    p[0] = p[1]+'inf\n'

def p_Exp11(p): 
    """Exp : Exp EQUAL"""
    p[0] = p[1]+'equal\n'

def p_Exp12(p): 
    """Exp : Exp NOTEQUAL"""
    p[0] = p[1]+'equal\n'+'not\n'

def p_Fatores1(p):
    """Fatores : Fator"""
    p[0]=p[1]

def p_Fatores2(p):
    """Fatores : Fatores Fator"""
    p[0]=p[1]+p[2]

def p_Fator(p):
    """Fator : NUM"""
    p[0] = 'pushi '+p[1]+'\n'

def p_Fator2(p): 
    """Fator : VAR '@'"""
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
parser.tabVAR = dict() #VarName -> PosStack 
parser.nextAdr = 0
parser.tabFunc = dict() #FuncName -> (PosStack,[Content])

# Parse da entrada
fonte = ""
for linha in sys.stdin:
    fonte += linha

result = parser.parse(fonte)

# Verifica se o parse foi bem-sucedido e imprime o resultado formatado
if parser.success:
    print('\n'+result)