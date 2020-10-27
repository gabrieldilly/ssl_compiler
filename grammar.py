from enum import Enum, auto

# Creating enumerations using class
class Words(Enum):

    # reserved words
    ARRAY = auto()              # array
    BOOLEAN = auto()            # boolean
    BREAK = auto()              # break
    CHAR = auto()               # char
    CONTINUE = auto()           # continue
    DO = auto()                 # do
    ELSE = auto()               # else
    FALSE = auto()              # false
    FUNCTION = auto()           # function
    IF = auto()                 # if
    INTEGER = auto()            # integer
    OF = auto()                 # of
    STRING = auto()             # string
    STRUCT = auto()             # struct
    TRUE = auto()               # true
    TYPE = auto()               # type
    VAR = auto()                # var
    WHILE = auto()              # while

    # symbols
    COLON = auto()              # :
    SEMI_COLON = auto()         # ;
    COMMA = auto()              # ,
    EQUALS = auto()             # =
    LEFT_SQUARE = auto()        # [
    RIGHT_SQUARE = auto()       # ]
    LEFT_BRACES = auto()        # {
    RIGHT_BRACES = auto()       # }
    LEFT_PARENTHESIS = auto()   # (
    RIGHT_PARENTHESIS = auto()  # )
    AND = auto()                # &&
    OR = auto()                 # ||
    LESS_THAN = auto()          # <
    GREATER_THAN = auto()       # >
    LESS_OR_EQUAL = auto()      # <=
    GREATER_OR_EQUAL = auto()   # >=
    NOT_EQUAL = auto()          # !=
    EQUAL_EQUAL = auto()        # ==
    PLUS = auto()               # +
    PLUS_PLUS = auto()          # ++
    MINUS = auto()              # -
    MINUS_MINUS = auto()        # --
    TIMES = auto()              # *
    DIVIDE = auto()             # /
    DOT = auto()                # .
    NOT = auto()                # !
    EOF = auto()                # end of file

    # regular tokens
    ID = auto()
    CHARACTER = auto()
    NUMERAL = auto()
    STRINGVAL = auto()

    # unknown token
    UNKNOWN = auto()


class Rules(Enum):
    P       = auto()
    LDE     = auto()
    DE      = auto()
    DF      = auto()
    DT      = auto()
    T       = auto()
    DC      = auto()
    LI      = auto()
    LP      = auto()
    B       = auto()
    LDV     = auto()
    DV      = auto()
    LS      = auto()
    S       = auto()
    E       = auto()
    LV      = auto()
    L       = auto()
    R       = auto()
    Y       = auto()
    F       = auto()
    LE      = auto()
    ID      = auto()
    TRUE    = auto()
    FALSE   = auto()
    CHR     = auto()
    STR     = auto()
    NUM     = auto()
    PLINHA  = auto()
    M       = auto()
    U       = auto()


reserved_words = {
	'type'		: Words.TYPE,
	'array' 	: Words.ARRAY,
	'of' 		: Words.OF,
	'struct' 	: Words.STRUCT,
	'function' 	: Words.FUNCTION,
	'var' 		: Words.VAR,
	'if' 		: Words.IF,
	'else'		: Words.ELSE,
	'while'		: Words.WHILE,
	'do'		: Words.DO,
	'break'		: Words.BREAK,
	'continue'	: Words.CONTINUE,
	'true'		: Words.TRUE,
	'false'		: Words.FALSE,
	'boolean'	: Words.BOOLEAN,
	'char'		: Words.CHAR,
	'integer'	: Words.INTEGER,
	'string'	: Words.STRING
}

regular_tokens = [
    Words.ID,
    Words.CHARACTER,
    Words.NUMERAL,
    Words.STRINGVAL,
]

symbols = {
	'='	    : Words.EQUALS,
	'['	    : Words.LEFT_SQUARE,
	']'	    : Words.RIGHT_SQUARE,
	'('	    : Words.LEFT_PARENTHESIS,
	')'	    : Words.RIGHT_PARENTHESIS,
	'{'	    : Words.LEFT_BRACES,
	'}'	    : Words.RIGHT_BRACES,
	';'	    : Words.SEMI_COLON,
	':'	    : Words.COLON,
	','	    : Words.COMMA,
	'&&'	: Words.AND,
	'||'	: Words.OR,
	'<'	    : Words.LESS_THAN,
	'<='	: Words.LESS_OR_EQUAL,
	'>'	    : Words.GREATER_THAN,
	'>='	: Words.GREATER_OR_EQUAL,
	'=='	: Words.EQUAL_EQUAL,
	'!='	: Words.NOT_EQUAL,
	'+'	    : Words.PLUS,
	'++'	: Words.PLUS_PLUS,
	'-'	    : Words.MINUS,
	'--'	: Words.MINUS_MINUS,
	'*'	    : Words.TIMES,
	'/'	    : Words.DIVIDE,
	'!'	    : Words.NOT,
	'.'     : Words.DOT
}

ignored_chars = [' ', '\n', '\r', '\t', '\v', '\f']


rule_atr = []
rule_atr.append([1,		2,		1,		1,		1,		1,		1,		1,		1,		1,		9,		7,		4,		5,		3,		8,		5,		3,		4,		2,		1,		2,		1,		5,		3,		1,		1,		1,		5,		7,		7,		5,		7,		1,		4,		2,		2,		3,		3,		1,		3,		3,		3,		3,		3,		3,		1,		3,		3,		1,		3,		3,		1,		1,		2,		2,		2,		2,		3,		4,		2,		2,		1,		1,		1,		1,		1,		3,		1,		3,		4,		1,		1,		1,			1,			1,		1,		1])
rule_atr.append([Rules.P,	Rules.LDE,	Rules.LDE,	Rules.DE,	Rules.DE,	Rules.T,	Rules.T,	Rules.T,	Rules.T,	Rules.T,	Rules.DT,	Rules.DT,	Rules.DT,	Rules.DC,	Rules.DC,	Rules.DF,	Rules.LP,	Rules.LP,	Rules.B,	Rules.LDV,	Rules.LDV,	Rules.LS,	Rules.LS,	Rules.DV,	Rules.LI,	Rules.LI,	Rules.S,	Rules.S,	Rules.U,	Rules.U,	Rules.M,	Rules.M,	Rules.M,	Rules.M,	Rules.M,	Rules.M,	Rules.M,	Rules.E,	Rules.E,	Rules.E,	Rules.L,	Rules.L,	Rules.L,	Rules.L,	Rules.L,	Rules.L,	Rules.L,	Rules.R,	Rules.R,	Rules.R,	Rules.Y,	Rules.Y,	Rules.Y,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.F,	Rules.LE,	Rules.LE,	Rules.LV,	Rules.LV,	Rules.LV,	Rules.ID,	Rules.TRUE,	Rules.FALSE,	Rules.CHR,	Rules.STR,	Rules.NUM])

dic = {
	Words.INTEGER : 1,
	Words.CHAR : 2,
	Words.BOOLEAN : 3,
	Words.STRINGVAL : 4,
	Words.TYPE : 5,
	Words.EQUALS : 6,
	Words.ARRAY : 7,
	Words.LEFT_SQUARE : 8,
	Words.RIGHT_SQUARE : 9,
	Words.OF : 10,
	Words.STRUCT : 11,
	Words.LEFT_BRACES : 12,
	Words.RIGHT_BRACES : 13,
	Words.SEMI_COLON : 14,
	Words.COLON : 15,
	Words.FUNCTION : 16,
	Words.LEFT_PARENTHESIS : 17,
	Words.RIGHT_PARENTHESIS : 18,
	Words.COMMA : 19,
	Words.VAR : 20,
	Words.IF : 21,
	Words.ELSE : 22,
	Words.WHILE : 23,
	Words.DO : 24,
	Words.BREAK : 25,
	Words.CONTINUE : 26,
	Words.AND : 27,
	Words.OR : 28,
	Words.LESS_THAN : 29,
	Words.GREATER_THAN : 30,
	Words.LESS_OR_EQUAL : 31,
	Words.GREATER_OR_EQUAL : 32,
	Words.EQUAL_EQUAL : 33,
	Words.NOT_EQUAL : 34,
	Words.PLUS : 35,
	Words.MINUS : 36,
	Words.TIMES : 37,
	Words.DIVIDE : 38,
	Words.PLUS_PLUS : 39,
	Words.MINUS_MINUS : 40,
	Words.NOT : 41,
	Words.DOT : 42,
	Words.ID : 43,
	Words.TRUE : 44,
	Words.FALSE : 45,
	Words.CHARACTER : 46,
	Words.STRINGVAL : 47,
	Words.NUMERAL : 48,
	Words.EOF : 49,
	Rules.PLINHA : 50,
	Rules.P : 51,
	Rules.LDE : 52,
	Rules.DE : 53,
	Rules.T : 54,
	Rules.DT : 55,
	Rules.DC : 56,
	Rules.DF : 57,
	Rules.LP : 58,
	Rules.B : 59,
	Rules.LDV : 60,
	Rules.LS : 61,
	Rules.DV : 62,
	Rules.LI : 63,
	Rules.S : 64,
	Rules.U : 65,
	Rules.M : 66,
	Rules.E : 67,
	Rules.L : 68,
	Rules.R : 69,
	Rules.Y : 70,
	Rules.F : 71,
	Rules.LE : 72,
	Rules.LV : 73,
	Rules.ID : 74,
	Rules.TRUE : 75,
	Rules.FALSE : 76,
	Rules.CHR : 77,
	Rules.STR : 78,
	Rules.NUM : 79
}


NO_KIND_DEF_=-1
VAR_=0
PARAM_=1
FUNCTION_=2
FIELD_=3
ARRAY_TYPE_=4
STRUCT_TYPE_=5
ALIAS_TYPE_=6
SCALAR_TYPE_=7
UNIVERSAL_=8

def IS_TYPE_KIND(eKind):
    return (eKind==ARRAY_TYPE_ or eKind==STRUCT_TYPE_ or eKind==ALIAS_TYPE_ or eKind==SCALAR_TYPE_)

ERR_REDCL=9
ERR_NO_DECL=10
ERR_TYPE_EXPECTED=11
ERR_BOOL_TYPE_EXPECTED=12
ERR_TYPE_MISMATCH=13
ERR_INVALID_TYPE=14
ERR_KIND_NOT_STRUCT=15
ERR_FIELD_NOT_DECL=16
ERR_KIND_NOT_ARRAY=17
ERR_INVALID_INDEX_TYPE=18
ERR_KIND_NOT_VAR=19
ERR_KIND_NOT_FUNCTION=20
ERR_TOO_MANY_ARG=21
ERR_PARAM_TYPE=22
ERR_TOO_FEW_ARGS=23
ERR_RETURN_TYPE_MISMATCH=24

#Regras
PLINE_P_RULE = 0
P_LDE_RULE = 1
LDE_LDE_RULE = 2
LDE_DE_RULE = 3
DE_DF_RULE = 4
DE_DT_RULE = 5
T_INTEGER_RULE = 6
T_CHAR_RULE  = 7
T_BOOL_RULE = 8
T_STRING_RULE = 9
T_IDU_RULE = 10
DT_ARRAY_RULE = 11
DT_STRUCT_RULE = 12
DT_ALIAS_RULE = 12
DC_DC_RULE = 14
DC_LI_RULE = 15
DF_RULE = 16
LP_LP_RULE = 17
LP_IDD_RULE = 18
#LP_EPSILON_RULE = 
B_LS_RULE = 19
LDV_LDV_RULE = 20
LDV_DV_RULE = 21
LS_LS_RULE = 22
LS_S_RULE = 23
DV_VAR_RULE = 24
LI_COMMA_RULE = 25
LI_IDD_RULE = 26
S_M_RULE = 27
S_U_RULE = 28
#S_RETURN_RULE = 
U_IF_RULE = 29
U_IF_ELSE_U_RULE = 30
M_IF_ELSE_M_RULE = 31
M_WHILE_RULE = 32
M_DO_WHILE_RULE = 33
M_BLOCK_RULE = 34
M_E_SEMICOLON = 35
M_BREAK_RULE = 36
M_CONTINUE_RULE = 37
E_AND_RULE = 38
E_OR_RULE = 39
E_L_RULE = 40
#E_LV_EQUAL_RULE = 
L_LESS_THAN_RULE = 41
L_GREATER_THAN_RULE = 42
L_LESS_EQUAL_RULE = 43
L_GREATER_EQUAL_RULE = 44
L_EQUAL_EQUAL_RULE = 45
L_NOT_EQUAL_RULE = 46
L_R_RULE = 47
R_PLUS_RULE = 48
R_MINUS_RULE = 49
R_Y_RULE = 50
Y_TIMES_RULE = 51
Y_DIVIDE_RULE = 52
Y_F_RULE = 53
F_LV_RULE = 54
F_LEFT_PLUS_PLUS_RULE = 55
F_LEFT_MINUS_MINUS_RULE = 56
F_RIGHT_PLUS_PLUS_RULE = 57
F_RIGHT_MINUS_MINUS_RULE = 58
F_PARENTHESIS_E_RULE = 59
F_IDU_MC_RULE = 60
F_MINUS_F_RULE = 61
F_NOT_F_RULE = 62
F_TRUE_RULE = 63
F_FALSE_RULE = 64
F_CHR_RULE = 65
F_STR_RULE = 66
F_NUM_RULE = 67
LE_LE_RULE = 68
LE_E_RULE = 69
#LE_EPSILON_RULE = 
LV_DOT_RULE = 70
LV_SQUARE_RULE = 71
LV_IDU_RULE = 72
IDD_RULE = 73
IDU_RULE = 74
ID_RULE = 75
TRUE_RULE = 76
FALSE_RULE = 77
CHR_RULE = 78
STR_RULE = 79
NUM_RULE = 80
NB_RULE = 81
MF_RULE = 82
MC_RULE = 83
NF_RULE = 84
MT_RULE = 85
ME_RULE = 86
MW_RULE = 87
#MA_RULE = 


def Error(code):
    hasErr = True
    print("Linha: "+str(lxc.linha)+" - ")
    if (code==ERR_NO_DECL):
        print("Variável não previamente declarada")
    elif (code==ERR_REDCL):
        print("Variável já declarada")
    elif (code==ERR_TYPE_EXPECTED):
        print("Tipo não declarado previamente")
    elif (code==ERR_BOOL_TYPE_EXPECTED):
        print("Tipo boolean é esperado")
    elif (code==ERR_INVALID_TYPE):
        print("Tipo é invalido para a operação realizada")
    elif (code==ERR_TYPE_MISMATCH):
        print("Tipo é invalido para a operação realizada")
    elif (code==ERR_KIND_NOT_STRUCT):
        print("A operação pode ser realizada somente em tipos Struct")
    elif (code==ERR_FIELD_NOT_DECL):
        print("Campo não foi declarado")
    elif (code==ERR_KIND_NOT_ARRAY):
        print("A operação é destinada somente para Array")
    elif (code==ERR_INVALID_INDEX_TYPE):
        print("O índice é inválido para o Array")
    elif(code==ERR_KIND_NOT_VAR):
        print("A operação somente válida para tipo Var")
    elif(code==ERR_KIND_NOT_FUNCTION):
        print("A operação somente válida para tipo Function")
    elif (code==ERR_TOO_FEW_ARGS):
        print("O número de parâmetros é menor do que o especificado")
    elif (code==ERR_TOO_MANY_ARG):
        print("O número de parametros é maior do que o especificado")
    elif (code==ERR_PARAM_TYPE):
        print("O tipo especificado não é válido")
    elif (code==ERR_RETURN_TYPE_MISMATCH):
        print("O tipo de retorno não é compatível com o tipo especificado na função")