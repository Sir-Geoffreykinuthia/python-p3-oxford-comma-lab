def oxford_comma(items):
    if len(items) <= 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    else:
        oxford_items = ", ".join(items[:-1])
        return f"{oxford_items}, and {items[-1]}"

