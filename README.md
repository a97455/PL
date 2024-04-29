# Introdução
No âmbito da unidade curricular de Processamento de Linguagens, foi nos proposto que desenvolvesse-mos um compilador que converta código Forth para a VM. Neste sentido, foram criados dois ficheiros python, um contendo o analisador léxico e outro o sintático, necessários para realizar essa tarefa. Este trabalho requer um foco extra no sentido em que a linguagem utilizada é pós-fixa, formatação que não nos é tão familiar. 

# Ciclos 
Em Forth existem diferentes tipos de ciclos. O seguinte exemplo imprime para o terminal 1 2 3 4 5 6 7 8 9.
~~~
10 1 do 
    i . 
loop ;
~~~
~~~
variable a 

20 a !
a @ 10 do 5 . loop
~~~

Para o mesmo efeito, recorrendo a outros tipo de ciclo, obtém-se o seguinte código.
~~~
2 begin 
    dup .   
    1 +
    dup 
    10 >
until 
~~~
Relativamente ao analisador sintático, isto obrigou-nos à criação de mais 4 token (_DO_, _LOOP_, _BEGIN_ e _UNTIL_) para que os ciclos possam ser. 

Para os implementar no analisador léxico, foram criada mais duas frases (_p\_Frase7_ e _p\_Frase8_), seguindo a seguinte estrutura: 
~~~
"""Frase : Frase Ciclo1"""
~~~
~~~
    """Frase : Frase Ciclo2"""
~~~
No caso do primeiro ciclo, vemos os limites do ciclo e escreve-se tantas vezes o código inserido no ciclo quantas as interações que se pretende que este faça. 

No caso do segundo ciclo, caso este receba variáveis, então estas vão ser colocadas na stack. Em seguida é criada uma label para esse ciclo. Após a realização das tarefas inerentes ao ciclo, é verificada se a condição de saída do ciclo é verdadeira. Em caso afirmativo, então sai do ciclo. Caso contrário, dá um salto para a label do ciclo pretendido. 

# Extras

### DUP
No Forth existe a possibilidade de duplicar certas variáveis na stack. Decidimos então implementar esta funcionalidade no nosso projeto. No analisar sintático, foi adicionado um token, _DUP_. Quando uma expressão continha um dup, é gerado o código _dup 1_ para a VM. 