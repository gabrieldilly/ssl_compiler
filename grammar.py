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