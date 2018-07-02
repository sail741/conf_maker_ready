from model import Model
from tools.tools import greek, index_to_str


class Schnakenberg(Model):

    du = "[a + u²v - u].{0} + {1}u".format(greek["gamma"], greek["deltaU"])
    dv = "[b - u²v].{0} + d.{1}u".format(greek["gamma"], greek["deltaU"])

    def __init__(self, gamma_0=None, gamma_f=None, n=None, a_spec="", b_spec="", d_spec=""):
        Model.__init__(self, gamma_0, gamma_f, n)

        self.fixed_attributes = [
            {
                "display": "a",
                "var_name": "a_spec",
                "value": a_spec
            },
            {
                "display": "b",
                "var_name": "b_spec",
                "value": b_spec
            },
            {
                "display": "d",
                "var_name": "d_spec",
                "value": d_spec
            }
        ]
        self.setup()

    @staticmethod
    def eq_to_string():
        return "du/dt = {0}\ndv/dt = {1}".format(Schnakenberg.du, Schnakenberg.dv)


    def create_file(self):
        Model.create_header_file(self)
        with open(self.output_file, "a") as file:
            file.write("formula = (\n")

            i = 0
            for v in range(self.gamma_0, self.gamma_f, self.get_step()):
                file.write("delta_{0}_a = \"(a_spec + {0}_a*{0}_a*{0}_b - {0}_a) * G_{1} + laplacian_{0}_a;\"\n".format(index_to_str(i), i))
                file.write("delta_{0}_b = \"(b_spec + {0}_a*{0}_a*{0}_b) * G_{1} + d_spec * laplacian_{0}_a;\"\n".format(index_to_str(i), i))
                i += 1

            file.write(")\n")
            file.write("init = (\n")
            for att in self.fixed_attributes:
                file.write("float4 {0} = {1};\n".format(att["var_name"], att["value"]))

            i = 0
            for v in range(self.gamma_0, self.gamma_f, self.get_step()):
                file.write("float4 G_{0} = {1};\n".format(i, v))
                i += 1
            file.write(")\n")
