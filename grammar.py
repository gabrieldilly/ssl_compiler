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
