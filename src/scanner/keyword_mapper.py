from ..utils.token_type import TokenType

class KeywordMapper():

    KEYWORD_MAP = {
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'while': TokenType.WHILE,
        'foreach': TokenType.FOREACH,
        'return': TokenType.RETURN,
        'define': TokenType.DEFINE,
        'this': TokenType.THIS,
        'reflect': TokenType.REFLECT,
        'recursive': TokenType.RECURSIVE,
        'by_ref': TokenType.BY_REF,
        'class': TokenType.CLASS,
        'true': TokenType.BOOL_LITERAL,
        'false': TokenType.BOOL_LITERAL
    }

    SINGLE_CHAR_MAP = {
        "(": TokenType.OPEN_PARENTHESIS,
        ")": TokenType.CLOSING_PARENTHESIS,
        "[": TokenType.OPEN_BRACKET,
        "]": TokenType.CLOSING_BRACKET,
        "{": TokenType.OPEN_CURLY_BRACKET,
        "}": TokenType.CLOSING_CURLY_BRACKET,
        ",": TokenType.COMMA,
        ".": TokenType.ACCESS,
        ";": TokenType.SEMICOLON,
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "*": TokenType.MULTIPLY,
        "/": TokenType.DIVIDE,
        "%": TokenType.MODULO
    }