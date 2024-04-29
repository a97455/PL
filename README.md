# Ciclos em forth
O seguinte exemplo de ciclo imprime para o terminal 1 2 3 4 5 6 7 8 9.
~~~
: loop-exemplo 10 1 
do
    i .  
loop ;

loop-exemplo
~~~