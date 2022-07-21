def mprint(string: str):
    spl = string.split("\n")
    print("\n".join([ line.strip() for i, line in enumerate(spl) if i > 0 and i < len(spl)-1 ]))