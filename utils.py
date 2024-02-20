import json

extract_route = lambda request: request.split(' ')[1][1:]

read_file = lambda filepath: open(filepath, 'rb').read()

load_data = lambda filename: json.load(open('data/' + filename))

load_template = lambda filename: open('templates/' + filename).read()

def add_note(params):
    with open('data/notes.json', 'r') as file:
        notes = json.load(file)
    print(notes)
    notes.append(params)
    with open('data/notes.json', 'w') as file:
        json.dump(notes, file, indent=2)

# add_note = lambda params: json.dump(load_data('notes.json') + [params], open('data/notes.json', 'w')) <-- Possible lambda implementation

build_response = lambda body='', code=200, reason='OK', headers='': f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode() if headers else f'HTTP/1.1 {code} {reason}\n\n{body}'.encode()