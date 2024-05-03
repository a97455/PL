# Introdução
No âmbito da unidade curricular de Processamento de Linguagens, foi nos proposto que desenvolvesse-mos um compilador que converta código Forth para a VM. Neste sentido, foram criados dois ficheiros python, um contendo o analisador léxico e outro o sintático, necessários para realizar essa tarefa. Este trabalho requer um foco extra no sentido em que a linguagem utilizada é pós-fixa, formatação que não nos é tão familiar. 

# Ciclos 
Em Forth existem diferentes tipos de ciclos. Uma das estruturações possíveis para os ciclos é a seguinte: 
~~~
10 1 do 
    i . 
loop 
~~~
~~~
variable a 

20 a !
a @ 10 do 5 . loop
~~~
Outra formatação possível é a seguinte: 
~~~
2 begin 
    dup .   
    1 +
    dup 
    10 >
until 
~~~
Relativamente ao analisador sintático, isto obrigou-nos à criação de mais 4 tokens (_DO_, _LOOP_, _BEGIN_ e _UNTIL_) para que os ciclos possam ser. 

Para os implementar no analisador léxico, foram criada mais duas frases (_p\_Frase9_ e _p\_Frase10_), seguindo a seguinte estrutura: 
~~~
Frase : Frase Ciclo1
      | Frase Ciclo2
~~~

Os ciclos, por sua vez, seguem a seguinte formatação:
~~~
Ciclo1 : Fatores DO corpoCiclo LOOP

Ciclo2 : Fatores BEGIN FuncCont UNTIL
       | BEGIN FuncCont UNTIL 
~~~

No caso do primeiro ciclo, par implementar o analisador sintático, primeiro recolhem-se os limites do ciclo. Para as armazenar, reservam-se 2 espaços de memória na stack global da VM. Após isso, é criada uma label para o ciclo. É introduzido o corpo do ciclo nessa label. No ciclo é ainda incrementada a variável que verifica os limites do ciclo e é verificada se a condição de fim de ciclo se verifica. Se se verificar, então o ciclo é terminado. Caso contrário, ocorre um salto para a label anteriormente criada. Neste caso, é ainda implementado _i_. Para o fazer, tivemos de perceber se as operações contidas no ciclo eram 'i' ou diferentes de 'i'. Se fossem diferentes, escrevia-se para a VM o próprio código da instrução. Caso contrário, íamos ver o valor do limite inferior do ciclo e escrevia-se na VM esse valor. 

No caso do segundo ciclo, começa por identificar se recebe argumentos. Em caso afirmativo, entra no caso do _Ciclo2_ em que começa por escrever os argumentos para a stack. Após isso, é criada uma label para o ciclo e posteriormente é escrito o código do corpo do ciclo. No final, verifica-se se o ciclo terminou, a partir do valor da última instrução contida no ciclo. Em caso afirmativo sai do ciclo. Caso contrário, faz um salto para a label criada. No caso de não conter argumentos, entra no outro caso do _Ciclo2_, em todo idêntico ao anteriormente descrito, retirando-se apenas o processo de escrita dos argumentos para a stack. 

As labels dos ciclos tem um nome estruturado, sendo ele _ciclo<\num>_ em que <\num> é o número de ciclo, variável do parser que é incrementada quando um ciclo é criado. 

# Comentários
No Forth, para realizar comentários, basta colocar o bloco que se deseja que seja comentado dentro de parênteses curvos. 

Para identificar os comentários, o analisador léxico teve de ser adaptado para reconhecer mais um token, o _COMMENT_. Esse token reconhece todo o conteúdo presente dentro de parêntese.  

O analisador sintático, em qualquer parte do código, seja numa linha apenas formada por um comentário, dentro de ciclos ou funções, se detetar um comentário, limita-se a não escrever nenhum código para a VM. 
