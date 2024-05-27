# Python testbed template

This template is a collection of shell scripts and a Readme to make it easy to quickly iterate on a python script, keeping good visibility on versioning. An example use case is using a chatbot/LLM like ChatGPT to generate and iterate on a script, then using this python testbed to test versions and keep track of iterations and diffs.

## Setup

```bash
# use whichever version of python you need
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Scripts

Run this command to open the next iteration file, diff the most recent two files, and run the script - this works well for a vscode workflow, but it will use your default $VISUAL editor.

```bash
scripts/next.sh
```

open empty file for next version of script:

```bash
scripts/create_next_iteration.sh
```

run most recent version:

```bash
scripts/run_most_recent_iteration.sh
```

diff two most recent iteration:

```bash
scripts/diff_most_recent_iterations.sh
```
