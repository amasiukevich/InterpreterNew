from src.utils.token_type import TokenType
from .and_oper import AndOperator
from .data_access_oper import DataAccessOperator
from .divide_oper import DivideOperator
from .equal_oper import EqualOperator
from .greater_equal_oper import GreaterEqualOperator
from .greater_oper import GreaterOperator
from .less_equal_oper import LessEqualOperator
from .less_oper import LessOperator
from .minus_oper import MinusOperator
from .modulo_oper import ModuloOperator
from .multiply_oper import MultiplyOperator
from .negative_oper import NegativeOperator
from .not_oper import NotOperator
from .or_operator import OrOperator
from .plus_oper import PlusOperator


class OperatorMapper:

    TOKEN_TYPE_TO_OPER = {
        TokenType.AND: AndOperator(),
        TokenType.ACCESS: DataAccessOperator(),
        TokenType.DIVIDE: DivideOperator(),
        TokenType.EQUAL: EqualOperator(),
        TokenType.GREATER_EQUAL: GreaterEqualOperator(),
        TokenType.GREATER: GreaterOperator(),
        TokenType.LESS_EQUAL: LessEqualOperator(),
        TokenType.LESS: LessOperator(),
        TokenType.MINUS: MinusOperator(),
        TokenType.MODULO: ModuloOperator(),
        TokenType.MULTIPLY: MultiplyOperator(),
        TokenType.MINUS: NegativeOperator(),
        TokenType.NOT: NotOperator(),
        TokenType.OR: OrOperator(),
        TokenType.PLUS: PlusOperator()
    }