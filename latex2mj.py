# ########################################################
#
# Converts LaTeX-styled equations to MathJax-styled equations in a Markdown file.
#
# USAGE
#
#   python latex2mj.py [-h] <FileNameIn> [<FileNameOut> -i i1 i2 i3 i4]
#
# ARGS
#   FileNameIn - input LaTeX-styled Markdown file name
#   FileNameOut - output MathJax-styled Markdown file name (if not specified will overwrite FileNameIn)
#   -i sets the inline equation delimiters [OrigOpen OrigEnd NewOpen NewEnd], default=[$ $ \\( \\)]
#
# June 2018
# Brendan Hasz
# winsto99@gmail.com
# brendanhasz.github.io
# ########################################################

import pandas as pd
import argparse
import glob

# Command line arguments
p = argparse.ArgumentParser(description='Combine multiple STAN fit MCMC chain .csv files')
p.add_argument("out", help="Combined chain output .csv filename")
p.add_argument("ins", nargs='+', help="List of input per-chain .csv filenames")
p.add_argument("-o", "--horiz", action='store_true', help="Concatenate horizontally instead of vertically")
args = p.parse_args()

# Combine csv files and save to single file
ins = [] #list of per-chain dataframes
print('Combined')
for tinp in args.ins: #for each input pattern (can use wildcards)
    for tin in glob.glob(tinp): #for each input filename
        print('  '+tin)
        ins.append(pd.read_csv(tin)) #read it in as a dataframe
if args.horiz:
    tdf = pd.concat(ins, axis=1) #concatenate per-chain dataframes horizontally
else:
    tdf = pd.concat(ins) #concatenate per-chain dataframes vertically
tdf.to_csv(args.out, index=False) #write csv for all chains
print('Into '+args.out)
