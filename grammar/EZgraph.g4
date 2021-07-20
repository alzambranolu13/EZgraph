grammar EZgraph;

s   : exp ;

exp   : e exp
      |  ;

e   : (declaracion | creacion | asignacion | leer | imprimir | ciclo | pintar | funcion );


creacion    : TIPOGRAFO ID '[' INT ']' ';' ;



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

funciondeclaracion  : ID '.' FUNCIONCPARAM '(' ')' ';'
                    | ID '.' FUNCIONUNPARM '('INT')' ';'
                    | ID '.' FUNCIONDOPARAM '('INT ',' INT')' ';' ;

funcion : ID '.' ADDEDGE '(' INT ',' INT')' ';'
        | ID '.' ADDEDGE '(' INT ',' INT',' INT')' ';'
        | ID '.' DELETEEDGE '(' INT ',' INT')' ';' ;


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
                    | TIPOGRAFO
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
FUNCIONCPARAM       :'getNumEdges'
                    | 'getNodes'
                    | 'getEdges'
                    | 'getSize'
                    | 'getMatrix'
                    | 'getAllDistances'
                    | 'getShortestPath'
                    | 'getMinimunSpanningTree'
                    | 'getMaximunSpanningTree'
                    | 'hasCycle'
                    | 'getSCC'
                    | 'getTopologicalOrder' ;
FUNCIONUNPARM       : 'getDistancesFromNode'
                    | 'BFS'
                    | 'DFS' ;
FUNCIONDOPARAM      : 'getDistance' ;
ADDEDGE             : 'addEdge' ;
DELETEEDGE          : 'deleteEdge' ;
TIPOGRAFO           : 'NDGraph'
                    | 'DGraph'
                    | 'DWGraph'
                    | 'NDWGraph';
ID 		            : [a-zA-Z][a-zA-Z0-9_]* ;











