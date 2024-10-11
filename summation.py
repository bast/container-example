import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "numbers", help="Numbers to sum", type=int, nargs='*'
)
args = parser.parse_args()

numbers = args.numbers

if len(numbers) > 1:
   print(f'Sum of numbers was: {sum(numbers)}')
else:
   print('You did not give me any numbers to sum!')
