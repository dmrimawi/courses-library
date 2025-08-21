def convert(cel):
    return (9/5 * cel) + 32

cel = float(input("Enter the tempreture: "))
feh = convert(cel)

with open("out.txt", "w") as f:
    f.write(f"The temp {cel} C in fehr {feh}")
    f.close()
