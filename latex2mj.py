# #############################################################################
#
# Converts LaTeX-styled equations to MathJax-styled equations in Markdown.
#
# USAGE
#
#   python latex2mj.py [-h] <FileIn> <FileOut>
#
# ARGS
#   FileNameIn - input LaTeX-styled Markdown file name
#   FileNameOut - output MathJax-styled Markdown file name to write
#
# June 2018
# Brendan Hasz
# winsto99@gmail.com
# brendanhasz.github.io
# #############################################################################

import argparse
import re

# Command line arguments
p = argparse.ArgumentParser(description='Convert LaTeX-styled equations to MathJax-styled equations in Markdown')
p.add_argument("FileIn", help="Filename of the input file (with LaTeX-styled equations)")
p.add_argument("FileOut", default=None, help="Filename of the output file to write (with MathJax-styled equations)")
args = p.parse_args()

# Load file
with open(args.FileIn, "r") as f:
    I = f.read()

# Find inlines and replace $x$ with \\(x\\)
ml = r'50' #max length (in chars) for inlines
O = re.sub(r'((?<!\$)(\$)([^\$]{1,'+ml+'}?)(\$)(?!\$))', r'\\\\( \3 \\\\)', I)

# Write output file
with open(args.FileOut, "w") as f:
    f.write(O)

