"""
    
    Returns:
        _type_: _description_
"""

# TODO: Fractions with a whole part
# TODO: Fractions queue
# TODO: Result optimisation


class Fraction:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return str(self.a) + "/" + str(self.b)

    def __repr__(self) -> str:
        return str(self.a) + "/" + str(self.b)

    def __eq__(self, o: object) -> bool:
        return self.a == o.a and self.b == o.b

    def add(self, frac2):
        if self.b == frac2.b:
            return Fraction(
                self.a + frac2.a,
                self.b
            )

        return Fraction(
            self.a * frac2.b + frac2.a * self.b,
            self.b * frac2.b
        )

    def sub(self, frac2):
        if self.b == frac2.b:
            return Fraction(
                self.a - frac2.a,
                self.b
            )

        return Fraction(
            self.a * frac2.b - frac2.a * self.b,
            self.b * frac2.b
        )

    def mult(self, frac2):
        return Fraction(
            self.a * frac2.a,
            self.b * frac2.b
        )

    def div(self, frac2):
        return Fraction(
            self.a * frac2.b,
            self.b * frac2.a
        )


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage: python " + sys.argv[0] + " a/b {+|-|*|/} c/d")
        exit(1)

    f1a = list(map(int, sys.argv[1].split("/")))
    f2a = list(map(int, sys.argv[3].split("/")))
    op = sys.argv[2]

    f1 = Fraction(f1a[0], f1a[1])
    f2 = Fraction(f2a[0], f2a[1])

    if op not in ['+', '-', '*', '/']:
        print("Operation must be one of: + - * /")
        exit(1)

    if op == "+":
        print(f1.add(f2))
    elif op == "-":
        print(f1.sub(f2))
    elif op == "*":
        print(f1.mult(f2))
    elif op == "/":
        print(f1.div(f2))
