def banner_text(text: str = " ", width: int = 80) -> None:
    """
    This function is used to print the bannner with the help of two paramenters(string, int)
    :param text: Enter the text text which needs to be printed on the banner
    :param width: the size of the banner
    :return: it returns no value
    :raises ValueError: if supplied with a string which is too long to fit
    """
    screen_width = width
    if len(text) > screen_width -4:
        raise ValueError("String {0} is larger than the specified size {1}"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)
print(input.__doc__)
print('*'*90)
print(banner_text.__doc__)
print('*'*90)
banner_text("*", 80)
banner_text("Always look on the bright side of life...", 80)
banner_text("If life seems jolly rotten,", 80)
banner_text("There's something you've forgotten!", 80)
banner_text("And that's to laugh and smile and dance and sing,", 80)
banner_text(" ", 80)
banner_text("When you're feeling in the dumps,", 80)
banner_text("Don't be silly chumps,", 80)
banner_text("Just purse your lips and whistle - that's the thing!", 80)
banner_text("And... always look on the bright side of life...", 80)
banner_text("*", 80)