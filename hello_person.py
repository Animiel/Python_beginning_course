# if command line arguments are needed (in terminal)
# if this is added, can't run it like normally as it needs an argument in the terminal so use : py filename.py -argument argValue

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "French": "Bonjour",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name} !"
    print(msg)

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personnal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar = "name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "French", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)