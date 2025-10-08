import pymsteams

from dotenv import load_dotenv
import os

load_dotenv()

web_hook_var = os.getenv("WEB_HOOK")

teams_message = pymsteams.connectorcard(web_hook_var)

with open("../reports/markdown/md_report.md") as f:
    report = f.read()

teams_message.text(report)
teams_message.send()