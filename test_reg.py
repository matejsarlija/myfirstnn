import re

pattern = r'\\\\([^ ]+)'

str = r"(see Davison and Hinkley 1997, equ. 5.6 p. 194): ( 2 ^ ( 1 / 2 ) , 2 ^ ( / 2 ) ) }-\\theta ^,2}-\\theta ^)} where ( 1 / 2 ) \\theta ^ denotes the 1 / 2 1-\\alpha /2 percentile of the bootstrapped coefficients \\theta ^ .Percentile bootstrap. The percentile bootstrap proceeds in a similar way to  (note the inversion of the left and right quantiles): ( ( / 2 ) , ( 1 / 2 ) ) ^,\\theta ^)} where ( 1 / 2 ) \\theta _^ denotes the 1 / 2 1-\\alpha /2 percentile of the bootstrapped coefficients \\theta ^ ."

def remove_double_backslash_tokens(text):
    return re.sub(pattern, '', text)

new_str = re.sub(pattern, '', str)


print(new_str)
