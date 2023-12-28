import math

class Equation:
    def __init__(self, koeffs=None):
        self.A = 0.0
        self.B = 0.0
        self.C = 0.0
        self.solutions = []
        if koeffs:
            self.set_koeffs(koeffs)

    def set_koeffs(self, koeffs):
        if len(koeffs) == 3:
            self.A, self.B, self.C = koeffs

    def get_roots(self):
        a = self.A
        b = self.B
        c = self.C
        result = []
        D = b * b - 4 * a * c
        if D == 0.0:
            root = math.sqrt(-b / (2.0 * a))
            if root == 0.0:
                result.append(abs(root))
            else:
                result.append(root)
                result.append(-root)
        elif D > 0.0:
            sqD = math.sqrt(D)
            r1 = (-b + sqD) / (2.0 * a)
            r2 = (-b - sqD) / (2.0 * a)
            if r1 == 0.0:
                result.append(r1)
            if r2 == 0.0 and r1 != 0.0:
                result.append(r2)
            if r1 > 0.0:
                root1 = math.sqrt(r1)
                result.append(root1)
                result.append(-root1)
            if r2 > 0.0:
                root2 = math.sqrt(r2)
                result.append(root2)
                result.append(-root2)
        return result

def main():
    koeffs = []
    for i in range(1, 4):
        while True:
            try:
                koeff_str = input('Введите коэффициент {}: '.format(chr(64 + i)))
                koeff = float(koeff_str)
                koeffs.append(koeff)
                break
            except ValueError:
                print('Введено неверное значение. Попробуйте снова.\n')
    eq = Equation(koeffs)
    roots = eq.get_roots()
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
