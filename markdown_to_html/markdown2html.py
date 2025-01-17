#!/usr/bin/python3
"""
Markdown to HTML converter module.

This script reads a Markdown file and converts its content to HTML.
"""

import sys

def markdown_to_html(input_file, output_file):
    """Converts Markdown content to HTML."""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if line.startswith('# '):
                    outfile.write(f"<h1>{line[2:].strip()}</h1>\n")
                elif line.startswith('## '):
                    outfile.write(f"<h2>{line[3:].strip()}</h2>\n")
                elif line.startswith('- '):
                    outfile.write(f"<li>{line[2:].strip()}</li>\n")
                else:
                    outfile.write(f"<p>{line.strip()}</p>\n")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown_to_html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)
    
    markdown_to_html(sys.argv[1], sys.argv[2])
