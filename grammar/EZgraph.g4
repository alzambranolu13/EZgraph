grammar EZgraph;

s   : exp ;

exp   : e exp
      |  ;

e   : (declaracion | creacion  | leer | imprimir | ciclo | pintar | funcion );


creacion    : TIPOGRAFO ID '[' INT ']' ';' ;


declaracion         : ID '=' value;

leer    : 'read' '(' ID ')' ';';


imprimir    : 'print' '(' value ')' ';';

value   : funciondeclaracion
        | STRING ';'
        | INT ';'
        | DOUBLE ';'
        | BOOLEANO ';'
        | ID;

funciondeclaracion  : ID '.' FUNCIONCPARAM '(' ')' ';'
                    | ID '.' FUNCIONUNPARAM '('INT')' ';'
                    | ID '.' FUNCIONDOPARAM '('INT ',' INT')' ';' ;

funcion : ID '.' ADDEDGE '(' INT ',' INT')' ';'
        | ID '.' ADDEDGE '(' INT ',' INT',' INT')' ';'
        | ID '.' DELETEEDGE '(' INT ',' INT')' ';' ;



pintar  : ID '.' 'paint' '(' ')' ';';

ciclo : 'for' ID  '='  value ':' value '{'exp'}' ;

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
                    | 'getMatrix'
                    | 'getAllDistances'
                    | 'getMinimunSpanningTree'
                    | 'getMaximunSpanningTree'
                    | 'hasCycle'
                    | 'getSCC'
                    | 'getTopologicalOrder' ;
FUNCIONUNPARAM       : 'getDistancesFromNode'
                    | 'BFS'
                    | 'DFS' ;
FUNCIONDOPARAM      : 'getDistance'
                    | 'getShortestPath';
ADDEDGE             : 'addEdge' ;
DELETEEDGE          : 'deleteEdge' ;
TIPOGRAFO           : 'NDGraph'
                    | 'DGraph'
                    | 'DWGraph'
                    | 'NDWGraph';
ID 		            : [a-zA-Z][a-zA-Z0-9_]* ;











