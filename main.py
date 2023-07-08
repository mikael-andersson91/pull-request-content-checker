import os
import json

# Set the output value by writing to the outputs in the
# GITHUB_OUTPUT Environment File
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()


def main():
    my_input = os.environ["INPUT_MYINPUT"]
    my_output = f'Hello {my_input}'

    print(os.environ["GITHUB_EVENT_NAME"])
    f = open(os.environ["GITHUB_EVENT_PATH"])
    event_data = json.load(f)
    f.close()

    print(event_data)

    set_github_action_output('myOutput', my_output)


if __name__ == "__main__":
    main()
