import numpy as np


def custom_log_formatter(x, pos=None):
    """
    Custom formatter for log scale tick labels.
    Formats labels as {}^{1-}10 for negative exponents and 10^{exp} for positive exponents.
    """
    if x == 0:
        return "0"  # Avoid log(0) issues
    
    exponent = int(np.log10(x)) # Get log base-10 exponent

    if exponent < 0:
        return rf"$^{{{abs(exponent)}\!\!-\!\!}}10$"  # Example: 10^{1-}, 10^{2-}
    else:
        return rf"$^{{{exponent}}}10$"  # Example: 10^1, 10^2


def custom_formatter(x, pos=None):
    if x < 0:
        return f'{abs(x):.2f}-'  # Format to 2 decimal places
    return f'{x:.2f}'  # Format to 2 decimal places

def pi_formatter(x):
    """Formats axis labels as multiples of π using fractions where necessary."""
    from fractions import Fraction
    sign = ""
    if x<0: sign = "-"
    
    
    pi_fraction = Fraction(x / np.pi).limit_denominator()
    
    if pi_fraction.denominator == 1:  # If it's an integer
        if pi_fraction.numerator == 0:
            return '0'
        elif pi_fraction.numerator == 1:
            return 'ط'
        elif pi_fraction.numerator == -1:
            return 'ط-'
        else:
            text = "\u0637" + str(abs(pi_fraction.numerator)) + sign
            return text
    return f'ط{pi_fraction.denominator}\\{abs(pi_fraction.numerator)}'+ sign

def generate_tickvals_and_text(data, num_ticks=4, use_pi_format=False, minmax = None):
    """Generates evenly spaced tick values and formatted tick text for an axis."""
    
    if minmax == None:
        min_val, max_val = np.min(data), np.max(data)
    else:
        min_val = minmax[0]
        max_val = minmax[1]
    
    tickvals = np.linspace(min_val, max_val, num_ticks).tolist()
    
    if use_pi_format:
        ticktext = [pi_formatter(x) for x in tickvals]
    else:
        ticktext = [custom_formatter(x) for x in tickvals]
    
    return tickvals, ticktext
