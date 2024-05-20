def main():
    dollars = dollars_to_float(input("Cost of meal? "))
    percent = percent_to_float(input("Percentage to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dnew = d.replace("$", "")
    return float(dnew)


def percent_to_float(p):
    pnew = float(p.replace("%", ""))/ 100
    return (pnew)

main()

