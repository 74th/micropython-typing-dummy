from micropython import const
from collections import namedtuple
def __do_nothing(*args, **kwargs):
    pass

Any = None
NoReturn = None
Tuple = list
Union = list
Optional = list
Callable = list
Literal = list
ClassVar = list
Final = list
Annotated = list
Generic = list
TypeVar = __do_nothing
AnyStr = None
Protocol = int
runtime_checkable = __do_nothing
NamedTuple = namedtuple
NewType = __do_nothing
TypedDict = dict
Dict = dict
List = list
Set = set
FrozenSet = set
DefaultDict = dict
OrderedDict = dict
def cast(typ, val):
    return val
final = const