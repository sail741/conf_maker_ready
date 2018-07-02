import math
import re

from tools.tools import greek

class Model:
    output_file = "output.conf"

    du = None
    dv = None

    fixed_attributes = {}

    gamma_0 = ""
    gamma_f = ""
    n = ""

    def __init__(self, gamma_0, gamma_f, n):
        self.gamma_0 = gamma_0
        self.gamma_f = gamma_f
        self.n = n

    def __str__(self):
        return "du/dt = {0}\ndv/dt = {1}\nWith : {2} and {3}".format(
            self.du, self.dv, self.fixed_attributes, {"gamma_0 = ": self.gamma_0, "gamma_f": self.gamma_f, "n": self.n})

    @staticmethod
    def eq_to_string():
        return ""

    def get_step(self):
        res = math.floor((self.gamma_f - self.gamma_0) / self.n)
        if res == 0:
            return self.gamma_f - self.gamma_0 + 1
        return res

    def create_header_file(self):
        with open(self.output_file, "w") as file:
            file.write("nSpecies = 1\n")
            file.write("dimension = 1\n")
            file.write("maxSteps = {0}\n".format(self.gamma_f))
            file.write("interval = {0}\n".format(self.get_step()))
            file.write("seed = ??\n")
            file.write("temperature = 313.13\n")
            file.write("scale = 5e-13\n")
            file.write("\n")

    def setup(self):
        while self.gamma_0 is None or not bool(re.search('^-?[0-9]+$', str(self.gamma_0))):
            self.gamma_0 = int(float(input(greek["gamma"] + "_0 : ")))
        while self.gamma_f is None or not bool(re.search('^-?[0-9]+$', str(self.gamma_f))):
            self.gamma_f = int(float(input(greek["gamma"] + "_f : ")))
        while self.n is None or not bool(re.search('^-?[0-9]+$', str(self.n))):
            self.n = int(float(input("N : ")))

        for att in self.fixed_attributes:
            while att["value"] == "" or not bool(re.search('^-?[0-9]+$', att["value"])):
                att["value"] = input(att["display"] + " : ")
