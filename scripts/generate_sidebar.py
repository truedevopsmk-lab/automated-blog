#!/usr/bin/env python3
import os, urllib.parse

def find_sections():
    sections = []
    for root, dirs, files in os.walk("."):
        if "README.md" in files and root != ".":
            encoded = urllib.parse.quote(root.strip("./"))
            sections.append((root, encoded))
    return sorted(sections)

def write_sidebar():
    sections = find_sections()
    with open("sidebar.md","w") as f:
        f.write("# 📑 Sidebar\n\n")
        for name, enc in sections:
            pretty = name.replace("-", " ").title()
            f.write(f"- [{pretty}]({enc}/)\n")

if __name__ == "__main__":
    write_sidebar()
