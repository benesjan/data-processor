import sys

if len(sys.argv) != 3:
    print("Not enough input arguments")
    sys.exit(1)

lines_seen = set()

with open(sys.argv[1], 'r') as input_file, open(sys.argv[2], 'w') as output_file:
    for line in input_file:
        if line.startswith("http") and line not in lines_seen:
            lines_seen.add(line)
            output_file.write(line)
