import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Write yourname!")
parser.add_argument("age", help = "Write your age!")
parser.add_argument("job", help = "Write your job")
arg = parser.parse_args()

print(arg.name, arg.age, arg.job)