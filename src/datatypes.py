"""
Module containing all datatypes used within the compiler.
"""
from typing import NamedTuple, Any, Dict, Tuple, List
from enum import Enum, auto
import decimal


PreprocessorSourceRemapping = Dict[int, List[Tuple[int, int]]]


class SourceLocation(NamedTuple):
    """
    Represents a pair of start and end locations for the lexer token/ast node.
    """
    line_start: int
    char_start: int
    line_end: int
    char_end: int


class RockstarError(Exception):
    """
    Exception with location data.
    """
    location: SourceLocation

    def __init__(self, message: str, location: SourceLocation) -> None:
        super().__init__(message)

        self.location = location


class PreprocessorError(RockstarError):
    """
    Error that occurred within the preprocessor.
    """
    pass


class LexerError(RockstarError):
    """
    Error that occurred within the parser.
    """
    pass


class ParserError(RockstarError):
    """
    Error that occurred within the parser.
    """
    pass


class RuntimeTypeError(RockstarError):
    """
    Type error that occurred during runtime.
    """
    pass


class RuntimeArithmeticError(RockstarError):
    """
    Arithmetic error that occurred during runtime.
    """
    pass


class RuntimeComparisonError(RockstarError):
    """
    Comparison error that occurred during runtime.
    """
    pass


class Number(decimal.Decimal):
    """
    A rockstar compliant number type
    """
    pass


class InvalidNumber(decimal.InvalidOperation):
    """
    Number was constructed with a invalid number string.
    """
    pass


class TokenType(Enum):
    """
    Indicates which type the current token is.
    """
    EOF = auto()                  # End of token stream
    Newline = auto()              # `\n`

    Mysterious = auto()           # `mysterious`
    Null = auto()                 # `null/nothing/nowhere/nobody/gone/empty`
    BooleanTrue = auto()          # `true/right/yes/ok`
    BooleanFalse = auto()         # `false/wrong/no/lies`
    Number = auto()               # `1234567890`
    String = auto()               # `"Hello"`
    Pronoun = auto()              # `it/he/she/him/her/they/them/ze/hir/zie/zir/xe/xem/ve/ver`

    Word = auto()                 # Any word that isn`t a keyword

    ReservedCommonVar = auto()    # `a/an/the/my/your`

    ReservedIf = auto()           # `if`
    ReservedElse = auto()         # `else`
    ReservedWhile = auto()        # `while`
    ReservedUntil = auto()        # `until`

    ReservedTakes = auto()        # `Func takes Val and Val2` (takes)
    ReservedAnd = auto()          # `Func takes Val and Val2` (and)
    ReservedBuild = auto()        # `build Val up` (build)
    ReservedUp = auto()           # `build Val up` (up)
    ReservedKnock = auto()        # `knock Val down` (knock)
    ReservedDown = auto()         # `knock Val down` (down)
    ReservedBreak = auto()        # `break it down`
    ReservedContinue = auto()     # `continue` or `take it to the top`
    ReservedPut = auto()          # `put Val into Val2` (put)
    ReservedInto = auto()         # `put Val into Val2` (into)
    ReservedListen = auto()       # `listen to Val` (listen to)
    ReservedSay = auto()          # `say/shout/whisper/scream Val` (say)
    ReservedReturn = auto()       # `give back Val` (give back)

    ReservedSays = auto()         # `Var says hi`
    ReservedAssignment = auto()   # `Var is/was/were/`s mysterious`

    ReservedIs = auto()           # `Val is Val2` (is)
    ReservedAs = auto()           # `Val is as great as` (as)
    ReservedOr = auto()           # `Val or Val2` (or)
    ReservedNor = auto()          # `Val nor Val2` (nor)
    ReservedGTE = auto()          # `higher/greater/bigger/stronger`
    ReservedLTE = auto()          # `lower/less/smaller/weaker`
    ReservedGT = auto()           # `high/great/big/strong`
    ReservedLS = auto()           # `low/little/small/weak`
    ReservedNEQ = auto()          # `aint/ain't`
    ReservedNegation = auto()     # `not`
    ReservedPlus = auto()         # `plus/with`
    ReservedMinus = auto()        # `minus/without`
    ReservedMultiply = auto()     # `times/of`
    ReservedDivide = auto()       # `over`


class Token(NamedTuple):
    """
    Lexer token. Data stores the "value" associated with the token. If there isn't a value associated with the
    token, it holds a string of the original text that the token represents. This is to allow poetic literals to work.
    """
    type: TokenType
    data: Any
    location: SourceLocation


class TokenStream(list):
    """
    List of tokens.
    """
    pass