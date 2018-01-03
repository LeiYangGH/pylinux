import argparse
def process_argument():
    parser = argparse.ArgumentParser(description="description:create fitnesse test case", epilog=" %(prog)s description end")
    parser.add_argument('-f', dest="file", default = "test.txt")
    args = parser.parse_args()
    return args

args=process_argument()
print(args.file)
print("end")
