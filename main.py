import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]
    my_output = f'Hello {my_input}'
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]),"a")
    f.write(f'myOutput={my_output}')
    f.close()
if __name__ == "__main__":
    main()
