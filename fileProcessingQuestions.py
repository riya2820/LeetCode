import csv
import re
from collections import Counter

def count_non_empty(path):
    with open(path) as f:
        count = 0
        for line in f:
            if line.strip():
                count += 1
        return count
        #  return sum(1 for line in f if line.strip())

def phrase_count(path, phrase):
    with open(path) as f:
        count = 0
        for line in f:
            if phrase in line:
                count += 1
        return count

def top_k_elements(path):
    with open(path) as f:
        words = re.findall(r"\w+", f.read().lower())
    return Counter(words).most_common(5) # returns top 5 elements in file

def merge_files(f1,f2,out):
    lines = set() # deduplicate
    for path in (f1,f2):
        with open(path) as f:
            for line in f:
                lines.add(line.strip())
    with open(out, "w") as o:
        for line in sorted(lines): # + sort
            o.write(line+"\n")


def avg_score(path):
    with open(path) as f:
        data = json.load(f)
        for d in data:
            d["score"] += score 
with open(path) as f:
        data = json.load(f)
    scores = [d["score"] for d in data]
    return sum(scores) / len(scores)


def flattedn(d, parent_key="", sep="."):
    f = {}
    queue = deque([(d, '')])  # Queue holds tuples of (current_dict, current_key)
    #  [{"a":{"b":1,"c":{"d":2}}, "e":3}, ' ']
    while queue:
        i, j = queue.popleft() # {a:{'b':1}, ''}
        
        for k, v in i.items(): 
            new_key = f"{i}_{k}" if j else k
            
            if isinstance(v, dict):
                queue.append((v, new_key))  # Add nested dictionaries to the queue
            else:
                f[new_key] = v 


    # or using new dict + recursive
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}-{sep}{k}" if parent_key else k
        if isinstance(v,dict):
            items.update(flatten(v,new_key, sep=sep)) # recursive call 
        else:
            items[k] = v
    return items 


def read_csv_file(file1):
    # print line by line
    with open{'Giants.csv', mode='r'} as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            print(line)

    # map to dict
    with open('Giants.csv', mode-'r') as file:
        csvFile = csv.DictReader(file) # OrderedDict([('Organization', 'Alphabet'), ... 
        for line in csvFile:
            print(line)
# example
data = {"a":{"b":1,"c":{"d":2}}, "e":3}
print(flatten(data))  


