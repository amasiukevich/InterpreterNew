from enum import Enum, auto

class TokenType(Enum):


    IDENTIFIER = auto()
    COMMENT = auto()        # comment here

    # Logical operators
    AND = auto(),           # &&
    OR = auto(),            # ||
    NOT = auto(),           # !


    # Relational
    ASSIGN = auto(),        # =
    EQUAL = auto(),         # ==
    NOT_EQUAL = auto(),     # !=
    GREATER = auto(),       # >
    GREATER_EQUAL = auto(), # >=
    LESS = auto(),          # <
    LESS_EQUAL = auto(),    # <=
    ACCESS = auto(),        # .



    # Arithmetic operators
    PLUS = auto(),          # +
    MINUS = auto(),         # -
    MULTIPLY = auto(),      # *
    DIVIDE = auto(),        # /
    MODULO = auto(),        # %

    # Symbols
    OPEN_PARENTHESIS = auto(),          # (
    CLOSING_PARENTHESIS = auto(),       # )
    OPEN_BRACKET = auto(),              # [
    CLOSING_BRACKET = auto(),           # ]
    OPEN_CURLY_BRACKET = auto(),        # {
    CLOSING_CURLY_BRACKET = auto(),     # }
    COMMA = auto(),                     # ,
    SEMICOLON = auto(),                 # ;

    # Default keywords
    IF = auto(),                # if
    ELSE = auto(),              # else
    WHILE = auto(),             # while
    FOREACH = auto(),           # foreach
    RETURN = auto(),            # return
    DEFINE = auto(),            # define
    THIS = auto(),              # this
    REFLECT = auto(),           # reflect
    RECURSIVE = auto(),         # recursive (for 'reflect recursive')
    BY_REF = auto(),            # by_ref
    CLASS = auto(),             # class
    IN = auto(),                # in

    # Literals
    NUMERIC_LITERAL = auto(),   # 123 or -123
    STRING_LITERAL = auto(),    # abcde
    BOOL_LITERAL = auto(),      # true, false


    UNKNOWN = auto(),
    EOF = auto()