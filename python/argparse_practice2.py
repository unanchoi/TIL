'''
Option Argument
'''
import argparse

parser.add_argument("--age", help="It means your age!",type=int)
parser.add_argument("--name", help = "It means your name")
parser.add_argument("-i", "--information", help = "It means your information")

args = parser.parse_args()

if args.age and args.name:
    print(args.name, args.age)

if args.information:
    print("your name, your age")