import argparse

def parser_argument():
    #if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--name", type=str, default="1234")
    args = parser.parse_args()
    return args
    # else:
    #     args = argparse.Namespace(name='123')
    #     return args

class callablity():
    def __init__(self):
        self.args = parser_argument()

    def call(self):
        print(self.args)
        print(self.args.__dict__)
        print(self.args.name)

args = parser_argument()
print(args)
