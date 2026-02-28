import math

class ConvexFunction:
    def __init__(self, func):
        self.func = func

    def evaluate(self, x: float) -> float:
        return self.func(x)

class Solution:
    def __init__(self, func: ConvexFunction):
        self.func = func

    def minimize(self, a: float, b: float, eps: float) -> float:
        while (b - a) > eps:
            # Calculate two midpoints that divide the interval into three equal parts.
            m1 = a + (b - a) / 3
            m2 = b - (b - a) / 3

            f1 = self.func.evaluate(m1)
            f2 = self.func.evaluate(m2)

            if f1 < f2:
                b = m2
            else:
                a = m1
        return (a + b) / 2

def test1():
    print("===== Test 1 =====")
    func = ConvexFunction(lambda x: (x - 3)**2 + 5)
    solution = Solution(func)
    result = solution.minimize(-10, 10, 0.01)
    print(f"Result: {result}")  # Expected: ~3.0

def test2():
    print("===== Test 2 =====")
    func = ConvexFunction(lambda x: x**2)
    solution = Solution(func)
    result = solution.minimize(-100, 50, 0.001)
    print(f"Result: {result}")  # Expected: ~0.0

def test3():
    print("===== Test 3 =====")
    func = ConvexFunction(lambda x: abs(x - 123.456))
    solution = Solution(func)
    result = solution.minimize(0, 1000, 0.0001)
    print(f"Result: {result}")  # Expected: ~123.456

def test4():
    print("===== Test 4 =====")
    func = ConvexFunction(lambda x: (x - 987.654)**2)
    solution = Solution(func)
    result = solution.minimize(-1e9, 1e9, 1e-4)
    print(f"Result: {result}")  # Expected: ~987.654

def test5():
    print("===== Test 5 =====")
    func = ConvexFunction(lambda x: math.exp(x) - 2 * x)
    solution = Solution(func)
    result = solution.minimize(0, 2, 1e-4)
    print(f"Result: {result}")  # Expected: ~0.693

def test6():
    print("===== Test 6 =====")
    func = ConvexFunction(lambda x: x)
    solution = Solution(func)
    result = solution.minimize(0, 100, 1e-4)
    print(f"Result: {result}")  # Expected: ~0.0
    print(round(result, 4))

def test7():
    print("===== Test 7 =====")
    func = ConvexFunction(lambda x: (x - 1)**2)
    solution = Solution(func)
    result = solution.minimize(0.9999, 1.0001, 1e-4)
    print(f"Result: {result}")  # Expected: ~1.0

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    test6()
    # test7()