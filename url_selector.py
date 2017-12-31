import sys

if len(sys.argv) != 4:
    print("Not enough input arguments")
    sys.exit(1)

sections = set()
with open(sys.argv[1], 'r') as sections_file:
    for line in sections_file:
        if line.startswith("http"):
            sections.add(line.strip())

with open(sys.argv[2], 'r') as input_file, open(sys.argv[3], 'w') as output_file:
    for line in input_file:
        for section in sections:
            if line.startswith(section):
                output_file.write(line)
                break
