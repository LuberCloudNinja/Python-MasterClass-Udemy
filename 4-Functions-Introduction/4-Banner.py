def banner_text(text=" ", screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError(f"String{text} is larger than specified width {screen_width}", 60)

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that is to laugh and smile and dance and sign", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps", 60)
banner_text("Don't be silly chumps", 60)
banner_text("just purse your lips and whistle - that's the thing", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)
