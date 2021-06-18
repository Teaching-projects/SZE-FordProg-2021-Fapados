
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startBOOLEAN COLON COMMA LBRACE LBRACKET NULL NUMBER RBRACE RBRACKET STRING\n        value : NUMBER\n              | STRING\n              | BOOLEAN\n              | NULL\n              | object\n              | array\n        \n        start : object\n              | array\n        \n        object : LBRACE pairs RBRACE\n        \n        pairs : pair\n              | empty\n        \n        pair : STRING COLON value COMMA pair\n             | STRING COLON value\n        \n        array : LBRACKET items RBRACKET\n        \n        items : item\n              | empty\n        \n        item : value COMMA item\n             | value\n        \n        empty :\n        '
    
_lr_action_items = {'LBRACE':([0,5,21,23,],[4,4,4,4,]),'LBRACKET':([0,5,21,23,],[5,5,5,5,]),'$end':([1,2,3,20,22,],[0,-7,-8,-9,-14,]),'STRING':([4,5,21,23,26,],[9,15,15,15,9,]),'RBRACE':([4,6,7,8,14,15,16,17,18,19,20,22,24,27,],[-19,20,-10,-11,-1,-2,-3,-4,-5,-6,-9,-14,-13,-12,]),'RBRACKET':([5,10,11,12,13,14,15,16,17,18,19,20,22,25,],[-19,22,-15,-16,-18,-1,-2,-3,-4,-5,-6,-9,-14,-17,]),'NUMBER':([5,21,23,],[14,14,14,]),'BOOLEAN':([5,21,23,],[16,16,16,]),'NULL':([5,21,23,],[17,17,17,]),'COLON':([9,],[21,]),'COMMA':([13,14,15,16,17,18,19,20,22,24,],[23,-1,-2,-3,-4,-5,-6,-9,-14,26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'object':([0,5,21,23,],[2,18,18,18,]),'array':([0,5,21,23,],[3,19,19,19,]),'pairs':([4,],[6,]),'pair':([4,26,],[7,27,]),'empty':([4,5,],[8,12,]),'items':([5,],[10,]),'item':([5,23,],[11,25,]),'value':([5,21,23,],[13,24,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('value -> NUMBER','value',1,'p_value','JSON_parse.py',20),
  ('value -> STRING','value',1,'p_value','JSON_parse.py',21),
  ('value -> BOOLEAN','value',1,'p_value','JSON_parse.py',22),
  ('value -> NULL','value',1,'p_value','JSON_parse.py',23),
  ('value -> object','value',1,'p_value','JSON_parse.py',24),
  ('value -> array','value',1,'p_value','JSON_parse.py',25),
  ('start -> object','start',1,'p_start','JSON_parse.py',31),
  ('start -> array','start',1,'p_start','JSON_parse.py',32),
  ('object -> LBRACE pairs RBRACE','object',3,'p_object','JSON_parse.py',38),
  ('pairs -> pair','pairs',1,'p_pairs','JSON_parse.py',44),
  ('pairs -> empty','pairs',1,'p_pairs','JSON_parse.py',45),
  ('pair -> STRING COLON value COMMA pair','pair',5,'p_pair','JSON_parse.py',51),
  ('pair -> STRING COLON value','pair',3,'p_pair','JSON_parse.py',52),
  ('array -> LBRACKET items RBRACKET','array',3,'p_array','JSON_parse.py',57),
  ('items -> item','items',1,'p_items','JSON_parse.py',63),
  ('items -> empty','items',1,'p_items','JSON_parse.py',64),
  ('item -> value COMMA item','item',3,'p_item','JSON_parse.py',70),
  ('item -> value','item',1,'p_item','JSON_parse.py',71),
  ('empty -> <empty>','empty',0,'p_empty','JSON_parse.py',76),
]