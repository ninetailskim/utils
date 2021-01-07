import argparse
from callable import callablity

parser = argparse.ArgumentParser()
parser.add_argument("--master",type=str)
args = parser.parse_args()

co = callablity()

print(args)

co.call()
