from sympy import sympify, symbols, Matrix, diff

class NewtonMethod:
    @staticmethod
    def Jacobian(funcs, vars):
        ''' Jacobian function for calculating gradient and hesian '''
        if len(funcs) == 1:
            return Matrix([diff(funcs[0], v) for v in vars])

        return Matrix([[diff(f, v) for v in vars] for f in funcs])

    def gradient(self):
        return NewtonMethod.Jacobian(Matrix([self.f]), self.var_symbols)

    def hessian(self):
        g_f = self.gradient()
        return NewtonMethod.Jacobian(g_f, self.var_symbols), g_f

    def __init__(self, func_expression: str, independent_variables=('x', 'y')) -> None:
        self.var_symbols = symbols(independent_variables)
        self.f = sympify(func_expression)

    def get_func(self):
        d2f, df = self.hessian()
        return self.f, df, d2f

    def list_vars(self):
        return ', '.join([str(v) for v in self.var_symbols])

    @staticmethod
    def F_ValueAt(F, X, vars):
        F_X = F.subs(vars[0], X[0])
        for idx, v in enumerate(vars[1:], start=1):
            F_X = F_X.subs(v, X[idx])
        return F_X

    def optimize(self, X0, min_error=1e-6, max_iterations=1000) -> list:
        '''perform Newton method and get all iterations '''
        X = []
        X_i = Matrix(X0)
        Hessian, Gradient = self.hessian()
        dX = Hessian.inv() * -Gradient
        for i in range(max_iterations):
            gradient = dX.subs(dict(zip(self.var_symbols, X_i)))
            dX_i = dX.subs(self.var_symbols[0], X_i[0])
            for idx, v in enumerate(self.var_symbols[1:], start=1):
                dX_i = dX_i.subs(v, X_i[idx])
            dX_i = NewtonMethod.F_ValueAt(dX, X_i, self.var_symbols)
            for i, dx in enumerate(dX_i):
                X_i[i] += dx
            err = gradient.norm()
            X_i.stringify = ', '.join([str(x) for x in X_i])

            X.append({'value': X_i, 'error': err})
            if err < min_error:
                break
        return X
