import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--start", help="what do you need?")
parser.add_argument("--end", help="I promise I'll be very helpful")


args = parser.parse_args()
if not args.start:
    args.start = 0


a = 0
start = int(args.start)
end = int(args.end) + 1
for n in range(start, end):
    a += n

print a

