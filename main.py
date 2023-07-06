import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f'Hello {my_input}'

    for line in os.path.abspath(os.environ["GITHUB_OUTPUT"]):
        print(line)    

    print(f'echo "myOutput={my_output}" >> "{os.path.abspath(os.environ["GITHUB_OUTPUT"])}"')
    for line in os.path.abspath(os.environ["GITHUB_OUTPUT"]):
        print(line)    


if __name__ == "__main__":
    main()
