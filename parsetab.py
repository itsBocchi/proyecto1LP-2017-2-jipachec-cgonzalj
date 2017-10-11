
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSANDleftTIMESDIVIDErightUMINUSNAME NUMBA PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN AND WURD TYPE COMstatement : NAME EQUALS TYPEstatement : NAME EQUALS expressionstatement : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression AND expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBAexpression : COM WURD COMexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,8,9,10,11,12,13,],[2,15,15,15,15,15,15,15,15,]),'MINUS':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,19,20,21,22,23,24,25,26,],[4,-13,10,4,4,-11,4,4,4,4,4,4,-9,-13,10,10,-4,-5,-6,-7,-8,-10,-12,]),'LPAREN':([0,4,5,8,9,10,11,12,13,],[5,5,5,5,5,5,5,5,5,]),'NUMBA':([0,4,5,8,9,10,11,12,13,],[6,6,6,6,6,6,6,6,6,]),'COM':([0,4,5,8,9,10,11,12,13,17,],[7,7,7,7,7,7,7,7,7,26,]),'$end':([1,2,3,6,14,15,18,19,20,21,22,23,24,25,26,],[0,-13,-3,-11,-9,-13,-1,-2,-4,-5,-6,-7,-8,-10,-12,]),'EQUALS':([2,],[8,]),'PLUS':([2,3,6,14,15,16,19,20,21,22,23,24,25,26,],[-13,9,-11,-9,-13,9,9,-4,-5,-6,-7,-8,-10,-12,]),'TIMES':([2,3,6,14,15,16,19,20,21,22,23,24,25,26,],[-13,11,-11,-9,-13,11,11,11,11,-6,-7,11,-10,-12,]),'DIVIDE':([2,3,6,14,15,16,19,20,21,22,23,24,25,26,],[-13,12,-11,-9,-13,12,12,12,12,-6,-7,12,-10,-12,]),'AND':([2,3,6,14,15,16,19,20,21,22,23,24,25,26,],[-13,13,-11,-9,-13,13,13,-4,-5,-6,-7,-8,-10,-12,]),'RPAREN':([6,14,15,16,20,21,22,23,24,25,26,],[-11,-9,-13,25,-4,-5,-6,-7,-8,-10,-12,]),'WURD':([7,],[17,]),'TYPE':([8,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,8,9,10,11,12,13,],[3,14,16,19,20,21,22,23,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS TYPE','statement',3,'p_statement_declaration','PUPPER.py',67),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','PUPPER.py',71),
  ('statement -> expression','statement',1,'p_statement_expr','PUPPER.py',76),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','PUPPER.py',80),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','PUPPER.py',81),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','PUPPER.py',82),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','PUPPER.py',83),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','PUPPER.py',84),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','PUPPER.py',96),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','PUPPER.py',100),
  ('expression -> NUMBA','expression',1,'p_expression_NUMBA','PUPPER.py',104),
  ('expression -> COM WURD COM','expression',3,'p_expression_wurd','PUPPER.py',108),
  ('expression -> NAME','expression',1,'p_expression_name','PUPPER.py',115),
]
