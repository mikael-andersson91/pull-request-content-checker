import os
import json
import difflib


# Set the output value by writing to the outputs in the
# GITHUB_OUTPUT Environment File
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()
    print(f'Output {output_name}={output_value}')


def main():
    pr_template_path = os.environ["INPUT_PULL_REQUEST_TEMPLATE_PATH"]
    max_pull_request_description_match = float(
        os.environ["INPUT_MAX_PULL_REQUEST_DESCRIPTION_MATCH"]
        )
    print(f'pr_template_path: {pr_template_path}')
    print(f'max body match: {max_pull_request_description_match}')

    print(os.environ["GITHUB_EVENT_NAME"])
    f = open(os.environ["GITHUB_EVENT_PATH"])
    event_data = json.load(f)
    f.close()

    pr_filestream = open(pr_template_path)
    pr_template_contents = pr_filestream.read().strip()
    pr_filestream.close()

    pr_body = event_data["pull_request"]["body"].strip()
    pr_title = event_data["pull_request"]["title"].strip()
    print(pr_body)
    print(pr_title)

    pr_body_similarity_score = difflib.SequenceMatcher(
        None, 
        pr_body,
        pr_template_contents).ratio()

    if pr_body_similarity_score > max_pull_request_description_match:
        print(
            f"{pr_body_similarity_score} exceeds max similarity score"
            )
    else:
        print(
            f"{pr_body_similarity_score} is below max similarity score"
            )
    set_github_action_output('myOutput', pr_body_similarity_score)


if __name__ == "__main__":
    main()
