# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'
def color_text(text: str, effect: str) -> None:
    """
    This function is used to print text in colour

    :param text: enter the text u want to display
    :param effect: enter the effect name from effects list to apply the effect on it
    :return: none
    """
    color_effect = "{0}{1}{2}".format(effect, text, RESET)
    print(color_effect)

color_text("This text will appear in red", RED)
color_text("the", CYAN)
color_text("Hello, Blue", BLUE)
color_text("Hello, Yellow", YELLOW)
color_text("Hello, Bold", BOLD)
color_text("Hello, Underline", UNDERLINE)
color_text("Hello, Reverse", REVERSE)
color_text("Hello, Black", BLACK)
# print(RED, "This text will appear in red")
# print(GREEN, "This text will be print in green")
# print(MAGENTA, "this text will be print in magenta")
# print(CYAN, "this text will be print in cyan")
# print(BLUE, "This text will be print in blue")
# print(BLUE, BOLD, "This text will be bold and blue.")
