# typing dummy for MicroPython and CircuitPython

This is a typing package dummy for writing code that also includes type hints in MicroPython/CircuitPython.
Please put typing.py in the root directory of your code directory on MCU.

## type alias

The following code causes an error in MicroPython/CircuitPython.

```python
LEDColor = tuple[int, int, int]
```

The following code is a workaround.

```python
from typing import TypeAlias

LEDColor: TypeAlias = "tuple[int, int, int]"
```
