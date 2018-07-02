#! /usr/bin/env python

from models import schnakenberg
from model import Model
from tools.tools import greek, index_to_str

array_model = [
    {
        "name": "Schnakenberg",
        "class": schnakenberg.Schnakenberg
    },
    {
        "name": "Thomas",
        "class": None
    }
]


def model_selection():

    res_ok = False
    model_choice = 0
    while not res_ok:
        for i in range(len(array_model)):
            print(str(i) + " - " + array_model[i]["name"])

        model_choice = int(float(input("Choose your mode : ")))

        res_ok = model_choice in range(len(array_model))
        if not res_ok:
            print("\nYou need to enter the number of the mode.")

    return array_model[model_choice]


def main():
    selected_model = model_selection()

    print(selected_model["class"].eq_to_string())

    a = selected_model["class"]()
    a.create_file()


def main_test():
    model_choice = array_model[0]
    gamma_0 = 0
    gamma_f = 10
    n = 5
    a = model_choice["class"](gamma_0, gamma_f, n, "1", "2", "3")
    a.create_file()


main_test()
#main()
