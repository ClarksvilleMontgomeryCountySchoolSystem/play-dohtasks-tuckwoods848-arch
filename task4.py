def main():
    color1 = "black"
    color2 = "white"
    print(f"1) Roll a ball using {color1} for body.\n")
    choice1 = input("hot dog or round like a body? ")
    if choice1 == "hotdog":
        print("2) Stretch it out.\n")
    else:
        print("2) Keep it round.\n")
    print(f"3) Roll a smaller ball using {color1} for the head.\n ")
    print("4) Attach the head to the body.\n")
    choice2 = input("standing up for a flopped down? ")
    if choice2 == "standing up":
        print(f"5) Attach two pointed peices using {color2} upright.\n")
    else:
        print(f"5) Attach two pieces using {color2} hanging downward.\n")
    print(f"6) Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n")
    print('7) Name this creation: "dog" ')


if __name__ == "__main__":
    main()
