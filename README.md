# Pull Request Content Checker

[![Action Template](https://img.shields.io/badge/Action%20Template-Python%20Container%20Action-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAM6wAADOsB5dZE0gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRhZG/SsMxFEZPfsVJ61jbxaF0cRQRcRJ9hlYn30IHN/+9iquDCOIsblIrOjqKgy5aKoJQj4O3EEtbPwhJbr6Te28CmdSKeqzeqr0YbfVIrTBKakvtOl5dtTkK+v4HfA9PEyBFCY9AGVgCBLaBp1jPAyfAJ/AAdIEG0dNAiyP7+K1qIfMdonZic6+WJoBJvQlvuwDqcXadUuqPA1NKAlexbRTAIMvMOCjTbMwl1LtI/6KWJ5Q6rT6Ht1MA58AX8Apcqqt5r2qhrgAXQC3CZ6i1+KMd9TRu3MvA3aH/fFPnBodb6oe6HM8+lYHrGdRXW8M9bMZtPXUji69lmf5Cmamq7quNLFZXD9Rq7v0Bpc1o/tp0fisAAAAASUVORK5CYII=)](https://github.com/jacobtomlinson/python-container-action)

This is an action for validating that a pull request body is not empty and has been modified from the given template to a specific degree. The action takes a value between 0-1 as an indicator for how similar the pull request body is allowed to be to the template in order to ensure that the creator of a pull request has actually filled out the body/description with content. The action fails if the pull request body is empty or not enough has been changed from the pull request template

## Usage

### Example workflow

```yaml
name: My Workflow
on: [pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Run action
      uses: mikael-andersson91/pull-request-content-checker@v0
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `pull_request_template_path`  | Path to the pull request template used by the repository (defailt value: .github/pull_request_template.md)    |
| `max_pull_request_description_match`  | Value between 0-1 to indicate how similar the pull request body/description is allowed to be with the template (default value: 0.7) |
| `github_Token`  | GitHub Token required for API requests to get most up-to-date pull request details |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `pull_request_body_match`  |  Value between 0-1 to indicate how much of the pull request body matches the pull request template   |

### Using the optional input

This is how to use the optional input.

```yaml
with:
  pull_request_template_path: .github/pull_request_template.md
  max_pull_request_description_match: 0.5
  github_token: ${{ secrets.GITHUB_TOKEN }}
```

### Using outputs

Show people how to use your outputs in another action.

```yaml
steps:
- uses: actions/checkout@v3
  with:
    fetch-depth: 0

- name: Run action
  id: pr_content_check
  uses: mikael-andersson91/pull-request-content-checker@v0
  with:
    pull_request_template_path: ".github/pull_request_template.md"
    max_pull_request_description_match: 0.5
    github_token: ${{ secrets.GITHUB_TOKEN }}

# Example outputs, print how much of a match in pr body compared to pr template (value between 0-1) 
- name: Check outputs
    run: |
    echo "Outputs - ${{ steps.pr_content_check.outputs.pull_request_body_match }}"
```
