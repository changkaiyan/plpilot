TinyC [https://tomassetti.me/ebnf/]

Syntax:

program
   : statement+
   ;

statement
   : 'if' paren_expr statement
   | 'if' paren_expr statement 'else' statement
   | 'while' paren_expr statement
   | 'do' statement 'while' paren_expr ';'
   | '{' statement* '}'
   | expr ';'
   | ';'
   ;


