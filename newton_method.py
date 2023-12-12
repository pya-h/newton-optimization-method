from sympy import sympify, diff, symbols

class NewtonMethod:
    '''This class will do all the work conserning newton method optimization and its calculations'''

    @staticmethod
    def D(f):
        '''return the derivative of f'''
        return diff(f)
    
    def __init__(self, func_expression: str, independant_variable='x') -> None:
        self.var_symbol = symbols(independant_variable)
        self.f_x = sympify(func_expression)

    def get_func(self):
        '''return f and its first and second derivatives'''
        df = NewtonMethod.D(self.f_x)
        return self.f_x, df, NewtonMethod.D(df)
        
    def optimize(self, x0, min_error=1e-6, max_iterations=100) -> list:
        '''perform newton method and get all iterations'''
        df = NewtonMethod.D(self.f_x)
        d2f = NewtonMethod.D(df)
        X = []
        x_i = x0
        for i in range(max_iterations):
            gradient, hessian = df.subs(self.var_symbol, x_i), d2f.subs(self.var_symbol, x_i)
            dx = -gradient / hessian
            x_i += dx
            err = abs(gradient)
            X.append({'value': x_i, 'error': err})
            if err < min_error:
                break
        return X