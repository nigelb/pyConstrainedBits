# pyConstrainedBits
pyConstrainedBits is a python library to assist making calculations with only the specified number of bits.

# Example
```python
>>> from constrained.bits import Unsigned

>>> uint3_t = Unsigned(3, name="uint3_t")
>>> a = uint3_t(7)
>>> print(a + 2)
1
>> a + 3
Unsigned{Name=uint3_t, Bits=3, Value=2}
```