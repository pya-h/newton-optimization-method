from newton_method_xd import NewtonMethod

if __name__ == '__main__':
    try:
        print('Enter the information needed below:\n\t[For questions that have default answers, press enter to use default value or enter your desired answer.]')
        str_symbols = (input('Enter the LIST of independant variables [default: x y]') or 'x y')
        symbols = str_symbols.split()
        f_expression = input(f'Enter the function as f({str_symbols}): [default: sin(x) + cos(y)]') or 'sin(x) + cos(y)'
        newton = NewtonMethod(f_expression, symbols)
        initial_guess = [float(x0) for x0 in (input(f'Enter the initial guess [default=1 1]:') or '1 1').split()]
        min_err = float(input('Enter the minimum where the algorythm should stop there: [default=0.000001]') or '1e-06')
        max_iterations = int(input('Enter the maximum number of iterations, if the newton method ' +
                            'doesn\'t reach the desired error, algorythm will stop at this iteration [default: 100]: ') or '100')
        X = newton.optimize(X0=initial_guess, min_error=min_err, max_iterations=max_iterations)
        f, df, d2f = newton.get_func()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        list_of_variables = newton.list_vars()
        print(f'\tIter\t\t\t\t{list_of_variables}\t\t\t\tf({list_of_variables})\t\t\t\t\tError')
        f_Xi = None
        Xi = None
        for i, x in enumerate(X, start=1):
            Xi, err = x['value'], float(x['error'])
            f_Xi = float(NewtonMethod.F_ValueAt(f, Xi, newton.var_symbols))
            print(f"\t{i}\t\t\t{Xi.stringify}\t\t\t{f_Xi:f}\t\t\t\t{err:f}")

        print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'Final Optimal Point:\n\t{list_of_variables} =', Xi.stringify, f'\tf({list_of_variables}) = ', f_Xi)
    except Exception as ex:
        print('Cannot apply the method! its usually because you entered one or more input in wrong format!\n\tActual Cause: ', ex)
