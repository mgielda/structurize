#!/usr/bin/env python3

import sys

'''
Turn a markdown file into a collapsible content list.
Enable changing paragraphs to their summary held in the original file in comments.
'''

css = '''
body { font-family: 'Roboto', sans-serif; width: 1024px; margin: auto; overflow-y: scroll }
body li.code { font-family: 'Overpass Mono', monospace }
li.title { display: none }
#main.titlesOnly li.title { display: list-item }
#main.titlesOnly li.text { display: none }
'''

script = '''
var toggler = document.getElementById("toggleTitlesOnly");

toggler.addEventListener("click", function() {
  var main = document.getElementById("main");
  main.classList.toggle("titlesOnly");
});
'''

lines = open(sys.argv[1]).readlines()

inside_code = False
output = f'<html><head><link href="https://fonts.googleapis.com/css?family=Overpass+Mono|Roboto&display=swap" rel="stylesheet"><style>{css}</style></head><body><button id="toggleTitlesOnly">Toggle titles</button><ul id="main">'
level = 0
# number of opens and closed actually will help in h1, h3, h1 situations
# but not fully used yet
opened = 0
closed = 0
for l in lines:
    if inside_code:
        if l[0:3] == '```':
            output += l + '</li>'
            inside_code=False
        else:
            output += l + '<br/>'
        continue
    if  l[0:3] == '```':
        inside_code=True
        output += '<li class="text code">' + l + '<br/>'
        continue
    if l.strip() == '':
        continue
    if l[0] == '#':
        hlevel = len(l.split(' ')[0]) # assuming space after "#"
        heading = l.split(' ',1)[1]
        if hlevel > level: # go down a level
            pass # do nothing, we will open a ul and li below
        # warning! we assume people use levels responsibly
        # i.e. h1 -> h3 -> h1 kills us
        elif hlevel < level: # go up a level
            for i in range(0, level-hlevel+1):
                output += '</ul>'
                output += '</li>'
                closed += 1
        else: # keep level
            output += '</ul>'
            output += '</li>'
            closed += 1
        output += f'<li>{heading}'
        output += '<ul>'
        opened += 1
        level = hlevel
    else:
        if l[0:4] == "<!--": # assume one-line comment
            output += f'<li class="title">{l[4:-4]}</li>'
        else:
            output += f'<li class="text">{l}</li>'

if opened < closed:
    print("ERROR! We closed more <uls> than we opened!")

if opened > closed:
    diff = opened - closed
    print(f"Closed {diff} unclosed uls.")
    for i in range(0, diff):
        output += '</ul>'
        output += '</li>'

output += f'</ul></body><script>{script}</script></html>'

from bs4 import BeautifulSoup
print(BeautifulSoup(output, 'html.parser').prettify())

