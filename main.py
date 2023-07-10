import os
import json
import difflib
import requests


def get_pull_request(pull_request_number, github_token):
    api_url = os.environ["GITHUB_API_URL"]
    github_repository = os.environ["GITHUB_REPOSITORY"]
    headers = {
        'Accept':'application/vnd.github+json'
        ,'Authorization':f'Bearer {github_token}'
        ,'X-GitHub-Api-Version':'2022-11-28' 
        }
    print(f'Geting pull request on {r.url}')
    r=requests.get(
        f'{api_url}/repos/{github_repository}/pulls/{pull_request_number}'
        ,headers=headers
        )
    # Throw exception if not 200
    r.raise_for_status()
    print(r.status_code)
    return json.loads(r.text)



# Set the output value by writing to the outputs in the
# GITHUB_OUTPUT Environment File
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()
    print(f'Output {output_name}={output_value}')


def is_pr_body_empty(pr_body):
    print(f'Pull request body: {pr_body}')
    if pr_body.isspace():
        raise Exception("The pull request body is empty")


def is_pr_body_below_similarity_score(pr_body,
                                      pr_template_contents,
                                      max_pull_request_similarity_score):
    pr_body_similarity_score = difflib.SequenceMatcher(
        None,
        pr_body,
        pr_template_contents).ratio()
    set_github_action_output('pull_request_body_match',
                             pr_body_similarity_score)
    if pr_body_similarity_score > max_pull_request_similarity_score:
        print(
            f"{pr_body_similarity_score} exceeds max similarity score"
            )
        raise Exception(
            f'Similarity score exceeded, score: {pr_body_similarity_score}'
            )
    else:
        print(
            f"{pr_body_similarity_score} is below max similarity score"
            )


def main():
    pr_template_path = os.environ["INPUT_PULL_REQUEST_TEMPLATE_PATH"]
    max_pull_request_description_match = float(
        os.environ["INPUT_MAX_PULL_REQUEST_DESCRIPTION_MATCH"]
        )
    github_token = os.environ["INPUT_GITHUB_TOKEN"]
    print(f'pr_template_path: {pr_template_path}')
    print(f'max body match: {max_pull_request_description_match}')

    print(os.environ["GITHUB_EVENT_NAME"])
    f = open(os.environ["GITHUB_EVENT_PATH"])
    event_data = json.load(f)
    f.close()

    pull_request = get_pull_request(event_data["number"], github_token)
    pr_title = pull_request["title"].strip()
    pr_body = pull_request["description"].strip()

    pr_filestream = open(pr_template_path)
    pr_template_contents = pr_filestream.read().strip()
    pr_filestream.close()

    print(pr_body)
    print(pr_title)
    is_pr_body_empty(pr_body)
    is_pr_body_below_similarity_score(pr_body,
                                      pr_template_contents,
                                      max_pull_request_description_match)


if __name__ == "__main__":
    main()
