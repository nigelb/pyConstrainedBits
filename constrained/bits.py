# pyConstrainedBits is a python library to assist making calculations with only
# the specified number of bits.
#
# Copyright (c) 2023 nigelb
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class Constrained:
    def __init__(self, bits, value=0, name=""):
        self.bits = bits
        self.name = name
        self.mask = int('1' * bits, 2)
        self.value = value & self.mask


class Unsigned(Constrained):

    def __init__(self, bits, value=0, name=""):
        super().__init__(bits, value, name)
        if value < 0:
            raise Exception("Invalid Value")

    def __call__(self, value):
        return Unsigned(self.bits, value, self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        _name = "Unsigned"
        if len(self.name) > 0:
            _name = self.name
        return "{name}{{Bits={bits}, Value={value}}}".format(name=_name, bits=self.bits, value=self.value)

    def __eq__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        return self.value == b.value

    def __add__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = self.value + b.value
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __sub__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = self.value - b.value
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __mul__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = self.value * b.value
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __truediv__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = int(self.value / b.value)
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __floordiv__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = self.value // b.value
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __pow__(self, power, modulo=None):
        if isinstance(power, Constrained):
            power = power.value
        if modulo is not None and isinstance(modulo, Constrained):
            modulo = modulo.value
        res = self.value ** power
        if modulo is not None:
            res %= modulo
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __lshift__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = self.value << b.value
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __rshift__(self, b):
        if not isinstance(b, Constrained):
            b = Unsigned(self.bits, b, self.name)
        res = self.value >> b.value
        res &= self.mask
        return Unsigned(self.bits, res, self.name)

    def __abs__(self):
        return self





