from doctest import testmod


class Integer:
    """
    仅使用与或非运算实现整数加法
    >>> Integer(1) + Integer(1)
    Integer(2)

    >>> Integer(10) + Integer(30)
    Integer(40)
    """

    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other):
        bn1 = bin(self.value)[2:].zfill(8)
        bn2 = bin(other.value)[2:].zfill(8)
        s = 0
        c = 0
        ss = []
        for n in range(8):
            s, c = full_add(int(bn1[-(n+1)]), int(bn2[-(n+1)]), c)
            ss.insert(0, s)
        bn_result = ''.join(str(x) for x in ss)


        return Integer(int(bn_result,2))

    def __repr__(self) -> str:
        return f"Integer({self.value})"

def full_add(bit1: int, bit2: int, ci: int):
    """全加器
    >>> full_add(0, 0, 0)
    (0, 0)

    >>> full_add(0, 1, 0)
    (1, 0)

    >>> full_add(1, 0, 0)
    (1, 0)

    >>> full_add(1, 1, 0)
    (0, 1)

    >>> full_add(0, 0, 1)
    (1, 0)

    >>> full_add(0, 1, 1)
    (0, 1)

    >>> full_add(1, 0, 1)
    (0, 1)

    >>> full_add(1, 1, 1)
    (1, 1)
    """
    s1, c1 = half_add(bit1, bit2)
    s, c2 = half_add(s1, ci)
    co = int(c2 or c1) 

    return s, co


def half_add(bit1: int, bit2: int):
    """半加器
    >>> half_add(0, 0)
    (0, 0)

    >>> half_add(0, 1)
    (1, 0)

    >>> half_add(1, 0)
    (1, 0)

    >>> half_add(1, 1)
    (0, 1)
    """

    return bit_sum(bit1, bit2), bit_ci(bit1, bit2)


def bit_sum(bit1: int, bit2: int):
    """
    >>> bit_sum(0, 0)
    0

    >>> bit_sum(0, 1)
    1

    >>> bit_sum(1, 0)
    1

    >>> bit_sum(1, 1)
    0
    """
    return int((bit1 or bit2) and not (bit1 and bit2))

def bit_ci(bit1: int, bit2: int):
    """
    >>> bit_ci(0, 0)
    0

    >>> bit_ci(0, 1)
    0

    >>> bit_ci(1, 0)
    0

    >>> bit_ci(1, 1)
    1

    """
    return int(bit1 and bit2)

if __name__ == "__main__":
    testmod()