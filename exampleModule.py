from random import choice

city = "Strasbourg"
animal = "Cow"
inhabitants = 150000
river = "Rhin"

def test_phrase():
    phrases = [
        "Strasbourg has a beautiful park.",
        "Cows are in my most liked animals.",
        "Sky is blue, but not when there's bad weather.",
        "A Beagle is not a baeggle."
    ]

    index = choice("0123")

    print(phrases[int(index)])

if __name__ == "__main__":          # when calling the function, always put that if statement, otherwise function will run when module is imported
    test_phrase()