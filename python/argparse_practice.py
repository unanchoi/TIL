import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Write yourname!")
parser.add_argument("age", help = "Write your age!", type=int)
parser.add_argument("job", help = "Write your job")
arg = parser.parse_args()

print(arg.name, arg.age - 1, arg.job)

'''
Option Argument
'''

parser2 = argparse.ArgumentParser()
parser2.add_argument("--brain", help="brain", action="store_true")

args2 = parser.parse_args()
if args2.brain:
    print("you are genius!")
