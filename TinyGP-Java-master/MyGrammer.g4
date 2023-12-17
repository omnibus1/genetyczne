grammar MyGrammer;
expr: left_quote expr binary_operator expr right_quote | unary_operator left_quote expr right_quote| floatVal| variable;

binary_operator: mul|div|add|sub;

left_quote: '(';

right_quote: ')';

mul: ' * ';
div: ' / ';
add: ' + ';
sub: ' - ';

floatVal: FLOAT;

variable: VARIABLE;

unary_operator: 'sin' | 'cos';

FLOAT   : [-]?[0-9]+ '.' [0-9]+
        | [-]?'.' [0-9]+;

VARIABLE: 'X1'|'X2';