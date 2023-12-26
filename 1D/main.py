from newton_method import NewtonMethod

if __name__ == '__main__':
    try:
        print('Enter the information needed below:\n\t[For questions that have default answers, press enter to use default value or enter your desired answer.]')
        symbol = input('Enter the symbol of independant variable [default: x]') or 'x'
        f_expression = input(f'Enter the function as f({symbol}): ')
        newton = NewtonMethod(f_expression, symbol)
        initial_guess = float(input(f'Enter the initial guess({symbol}0) [default=0]:') or '0')
        min_err = float(input('Enter the minimum where the algorythm should stop there: [default=0.000001]') or '1e-06')
        max_iterations = int(input('Enter the maximum number of iterations, if the newton method ' +
                            'doesn\'t reach the desired error, algorythm will stop at this iteration [default: 100]: ') or '100')
        X = newton.optimize(x0=initial_guess, min_error=min_err, max_iterations=max_iterations)
        f, df, d2f = newton.get_func()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'\tIter\t\t\tXi\t\t\t\tf({symbol}i)\t\t\t\t\tError')
        for i, x in enumerate(X, start=1):
            xi, err = float(x['value']), float(x['error'])
            f_xi = float(f.subs(newton.var_symbol, xi))
            print(f"\t{i}\t\t\t{xi:f}\t\t\t{f_xi:f}\t\t\t\t{err:f}")
            
        print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'Final Optimal Point:\n\t{symbol} =', X[-1]['value'], f'\tf({newton.var_symbol}) = ', f.subs(newton.var_symbol, X[-1]['value']), "\tError = ", X[-1]['error'])
    except Exception as ex:
        print('Cannot apply the method! its usually because you entered one or more input in wrong format!\n\tActual Cause: ', ex)