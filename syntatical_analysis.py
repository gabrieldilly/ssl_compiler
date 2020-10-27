import argparse
from grammar import *
import csv
import numpy as np
import pandas as pd
import traceback
from lexical_analysis import set_code, next_token

# %%
def parse_args():
    parser = argparse.ArgumentParser(description = 'Syntatical Analysis')
    parser.add_argument('infile', type = argparse.FileType('r'), help = 'SSL file to be analyzed')
    return parser.parse_args()


length = 0
left = 1

# %%
def syntatical_analysis(input_file):
    global code
    global actions
    try:
        code = open(input_file, 'r')
    except:
        exit()
    set_code(code)
    # df = pd.read_excel('actions.xlsx')
    # actions = [list(df[c]) for c in df.columns]
    actions = list(csv.reader(open('actions.csv', 'r'), delimiter='\t'))
    state = 0
    stack = []
    stack.append(state)
    token, line = next_token()
    error = False
    next_el = actions[state + 1][dic[token]]

    while not is_accept(next_el):
        if token == Words.UNKNOWN:
            error = True
            break
        if is_shift(next_el) >= 0:
            state = is_shift(next_el)
            token, line = next_token()
            stack.append(state)
            next_el = actions[state + 1][dic[token]]
            print(token, next_el, state)
        elif is_reduction(next_el) >= 0:
            rule = is_reduction(next_el)
            for i in range(rule_atr[length][rule - 1]):
                stack.pop()
            try:
                state = int(actions[stack[-1] + 1][dic[rule_atr[left][rule - 1]]])
            except:
                traceback.print_exc()
                print('Erro de sintaxe na linha ' + str(line))
                error = True
                break
            stack.append(state)
            next_el = actions[state + 1][dic[token]]
        else:
            print('Erro de sintaxe na linha ' + str(line))
            error = True
            break
    if not error:
        print('\nSem erros sintáticos\n')

    return not error

# %%
def is_reduction(n):
    if n[0] == 'r':
        return int(n[1:])
    return -1


def is_accept(n):
    if n == 'acc':
        return True
    return False


def is_shift(n):
    if n[0] == 's':
        return int(n[1:])
    return -1


# %%
if __name__ == '__main__':
    args = parse_args()
    syntatical_analysis(args.infile.name)
