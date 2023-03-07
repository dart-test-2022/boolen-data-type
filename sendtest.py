import requests
import sys
import json
from pprint import pprint
import argparse

url = 'http://codeschooluzapi.pythonanywhere.com/lesson/'

f = open('data.json', 'r')
data = json.load(f)
pprint(data)
parser = argparse.ArgumentParser()
parser.add_argument('github', help='github username')
parser.add_argument('repo', help='repository | homework')
parser.add_argument('changed_files', help='changed files')

arg = parser.parse_args()

print(arg.changed_files)

tasks = []
i = 0
while i < len(data):
    data[i]['name'] = data[i]['name'][:-10]
    if data[i]['name'] in arg.changed_files:
        tasks.append(data[i])

    i += 1

dct = {
    "github": arg.github,
    "tasks": tasks,
    "course": "Dart Foundation",
    "assignment": arg.repo.split("/")[-1]
}
pprint(dct)
f.close()
pprint(dct)
r = requests.post(url+'submission/add/', json=dct)
print(r.status_code)


corrects = 0
for answer in data:
    corrects += answer['isSolved']

print('=' * 8 + ' Natijalar: ' + '=' * 8)
    # Print readability report
for task in data:
    # task_name=results[t]
    
    if task['isSolved']:
        print(
            f'{task["name"]}  Passed:{task["details"]["passed"]} Failed:{task["details"]["failed"]} ✅')
    else:
        print(f'{task["name"]}  Passed:{task["details"]["passed"]} Failed:{task["details"]["failed"]} ❌')

 
# Check if all tasks are solved otherwise raise error
if corrects == len(data) and len(data) == 10:
    print('All tasks are solved')
    print('Barcha vazifalar topshirildi')
else:
    print('Not all tasks are solved')
    print('Barcha vazifalar topshirilmagan')
    sys.exit(1)
