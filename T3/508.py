with open("508_input.txt", "w") as f:
    x = "lorem ipsum dolor sit amet, consectetur adip"
    x=x.split()
    x = [i + "\n" for i in x]
    print(x)
    f.writelines(x)

open("508_output.txt", "w").write(open("508_input.txt").read().upper())
