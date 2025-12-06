#!/usr/bin/env python3
import os, urllib.parse

def scan():
    data=[]
    for root, dirs, files in os.walk("."):
        if "README.md" in files and root!=".":
            pretty=root.strip("./").replace("-", " ")
            encoded=urllib.parse.quote(root.strip("./"))
            data.append({"name": pretty, "path": root, "url": encoded})
    return data

def write_cards(sections):
    cards=[]
    for s in sections:
        cards.append(f'''
<a href="{s["url"]}/">
<div style="border:1px solid #ccc;padding:12px;margin:8px;border-radius:8px;display:inline-block;width:200px;">
  <h3>{s["name"].title()}</h3>
  <p>{s["path"]}</p>
</div>
</a>
''')
    with open("index.md") as f: home=f.read()
    home=home.replace("<!-- cards will be inserted here -->","".join(cards))
    with open("index.md","w") as f: f.write(home)

def write_sidebar(sections):
    with open("sidebar.md","w") as f:
        f.write("# 📑 Sidebar\n\n")
        for s in sections:
            f.write(f"- [{s['name'].title()}]({s['url']}/)\n")

if __name__ == "__main__":
    sec=scan()
    write_cards(sec)
    write_sidebar(sec)
