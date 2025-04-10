#!/usr/bin/env python3
# taggercopy Source Code

import os
from openai import OpenAI


client  = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-no-key-required"
)

completion = client.chat.completions.create(
    model="LLaMA_CPP",
    grammer='''
<tag>  ::= [a-z]+ | <tags> | <tags_end> | "\n"
<tags> ::=  [a-z]+ "," <tag>
<tags_end> ::=  <tags> "\n" ''',
    messages=[
        { "role": "system", "content": "act as a note tag extractor. return a list of tags lowercase, ex: note,blog,code,idea. do not be helpful."},
        { "role": "user", "content": "Idea, printer, automation for making paper checklist every day. Add whisper interface to add new items really quickly in the morning. Add business idea where you make a piece of software and a companion app that allows for this type of bullet journal paper automation. Add Activity Pieces, Common Scripts. add whisper subscription? add android app"}
    ]
)

print(completion.choices[0].message)


from llama_index.llms.llamafile import Llamafile
import pyperclip

llm = Llamafile(temperature=0, seed=0)

resp = llm.complete("act as a obsidian notes tag extractor. example: [[notes]], [[coding]],[[idea]],  do not be helpful, output tags only. heres my note: ")

print(resp)


# 
from llama_index.core.llms import ChatMessage

message = [
    ChatMessage(
        role="system",
        content="act as a obsidian notes tag extractor. example: [[notes]], [[coding]],[[idea]],  do not be helpful, output tags only. heres my note: ",
    ),
    ChatMessage(
        role="user",
        content="""
Idea, printer, automation for making paper checklist every day.
Add whisper interface to add new items really quickly in the morning.
Add business idea where you make a piece of software and a companion app that allows for this type of bullet journal paper automation.
Add Activity Pieces, Common Scripts. 
add whisper subscription?
add android app"""
    )
]