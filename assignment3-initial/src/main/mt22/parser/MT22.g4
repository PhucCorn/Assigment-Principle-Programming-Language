grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist? EOF;
/////DECLARATION
decllist: decl decltail;
decltail: decl decltail |;
decl: vardecl | funcdecl;
//variables declaration
vardecl: idlist COLON vartype SEMI | initiazation;
initiazation: initcy SEMI;
initcy: ID COMMA initcy COMMA val | ID COLON atyp EQ val ;
//function declaration
funcdecl: ID COLON FUNCTION typ LB paramlist RB (INHERIT ID)? body;
paramlist: param paramprime | ;
paramprime: COMMA param paramprime | COMMA param | ;
//param: INHERIT? OUT? idlist COLON atyp;
param: INHERIT? OUT? ID COLON atyp;
body: blockstmt;
/////END DECLARATION


/////STATEMENT
// function statement
//blockfuncstmt: LCB (funcstmtlist|) RCB | '{}';
//funcstmtlist: funcstmt SEMI funcstmtlist | funcstmt SEMI;
//funcstmt: stmt | retstmt;
// loop statement
//blockloopstmt: LCB (loopstmtlist|) RCB | '{}';
//loopstmtlist: loopstmt SEMI loopstmtlist | loopstmt SEMI;
//loopstmt: breakstmt | contstmt | stmt;
//normal statement
tstmt: (blockstmt|stmt);
fstmt: (blockstmt|stmt);
blockstmt: LCB (stmtlist|) RCB | '{}';
stmtlist: (vardecl|stmt) stmtlist | (vardecl|stmt);
stmt: asstmt | ifstmt | forstmt | whilestmt | dowhilestmt | callstmt | breakstmt | contstmt | retstmt;
//assignment statement
asstmt: lhs EQ expr SEMI;
lhs: ID | indexop;
//if statement
ifstmt: IF LB expr RB tstmt (ELSE fstmt)?;
//for statement
forstmt: FOR LB lhs EQ expr COMMA expr COMMA expr RB (blockstmt|stmt);
//while statement
whilestmt: WHILE LB expr RB (blockstmt|stmt);
//do while statement
dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;
//break statement
breakstmt: BREAK SEMI;
//continue statement
contstmt: CONTINUE SEMI;
//return statement
retstmt: RETURN expr? SEMI;
//call statement
callstmt: (ID|SPECIAL_FUNC) LB (arglist | ) RB SEMI;
/////END STATEMENT


/////EXPRESSIONS
// exprlist: exprlist exprprime | exprprime;
// exprprime: COMMA expr | expr;
exprlist: expr exprprime | expr;
exprprime: COMMA expr | ;
expr: string | funccall;
string: relational DOUBLECOLON relational | relational ;
relational: logical EQUAL logical | logical DIF logical | logical SMALLER logical | logical BIGGER logical | logical SMALLER_OR_EQUAL logical | logical BIGGER_OR_EQUAL logical | logical | STR;
logical: logical AND adding | logical OR adding | adding;
adding: adding ADD multiplying | adding MINUS multiplying | multiplying;
multiplying: multiplying MUL not_logical | multiplying DIV not_logical | multiplying PER | not_logical;
not_logical: NOT not_logical | sign | TRUE | FALSE;
sign: MINUS sign | indexop | ID | INT | FL | ARR | funccall;
indexop: ID LSB exprlist RSB;
//function call
funccall: ID LB (arglist | ) RB;
arglist: arg COMMA arglist | arg;
arg: ID | expr;
/////END EXPRESSIONS


typ: vartype | VOID;
val: INT | FL | TRUE | FALSE | STR | ARR | funccall | expr;
vartype: atyp | AUTO;
atyp: fourarrtype | arraytype;
fourarrtype: BOOLEAN | INTEGER | FLOAT | STRING;
arraytype: ARRAY LSB dimensionlist RSB OF fourarrtype;
dimensionlist: INT COMMA dimensionlist | INT;
idlist: ID COMMA idlist | ID;

/////LEXER
//comment
COMMEMTLINE: '//' ~( '\r' | '\n' )* ->skip;
COMMENTBOX: '/*' .*? '*/' -> skip ;
//array
// ARR: ID '[' ( INARR ( ',' INARR )* )? ']' ;
// fragment INARR: INT | FL | STR | TRUE | FALSE;
ARR: '{' ( VAL ( ',' VAL )* )? '}' ;
fragment VAL: INT | FL | TRUE | FALSE | STR | ID | ARR;
//interger
INT: [0] | [1-9] NUM* (('_') NUM+)* {self.text = self.text.replace("_", "")}; 
fragment NUM: [0-9];
//float
FL: INT (DOT [0-9]* ([Ee] [-]? DIGIT)? | [eE] [-]? DIGIT) {self.text = self.text.replace("_", "")};
fragment DIGIT: [1-9] NUM*;
//string
STR: DQ INSTR* DQ  {self.text = self.text[1:-1]};
fragment INSTR: (~'"'|'\\"') ;

AUTO: 'auto';	
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

ID: [A-Za-z_] [A-Za-z0-9_]*;
SPECIAL_FUNC: ('readInteger' | 'printInteger' | 'readFloat' | 'writeFloat' | 'readBoolean' | 'printBoolean' | 'readString' | 'printString' | 'preventDefault' | 'super');

//TAB: '\t';
//BACKSPACE: '\b';
//FF: '\f';
//CR: '\r';
//LF: '\n';

ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
PER: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
DIF: '!=';
SMALLER: '<';
SMALLER_OR_EQUAL: '<=';
BIGGER: '>';
BIGGER_OR_EQUAL: '>=';
DOUBLECOLON: '::';
LB: '(';
RB: ')';
LCB: [{];
RCB: [}];
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: [,];
SEMI: ';';
COLON: ':';
EQ: [=];
SQ: '\'';
DQ: '"';
BS: '\\';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
// SPECIAL_FUNC: ('readInteger();' | 'printInteger(' .*? ');' | 'readFloat();' | 'writeFloat(' .*? ');' | 'readBoolean();' | 'printBoolean(' .*? ');' | 'readString();' | 'printString(' .*? ');' | 'preventDefault();' | 'super(' .*? ');') -> skip;


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;