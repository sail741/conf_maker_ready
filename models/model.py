import re

from tools.tools import greek


class Model:
    """
    The abstract class to make models

    All models share :
    - an output file
    - du : one of the function
    - dv : the other function
    - a list of fixed attributes that don't change
    - a list of bead
    - gamma_0 : the initial gamma
    - gamma_f : the max gamma
    - n : how many steps between gamma_0 and gamma_f

    """

    output_file = "output.conf"

    du = None
    dv = None

    fixed_attributes = {}
    beads = []

    gamma_0 = ""
    gamma_f = ""
    n = ""

    def __init__(self, gamma_0, gamma_f, n):
        """
        init the base params
        """
        self.gamma_0 = gamma_0
        self.gamma_f = gamma_f
        self.n = n

    @classmethod
    def eq_to_string(cls):
        """
        :return: Return the equations of the model as string (to display all the variables to fill by the user)
        """
        return "du/dt = {0}\ndv/dt = {1}".format(cls.du, cls.dv)

    def get_step(self):
        """
        Get the step used from gamma_0 to gamma_f.
        We just do (gamma_f - gamma_0) / n
        If we don't even have 1 step, we just put the step to the difference + 1 to have 1 loop.
        :return: the step as float
        """
        res = (self.gamma_f - self.gamma_0) / self.n
        if res == 0:
            return self.gamma_f - self.gamma_0 + 1
        return res

    def setup(self):
        """
        Setup the model by asking for every parameters :
        - common variables
        - spec variables
        - beads
        :return: None
        """
        self.__ask_for_common()
        self.__ask_for_spec()
        self.__ask_for_bead()

    def __ask_for_common(self):
        """
        Ask the common attributes to the user:
        - gamma_0
        - gamma_f
        - n
        :return:
        """
        while self.gamma_0 is None or not bool(re.search('^-?[0-9]+$', str(self.gamma_0))):
            self.gamma_0 = int(float(input(greek["gamma"] + "_0 : ")))
        while self.gamma_f is None or not bool(re.search('^-?[0-9]+$', str(self.gamma_f))):
            self.gamma_f = int(float(input(greek["gamma"] + "_f : ")))
        while self.n is None or not bool(re.search('^-?[0-9]+$', str(self.n))):
            self.n = int(float(input("N : ")))

    def __ask_for_spec(self):
        """
        Ask the spec attributes to the user: for each attributes added to the array, we ask it.
        :return:
        """
        for att in self.fixed_attributes:
            while att["value"] == "" or not bool(re.search('^-?[0-9]+$', att["value"])):
                att["value"] = input(att["display"] + " : ")

    def __ask_for_bead(self):
        """
        Ask the beads to the user: while he want to add bead, he can.
        When he want to stop, he need to answer "n" at the question.
        :return:
        """
        is_add_bead = ""
        cpt = 0

        while True:
            while is_add_bead not in ["y", "n"]:
                is_add_bead = input("Bead : add one more (y/n) ? ")

            if is_add_bead is "n":
                return
            current_bead = {
                "name": {
                    "value": "bead_" + str(cpt),
                    "regex": "."
                },
                "x": {
                    "value": "",
                    "regex": "^-?[0-9]+(.[0-9]+)?$"
                },
                "y": {
                    "value": "",
                    "regex": "^-?[0-9]+(.[0-9]+)?$"
                },
                "radius": {
                    "value": "",
                    "regex": "^-?[0-9]+(.[0-9]+)?$"
                },
                "conc": {
                    "value": "",
                    "regex": "^-?[0-9]+(.[0-9]+)?$"
                },
                "chem": {
                    "value": "",
                    "regex": "^-?[a-z]+$"
                }
            }

            for e in current_bead:
                while not bool(re.search(current_bead[e]["regex"],  current_bead[e]["value"])):
                    current_bead[e]["value"] = input(e + " : ")

            self.beads.append(current_bead)

            cpt += 1
            is_add_bead = None

    def write_header_file(self):
        """
        Write the header of the output file (the common variables)
        :return: None
        """
        with open(self.output_file, "w") as file:
            file.write("nSpecies = 1\n")
            file.write("dimension = 1\n")
            file.write("maxSteps = {0}\n".format(self.gamma_f))
            file.write("interval = {0}\n".format(self.get_step()))
            file.write("seed = ??\n")
            file.write("temperature = 313.13\n")
            file.write("scale = 5e-13\n")

    def write_bead_file(self):
        """
        Write the beads on the output file
        :return: None
        """
        with open(self.output_file, "a") as file:
            for b in self.beads:
                file.write("\n{0} = (\n".format(b["name"]["value"]))
                file.write("x = {0}\n".format(b["x"]["value"]))
                file.write("y = {0}\n".format(b["y"]["value"]))
                file.write("radius = {0}\n".format(b["radius"]["value"]))
                file.write("conc = {0}\n".format(b["conc"]["value"]))
                file.write("chem = {0}\n".format(b["chem"]["value"]))
                file.write(")\n")
