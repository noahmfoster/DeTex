import os

def gen_image(formula, filename, path = None):
    '''
    "List of options:"
    b <color>       Set the background color."
    B <color>       Set the border color."
    d <dpi>         Set the output resolution to the specified dpi."
    e <environment> Set the environment with [options] and {arguments}."
    f <formula>     The LaTeX formula."
    F <color>       Set the foreground color."
    h               Print this help message."
    H <file>        Insert the content of the specified file in the preamble."
    l <file>        Log file."
    m <margin>      Set the margin."
    o <file>        Specify the output file name."
    O               Optimize the image."
    p <packages>    A colon separated list of LaTeX package names."
    P <padding>     Set the padding."
    s <size>        Set the font size."
    S               Silent mode: don't print image file name."
    v               Show version."
    '''

    if path is None:
        path = os.getcwd()

    os.system(f'pnglatex -f "{formula}" -o {path}/data/{filename}.png -S')