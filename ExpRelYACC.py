import ply.yacc as yacc
from ExpRelLEX import tokens

def p_Prog(p):
    """Prog : Frase"""
    p[0] = '\tpushn '+str(parser.nextAdr)+'\n'
    p[0] += 'start\n'
    p[0] += p[1]
    p[0] += 'stop\n'

def p_Frase1(p):
    """Frase : """
    p[0] = ''

def p_Frase2(p):
    """Frase : Frase STRING"""
    p[0]= p[1]+'\tpushs ' + p[2] + '\n' + '\twrites\n' 

def p_Frase3(p):
    """Frase : Frase Exp"""
    p[0] = p[1]+p[2]

def p_Frase4(p):
    """Frase : Frase Exp '.'"""
    p[0] = p[1]+p[2]+'\twritei\n'

def p_Frase5(p):
    """Frase : Frase Decl"""
    p[0] = p[1]+p[2]

def p_Frase6(p):
    """Frase : Frase Atrib"""
    p[0] = p[1]+p[2]

def p_Frase7(p):
    """Frase : Frase FuncDecl"""
    p[0] = p[1]+p[2]

def p_Frase8(p):
    """Frase : Frase FuncAtrib"""
    p[0] = p[1]+p[2]

def p_Frase9(p):
    """Frase : Frase Ciclo1"""
    p[0] = p[1]+p[2]

def p_Frase10(p):
    """Frase : Frase Ciclo2"""
    p[0] = p[1]+p[2]

def p_Frase11(p):
    """Frase : Frase Condicional1"""
    p[0] = p[1]+p[2]

def p_Frase12(p):
    """Frase : Frase Condicional2"""
    p[0] = p[1]+p[2]

def p_Frase13(p):
    """Frase : Frase CHAR VAR '.'"""
    p[0] = p[1]+f'\tpushs "{p[3]}"\n'+'\tchrcode\n'+'\twritei\n'

def p_Frase14(p):
    """Frase : Frase COMMENT """
    p[0] = p[1]

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
        p[0] = p[1]+'\tstoreg '+str(parser.tabVAR[p[2]])+'\n'
    else:
        print(f"Erro semântico: Variável {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_Atrib2(p):
    """Atrib : Exp VAR '!'"""
    if p[2] in parser.tabVAR.keys():
        p[0] = p[1]+'\tstoreg '+str(parser.tabVAR[p[2]])+'\n'
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
        parser.tabFunc[p[2]] = p[3]
        p[0] = ''

def p_FuncCont1(p):
    """FuncCont : """
    p[0] = list()

def p_FuncCont2(p):
    """FuncCont : FuncCont Fatores"""
    p[0] = p[1] + [p[2]]

def p_FuncCont3(p):
    """FuncCont : FuncCont '+'"""
    p[0] = p[1] + ['\tadd\n']

def p_FuncCont4(p):
    """FuncCont : FuncCont '-'"""
    p[0] = p[1] + ['\tsub\n']

def p_FuncCont5(p):
    """FuncCont : FuncCont '*'"""
    p[0] = p[1] + ['\tmul\n']

def p_FuncCont6(p):
    """FuncCont : FuncCont '/'"""
    p[0] = p[1] + ['\tdiv\n']

def p_FuncCont7(p):
    """FuncCont : FuncCont MOD"""
    p[0] = p[1] + ['\tmod\n']

def p_FuncCont8(p):
    """FuncCont : FuncCont GREATEREQUAL"""
    p[0] = p[1] + ['\tsupeq\n']

def p_FuncCont9(p):
    """FuncCont : FuncCont GREATER"""
    p[0] = p[1] + ['\tsup\n']

def p_FuncCont10(p):
    """FuncCont : FuncCont LESSEQUAL"""
    p[0] = p[1] + ['\tinfeq\n']

def p_FuncCont11(p):
    """FuncCont : FuncCont LESS"""
    p[0] = p[1] + ['\tinf\n']

def p_FuncCont12(p):
    """FuncCont : FuncCont EQUAL"""
    p[0] = p[1] + ['\tequal\n']

def p_FuncCont13(p):
    """FuncCont : FuncCont NOTEQUAL"""
    p[0] = p[1] + ['\tequal\n'+'\tnot\n']

def p_FuncCont14(p): 
    """FuncCont : FuncCont DUP"""
    p[0] = p[1]+['\tdup 1\n']
    
def p_FuncCont15(p):
    """FuncCont : FuncCont '.'"""
    p[0]=p[1] + ['\twritei\n']

def p_FuncCont16(p):
    """FuncCont : FuncCont STRING"""
    p[0]=p[1] + ['\tpushs ' + p[2] + '\n' + '\twrites\n']

def p_FuncCont17(p):
    """FuncCont : FuncCont Condicional1"""
    p[0]=p[1] + [p[2]]

def p_FuncCont18(p):
    """FuncCont : FuncCont Condicional2"""
    p[0]=p[1] + [p[2]]

def p_FuncCont19(p):
    """FuncCont : FuncCont Ciclo1"""
    p[0]=p[1] + [p[2]]

def p_FuncCont20(p):
    """FuncCont : FuncCont Ciclo2"""
    p[0]=p[1] + [p[2]]

def p_FuncCont21(p):
    """FuncCont : FuncCont COMMENT"""
    p[0]=p[1]

def p_FuncAtrib1(p):
    """FuncAtrib : Fatores VAR FuncPrint"""
    if p[2] in parser.tabFunc.keys():
        p[0]=p[1]
        for cont in parser.tabFunc[p[2]]:
            p[0]+=cont
        p[0]+=p[3]
    else:
        print(f"Erro semântico: Função {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_FuncAtrib2(p):
    """FuncAtrib : Exp VAR FuncPrint"""
    if p[2] in parser.tabFunc.keys():
        p[0]=p[1]
        for cont in parser.tabFunc[p[2]]:
            p[0]+=cont
    else:
        print(f"Erro semântico: Função {p[2]} não declarada.")
        parser.success = False
        p[0] = ''

def p_FuncAtrib3(p):
    """FuncAtrib : VAR FuncPrint"""
    if p[1] in parser.tabFunc.keys():
        p[0]=''
        for cont in parser.tabFunc[p[1]]:
            p[0]+=cont
    else:
        print(f"Erro semântico: Função {p[1]} não declarada.")
        parser.success = False
        p[0] = ''

def p_FuncPrint1(p):
    """FuncPrint : """
    p[0] = ''

def p_FuncPrint2(p):
    """FuncPrint : '.'"""
    p[0] = '\twritei\n'

def p_Ciclo1(p):
    """Ciclo1 : Fatores DO corpoCiclo LOOP """

    if(p[1].count('\n')==2):
        argumentos = p[1].split('\n')

        posicao_1 = parser.nextAdr
        parser.nextAdr+=1
        posicao_2 = parser.nextAdr
        parser.nextAdr+=1

        p[0]=''
        p[0]+=argumentos[0]+'\n'
        p[0]+='\tstoreg '+str(posicao_1)+'\n'
        p[0]+=argumentos[1]+'\n'
        p[0]+='\tstoreg '+str(posicao_2)+'\n'

        p[0]+='ciclo'+str(parser.idCiclo)+':\n'

        for elem in p[3]:
            if elem=='i\n':
                p[0]+='\tpushg '+str(posicao_2)+'\n'
            else:
                p[0]+=elem

        p[0]+='\tpushg '+str(posicao_2)+'\n'
        p[0]+='\tpushi 1\n'
        p[0]+='\tadd\n'
        p[0]+='\tstoreg '+str(posicao_2)+'\n'

        p[0]+='\tpushg '+str(posicao_1)+'\n'
        p[0]+='\tpushg '+str(posicao_2)+'\n'
        p[0]+='\tinfeq\n'
        p[0]+='\tjz ciclo'+str(parser.idCiclo)+'\n'
        parser.idCiclo+=1

def p_Ciclo2(p):
    """Ciclo2 : Fatores BEGIN FuncCont UNTIL """

    argumentos = p[1].split('\n')
    lista_enderecos_codigo=[]
    for i in range(len(argumentos)-1):
        lista_enderecos_codigo.append((argumentos[i]+'\n',parser.nextAdr))
        parser.nextAdr+=1

    p[0]=''
    for elemento in lista_enderecos_codigo:
        p[0]+=elemento[0]
        p[0]+='\tstoreg '+str(elemento[1])+'\n'

    for elemento in lista_enderecos_codigo:
        p[0]+='\tpushg '+str(elemento[1])+'\n'

    p[0]+='ciclo'+str(parser.idCiclo)+':\n'

    for elem in p[3]:
        p[0]+=elem
    p[0]+='\tjz ciclo'+str(parser.idCiclo)+'\n'

    parser.idCiclo+=1

def p_Ciclo3(p):
    """Ciclo2 : BEGIN FuncCont UNTIL """
    p[0]=''
    p[0]+='ciclo'+str(parser.idCiclo)+':\n'

    for elem in p[2]:
        p[0]+=elem
    p[0]+='\tjz ciclo'+str(parser.idCiclo)+'\n'

    parser.idCiclo+=1

def p_corpoCiclo1(p):
    """corpoCiclo : corpoCiclo 'i' """
    p[0]= p[1] + ['i\n']

def p_corpoCiclo2(p):
    """corpoCiclo : corpoCiclo FuncCont"""
    p[0] = p[1] + p[2] 

def p_corpoCiclo3(p):
    """corpoCiclo : """
    p[0] = []

def p_Condicional1(p):
    """Condicional1 : IF FuncCont THEN"""
    p[0] = f"\tjz endif{parser.cont}\n" 
    for cont in p[2]:
        p[0]+=cont 
        
    p[0]+=f"endif{parser.cont}:\n"
    parser.cont +=1

def p_Condicional2(p):
    """Condicional2 : IF FuncCont ELSE FuncCont THEN"""
    p[0] = f"\tjz else{parser.cont}\n"
    for cont in p[2]:
        p[0]+=cont

    p[0]+=f"\tjump endif{parser.cont}\n" + f"else{parser.cont}:\n" 
    for cont in p[4]:
        p[0]+=cont
        
    p[0]+=f"endif{parser.cont}:\n"
    parser.cont +=1

def p_Exp1(p):
    """Exp : Fatores"""
    p[0] = p[1]

def p_Exp2(p): 
    """Exp : Exp '+'"""
    p[0] = p[1]+'\tadd\n'

def p_Exp3(p): 
    """Exp : Exp '-'"""
    p[0] = p[1]+'\tsub\n'

def p_Exp4(p): 
    """Exp : Exp '*'"""
    p[0] = p[1]+'\tmul\n'

def p_Exp5(p): 
    """Exp : Exp '/'"""
    p[0] = p[1]+'\tdiv\n'

def p_Exp6(p): 
    """Exp : Exp MOD"""
    p[0] = p[1]+'\tmod\n'

def p_Exp7(p): 
    """Exp : Exp GREATEREQUAL"""
    p[0] = p[1]+'\tsupeq\n'

def p_Exp8(p): 
    """Exp : Exp GREATER"""
    p[0] = p[1]+'\tsup\n'

def p_Exp9(p): 
    """Exp : Exp LESSEQUAL"""
    p[0] = p[1]+'\tinfeq\n'

def p_Exp10(p): 
    """Exp : Exp LESS"""
    p[0] = p[1]+'\tinf\n'

def p_Exp11(p): 
    """Exp : Exp EQUAL"""
    p[0] = p[1]+'\tequal\n'

def p_Exp12(p): 
    """Exp : Exp NOTEQUAL"""
    p[0] = p[1]+'\tequal\n'+'\tnot\n'

def p_Exp13(p): 
    """Exp : Exp DUP"""
    p[0] = p[1]+'\tdup 1\n'

def p_Exp14(p):
    """Exp : Exp EMIT"""
    p[0]= p[1] + '\twritechr\n'

def p_Exp15(p):
    """Exp : Exp COMMENT"""
    p[0]= p[1]

def p_Fatores1(p):
    """Fatores : Fator"""
    p[0]=p[1]

def p_Fatores2(p):
    """Fatores : Fatores Fator"""
    p[0]=p[1]+p[2]

def p_Fator1(p):
    """Fator : NUM"""
    p[0] = '\tpushi '+p[1]+'\n'

def p_Fator2(p): 
    """Fator : VAR '@'"""
    if p[1] in parser.tabVAR.keys():
        p[0] = '\tpushg '+str(parser.tabVAR[p[1]])+'\n'
    else:
        print(f"Erro semântico: Variável {p[1]} não declarada.")
        parser.success = False
        p[0]=''
    
def p_error(p):
    print(p)
    print("Erro sintático no input!")
    parser.success = False


# Instância do parser
parser = yacc.yacc()
parser.success = True
parser.tabVAR = dict() #VarName -> PosStack 
parser.nextAdr = 0
parser.tabFunc = dict() #FuncName -> [Content]
parser.idCiclo = 1
parser.cont = 1

# Parse da entrada
fonte = ""
with open("Input.txt",'r') as f:
    fonte = f.read()

result = parser.parse(fonte)

# Verifica se o parse foi bem-sucedido e imprime o resultado formatado
if parser.success:
    with open("Output.txt",'w') as f:
        f.write(result)