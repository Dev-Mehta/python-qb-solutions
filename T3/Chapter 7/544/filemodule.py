def copyfile(f1: str, f2: str):
    with open(f1) as f:
        lines = f.readlines()
        lines = [line.split('#')[0].strip() for line in lines]
        lines = [line for line in lines if line != '']
        lines = [line.split("\n")[0] + "\n" for line in lines]
        with open(f2, "w") as fo:
            fo.writelines(lines)