# typing dummy for MicroPython and CircuitPython

You want to write code that includes type hints in MicroPython/CircuitPython as well.

This is a dummy of the typing package for MicroPython/CircuitPython.
Please put typing.py in the root directory of your microcontroller.

## workarounds

### type alias

#### error code

```python
LEDColor = tuple[int, int, int]
```

#### workaround code

```python
from typing import TypeAlias

LEDColor: TypeAlias = "tuple[int, int, int]"
```

### cast

#### error code

```python
LEDColors = cast(tuple[int, int, int], config.led_colors)
```

#### workaround code

```python
LEDColors = cast("tuple[int, int, int]", config.led_colors)
```
