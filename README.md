# typing dummy for MicroPython and CircuitPython

You want to write code that includes type hints in MicroPython/CircuitPython as well.

This is a dummy of the typing package for MicroPython/CircuitPython.
Please put typing.py in the root directory of your microcontroller.

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
