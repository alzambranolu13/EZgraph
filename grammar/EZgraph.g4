grammar EZgraph;

s   : exp ;

exp   : e exp
      |  ;

e   : (declaracion | creacion | asignacion | leer | imprimir | ciclo | pintar | funcion);


creacion    : tipografo ID '[' ENTERO ']' ';' ;

tipografo   : 'NDGraph'
            | 'DGraph'
            | 'DWGraph'
            | 'NDWGraph'
            ;

declaracion         : tipo ID '=' value
                    | tipo ID  ';' ;

asignacion  : ID '=' value ;

leer    : 'read' '(' ID ')' ';';


imprimir    : 'print' '(' (STRING | ID) ')' ';';

value   : funciondeclaracion
        | STRING ';'
        | INT ';'
        | FLOAT ';'
        | BOOLEANO ';'
        | lista ';'
        | matriz ';' ;

funciondeclaracion  :  ID '.' 'getNumEdges' '('')' ';'
                    | ID '.' 'getNodes' '('')' ';'
                    | ID '.' 'getEdges' '('')' ';'
                    | ID '.' 'getSize' '('')' ';'
                    | ID '.' 'getMatrix' '('')' ';'
                    | ID '.' 'getDistancesFromNode' '('INT')' ';'
                    | ID '.' 'getAllDistances' '('')' ';'
                    | ID '.' 'getDistance' '('INT ',' INT')' ';'
                    | ID '.' 'getShortestPath' '('')' ';'
                    | ID '.' 'getMinimunSpanningTree' '('')' ';'
                    | ID '.' 'getMaximunSpanningTree' '('')' ';'
                    | ID '.' 'hasCycle' '('')' ';'
                    | ID '.' 'getSCC' '('')' ';'
                    | ID '.' 'getTopologicalOrder' '('')' ';'
                    | ID '.' 'BFS' '('INT')' ';'
                    | ID '.' 'DFS' '('INT')' ';';

funcion : ID '.' 'addEdge' '(' INT ',' INT')' ';'
        | ID '.' 'addEdge' '(' INT ',' INT',' INT')' ';'
        | ID '.' 'deleteEdge' '(' INT ',' INT')' ';' ;


lista   : '[' (INT.*? ) ']'
        | '[' (FLOAT.*? ) ']'
        | '[' (STRING.*? ) ']';

matriz  : '[' lista  dentro.*? ']' ;

dentro  : ';' lista;

pintar  : ID '.' 'paint' '(' ')' ';';

tipo                : 'int'
                    | 'string'
                    | 'double'
                    | 'bool'
                    | 'List'
                    | 'Matrix'
                    | tipografo
                    ;

ciclo : 'for' ID  '='  (ID| INT) ':' ID '{' exp'}' ;

COMMENT 		    : '/*' .*? '*/' -> skip ;
LINE_COMMENT 	    : '//' ~[\r\n]* -> skip ;
EASTEREGG           : '😊' .*? '😊 ' -> skip ;
WS		            : [ \t\r\n]+ -> skip ;
DOUBLE	            : [0-9]+([.][0-9]+);
INT                 : [0-9]+;
STRING              : '"' .*? '"';
BOOLEANO            : ('true' | 'false');
ID 		            : [a-zA-Z][a-zA-Z0-9_]* ;