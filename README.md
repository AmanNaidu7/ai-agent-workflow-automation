# AI Agent Workflow Automation

A simple AI-driven workflow automation prototype for support ticket triage.

## What it does
- Loads support tickets from JSON
- Uses an OpenAI model to classify and analyze each ticket
- Routes each ticket to the correct queue
- Generates a draft response
- Saves the results to an output JSON file

## Run
1. Install requirements:
   pip install -r requirements.txt

2. Add your API key to `.env`

3. Run:
   python run.py