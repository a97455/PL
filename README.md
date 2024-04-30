# Introdução
No âmbito da unidade curricular de Processamento de Linguagens, foi nos proposto que desenvolvesse-mos um compilador que converta código Forth para a VM. Neste sentido, foram criados dois ficheiros python, um contendo o analisador léxico e outro o sintático, necessários para realizar essa tarefa. Este trabalho requer um foco extra no sentido em que a linguagem utilizada é pós-fixa, formatação que não nos é tão familiar. 

# Ciclos 
Em Forth existem diferentes tipos de ciclos. Uma das estruturações possiveis para os ciclos é a seguinte:
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
Outra formatação possivel é a seguinte:
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
No caso do primeiro ciclo, par implementar o analisador sintático, primeiro recolhem-se os limites do ciclo. Para as armazenar, reservam-se 2 espaços de memória na stack global da VM. Após isso, é criada uma label para o ciclo. É introduzido o corpo do ciclo nessa label. No ciclo é ainda incrimentada a variavel que verifica os limites do ciclo e é verificada se a condicao de fim de ciclo se verifica. Se se verificar, então o ciclo é terminado. Caso contrário, ocorre um salto para a label anteriormente criada. 

As labels dos ciclos tem um nome esctruturado, sendo ele _ciclo<\num>_ em que <\num> é o número de ciclo, variavel do parser que é incrementada quando um ciclo é criado.


