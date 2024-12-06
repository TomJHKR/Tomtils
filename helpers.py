import os
from print_color import print
from typing import Union
from rich.console import Console
from rich.markdown import Markdown
import argparse

def get_input():
    print("Please enter values seperated by newline: ", color='blue')
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    if line == None:
        return ""
    return lines

def validate_input(inp: Union[str,list]):
    if not inp:
        inp = get_input()
    if isinstance(inp, str):
        inp = [inp]
    return inp

def help():
    console = Console()

    # Markers for the sections to extract
    actions_start = "---------------------------------------"
    actions_end = "## Installation"
    usage_start = "## Usage"
    usage_end = "### Example Commands:"
    with open('readme.md') as f:
        lines = f.readlines()

    def extract_section(lines, start_marker, end_marker):
        section = []
        capture = False
        for line in lines:
            if end_marker in line and capture:
                break
            if start_marker in line:
                capture = True
            if capture:
                section.append(line)
        return section

    actions_section = extract_section(lines, actions_start, actions_end)

    usage_section = extract_section(lines, usage_start, usage_end)

    # Combine and display the relevant sections
    relevant_content = actions_section + usage_section
    if relevant_content:
        md = Markdown("".join(relevant_content))
        console.print(md)
    else:
        console.print("[bold red]Relevant sections not found in the README![/bold red]")
    console.print(Markdown("---------------------------------------"))

# Function to parse arguments and execute the specified method
def get_arguments():
    parser = argparse.ArgumentParser(description="Tomtils: Utility Tool for SOC Analysts")

    parser.add_argument('-m','--method', required=False, type=str, help='The method to execute (e.g., "decode64", "fang")')

    parser.add_argument('-i','--input', type=str, required=False, help='Specify the input for the method')

    return parser

def parse_arguments():
    parser = get_arguments()
    args = parser.parse_args()
    return args

