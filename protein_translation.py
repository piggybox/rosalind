import sys

lines = open(sys.argv[1].strip(), 'r').readlines()
text = str(lines[0]).strip()

translation = { 'C':{'A':{'U':'H', 'C':'H', 'A':'Q', 'G':'Q'},
                    'C':{'U':'P', 'C':'P', 'A':'P', 'G':'P'},
                    'G':{'U':'R', 'C':'R', 'A':'R', 'G':'R'},
                    'U':{'U':'L', 'C':'L', 'A':'L', 'G':'L'}},
                'G':{'A':{'U':'D', 'C':'D', 'A':'E', 'G':'E'},
                    'C':{'U':'A', 'C':'A', 'A':'A', 'G':'A'},
                    'G':{'U':'G', 'C':'G', 'A':'G', 'G':'G'},
                    'U':{'U':'V', 'C':'V', 'A':'V', 'G':'V'}},
                'U':{'A':{'U':'Y', 'C':'Y', 'A':'STOP', 'G':'STOP'},
                    'C':{'U':'S', 'C':'S', 'A':'S', 'G':'S'},
                    'G':{'U':'C', 'C':'C', 'A':'STOP', 'G':'W'},
                    'U':{'U':'F', 'C':'F', 'A':'L', 'G':'L'}},
                'A':{'A':{'U':'N', 'C':'N', 'A':'K', 'G':'K'},
                    'C':{'U':'T', 'C':'T', 'A':'T', 'G':'T'},
                    'G':{'U':'S', 'C':'S', 'A':'R', 'G':'R'},
                    'U':{'U':'I', 'C':'I', 'A':'I', 'G':'M'}}}

result = ""
for i in range(0, len(text), 3):
    target = translation[text[i]][text[i+1]][text[i+2]]
    if target == 'STOP':
        break
    else:
        result += target

print result

