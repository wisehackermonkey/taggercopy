#!/usr/bin/env python3
# taggercopy Source Code
import dotenv
import pyperclip
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
client = anthropic.Anthropic(
    api_key=api_key
)

# add short cut command to trigger pyperclip
current_clipboard = pyperclip.paste()
strip_clipboard = current_clipboard.strip()

note_classification_text = strip_clipboard
# """
# Idea, printer, automation for making paper checklist every day. Add whisper interface to add new items really quickly in the morning. Add business idea where you make a piece of software and a companion app that allows for this type of bullet journal paper automation. Add Activity Pieces, Common Scripts. add whisper subscription? add android app
# """

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=8192,
    temperature=1,
    system="act as a note tag extractor. return a list of tags lowercase, ex: \"note,blog,code,idea\". do not be helpful.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                "type" : "text",
                "text" : note_classification_text
                }
            ]
        }
    ]
)

tag_formated = message.content[0].text.split(",")
tag_final_form = "".join([ f"[[{tag}]]" for tag in tag_formated ])
print("output:")
print(tag_final_form)
pyperclip.copy(tag_final_form)