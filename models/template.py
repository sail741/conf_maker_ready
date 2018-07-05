from models.model import Model
from tools.tools import greek, index_to_str


# FILL HERE : 1/4 replace the name of the class and the description
class Template(Model):
    """
    The Template model.
    """

    # FILL HERE : 2/4 replace the equations with the good ones
    du = "[a + u²v - u].{0} + {1}u".format(greek["gamma"], greek["deltaU"])
    dv = "[b - u²v].{0} + d.{1}u".format(greek["gamma"], greek["deltaU"])

    def __init__(self, gamma_0=None, gamma_f=None, n=None):
        """
        Initialise when we create a the model.
        """

        # We initialise gamma_0, gamma_f and n if the user entered something.
        Model.__init__(self, gamma_0, gamma_f, n)

        '''
        We define the fixed attribute (that won't change for all the equations of this model).
        display : how we show it to the user to ask him to fill the value
        var_name : how the variable is written in the .conf file
        value : The value of the variable. Set to "" (empty string) by default.
        '''
        # FILL HERE : 3/4 put the good attributes of your model (specifics variables that the user need to give)
        self.fixed_attributes = [
            {
                "display": "a",
                "var_name": "a_spec",
                "value": ""
            },
            {
                "display": "b",
                "var_name": "b_spec",
                "value": ""
            },
            {
                "display": "d",
                "var_name": "d_spec",
                "value": ""
            }
        ]

        # We run the setup function to ask every attribute to the user.
        self.setup()

    def write_file(self):
        """
        The function used to write the .conf file.
        :return:
        """

        # We start by writing the header (common variables) and beads;
        Model.write_header_file(self)
        Model.write_bead_file(self)

        # then we write specific data
        with open(self.output_file, "a") as file:
            # We write the formulas. We start from gamma_0 to gamma_f adding "get_step" at each loop.
            # For each loop, we add 2 equations : du and dv.
            file.write("formula = (\n")

            i = 0
            current_gamma = self.gamma_0
            while current_gamma < self.gamma_f:
                # FILL HERE : 4/4 Change the display of your equation in the .conf file
                file.write("delta_{0} = \"(a_spec + {0}*{0}*{1} - {0}) * G_{2} + laplacian_{0};\"\n".format(index_to_str(i), index_to_str(i + 1), i))
                file.write("delta_{2} = \"(b_spec + {0}*{0}*{1}) * G_{2} + d_spec * laplacian_{0};\"\n".format(index_to_str(i), index_to_str(i + 1), i))
                i += 2
                current_gamma += self.get_step()

            file.write(")\n")

            # Then we write the init part : declaration of variable.
            # in this part, we write fixed specific attributes
            file.write("init = (\n")
            for att in self.fixed_attributes:
                file.write("float4 {0} = {1};\n".format(att["var_name"], att["value"]))

            # in this part, we write all the gamma (from gamma_0 to gamma_f with "get_step" between each value)
            i = 0
            current_gamma = self.gamma_0
            while current_gamma < self.gamma_f:
                file.write("float4 G_{0} = {1:.2f};\n".format(i, current_gamma))
                i += 1
                current_gamma += self.get_step()
            file.write(")\n")
