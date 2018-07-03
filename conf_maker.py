#!/usr/bin/env python

# import the models
from models import schnakenberg

# Append the models to the proposed list
array_model = [
    {
        "name": "Schnakenberg",
        "class": schnakenberg.Schnakenberg
    }
]


def model_selection():
    """
    Use to ask the user what kind of model he want to use.
    :return: the python dict of the model define in "array_model"
    """

    # init variables
    res_ok = False
    model_choice = 0

    # While the user didn't enter a valid answer
    while not res_ok:
        # We display all the possibilities
        for i in range(len(array_model)):
            print(str(i) + " - " + array_model[i]["name"])

        # We get the user choice
        model_choice = int(float(input("Choose your model : ")))

        # We check that the input of the user is valid
        res_ok = model_choice in range(len(array_model))

        # If not, we ask him to enter a valid data.
        if not res_ok:
            print("\nYou need to enter the number of the model.")

    # We return the dict
    return array_model[model_choice]


def main():
    """
    The main function that call the different steps.
    :return: None
    """

    # We get the user model choice.
    selected_model = model_selection()

    # We print equations to show the different variables to fill.
    print(selected_model["class"].eq_to_string())

    # We create an object from the model chosen
    model_obj = selected_model["class"]()

    # We write the output to the file
    model_obj.write_file()

#main()
