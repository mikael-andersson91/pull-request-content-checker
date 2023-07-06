import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f'Hello {my_input}'

    for line in os.path.abspath(os.environ["GITHUB_OUTPUT"]):
        print(line) 
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]),"a") 
    f.write("myOutput={my_output}")
    f.close()
    #print(f'echo "myOutput={my_output}" >> "{os.path.abspath(os.environ["GITHUB_OUTPUT"])}"') 


if __name__ == "__main__":
    main()
