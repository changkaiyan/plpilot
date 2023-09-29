A Graph Manipulation Language (GML) is a declarative programming language used to specify graph structures and transformations.

program ::= statement*
statement ::= graph_declaration | graph_transformation
graph_declaration ::= "new" IDENTIFIER
graph_transformation ::= "transform" graph_pattern? "to" graph_expression
graph_pattern ::= graph_expression
graph_expression ::= graph_object | graph_composition | graph_query
graph_object ::= node | edge
node ::= "[" node_label "]" 
edge ::= node "->" node
node_label ::= IDENTIFIER
graph_composition ::= "{" graph_expression* "}"
graph_query ::= "select" IDENTIFIER ("where" conditional_expression)?
conditional_expression ::= IDENTIFIER relational_operator IDENTIFIER
relational_operator ::= "<" | "=" | ">"