from basescript import BaseScript

class Add_Sub(BaseScript):
  
    def __init__(self):
        super(Add_Sub, self).__init__()
        self.a = 100
        self.b = 20

    def define_args(self, parser):
        parser.add_argument('c', type=int, help='Number')
       
    def define_args(self, pars):
        pars.add_argument('d', type=int, help='Number')
        

    def run(self):
        # print(self.a + self.b + self.args.c)
        # print(self.a + self.b - self.args.c)

        # print(self.a - self.b * self.args.c)
        # print(self.a - self.b - self.args.c)
        print(self.a - self.b  + self.args.d + self.args.c)
        print(self.a - self.b  + self.args.d)
      


if __name__ == '__main__':
    Add_Sub().start()