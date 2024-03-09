#fda that recognizes int, float and variable names
states = []
symbols = []
finalStates = []
transitionRules = []
currentState = ''

def init():
    global states, symbols, finalStates, transitionRules, currentState
    file = open('./machine.txt')
    states = file.readline().strip().split(',')
    symbols_line = file.readline().strip()
    finalStates = file.readline().strip().split(',')
    
    for symbol in symbols_line:
        symbols.append(symbol)
    
    line = file.readline().strip()
    while line:
        transitionRules.append(line)
        line = file.readline().strip()

    currentState = states[0]
    file.close()

def readInputFile():
    file = open('./input.c')
    lines = file.readlines()
    for line in lines:
        execute_dfa(line.strip())

def execute_dfa(line):
    global currentState
    for char in line:
        for rule in transitionRules:
            r = rule.split(':')
            if r[0] == currentState and char in r[1]:
                currentState = r[2]
                #r[0]: origin state
                #r[1]: symbols to read
                #r[2]: destination state
    print(line, 'done:', currentState)
    recognized = 0
    for fs in finalStates:
        if fs.split(':')[0] == currentState:
            print('recongnized as', fs.split(':')[1])
            recognized = 1
    if not recognized:
        print(line, 'not recognized')
    currentState = states[0]


init()
readInputFile()
