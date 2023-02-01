from basescript import BaseScript

class Calc(BaseScript):
    A = 10
    B = 20

    def add(self):
        print(self.A + self.args.b)

    def sub(self):
        print(self.B - self.args.b)

    def multiply(self):
        print(self.A * self.args.b)

    def division(self):
        print(self.B / self.args.b)

    def define_subcommands(self, subcommands):
        super(Calc, self).define_subcommands(subcommands)

        add_cmd = subcommands.add_parser("add", help="Adds number")
        add_cmd.set_defaults(func=self.add)
        add_cmd.add_argument('--b', type=int, help="Number to add")

        sub_cmd = subcommands.add_parser("sub", help="Subtracts number")
        sub_cmd.set_defaults(func=self.sub)
        sub_cmd.add_argument('--b', type=int, help="Number to subtract")

        multiply_cmd = subcommands.add_parser("multiply", help="Multiply number")
        multiply_cmd.set_defaults(func=self.multiply)
        multiply_cmd.add_argument('--b', type=int, help="Number to multiply")

        division_cmd = subcommands.add_parser("division", help="Divide number")
        division_cmd.set_defaults(func=self.division)
        division_cmd.add_argument('--b', type=int, help="Number to divide")

if __name__ == '__main__':
    Calc().start()