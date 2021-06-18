from JSON_parse import JSONParser
import sys
import os


NUM_TEST_FILES = 6


def run(num_tests):

    log_fname = "test_results.log"
    log_path = os.path.join(os.getcwd(), "tests", log_fname)

    with open(log_path, "w") as f:
        f.write("******** Running Tests *********** \n\n\n")

    sys.stdout = open(log_path, "a")
    sys.stderr = open(log_path, "a")

    for num in range(num_tests):
        try:
            test_fname = "test" + str(num + 1) + ".json"
            test_path = os.path.join(os.getcwd(), "tests", test_fname)

            with open(test_path, "r") as f:
                inp = f.read()

            with open(log_path, "a") as f:
                f.write("------{name} INPUT------\n".format(name=test_fname))
                f.write(inp)
                f.write("\n\n\n-------RESULTS------\n")

            parser = JSONParser()

            try:
                r = parser.parse(text=inp)

                if r:
                    with open(log_path, "a") as f:
                        f.write("Valid JSON.\n\n")

            except SyntaxError as e:
                with open(log_path, "a") as f:
                    f.write(str(e) + "\n")
                    f.write("Invalid JSON.\n\n\n")

        except FileNotFoundError:
            pass
    return


if __name__ == "__main__":
    run(NUM_TEST_FILES)
