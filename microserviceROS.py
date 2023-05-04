import re
import json
import time

ROSPipe = 'ROSPipe.txt'


def writeToFile(file, message):
    while True:
        try:
            with open(file, 'w') as openPipe:
                openPipe.write(message)
            break
        except:
            time.sleep(1)


def readFromFile(file):
    while True:
        try:
            with open(file, 'r') as openPipe:
                value = openPipe.read()
            if 'target_term' in value:
                break
            else:
                time.sleep(1)
        except:
            time.sleep(1)
    return value


def find_terms(def_terms, targ_term):
    definition = def_terms[0]
    set_terms = def_terms[1]
    array_terms = []

    for term in set_terms:
        if term.lower() in definition.lower() and term.lower() != targ_term.lower():
            array_terms += [term]

    return array_terms


def find_term_definition(json_object):
    target = json_object['target_term']
    definition_array = json_object['terms_and_definitions']
    target_definition = ''
    term_set = set()

    for value in definition_array:
        if value['term'] == target:
            target_definition = value['definition']
        term_set.add(value['term'])
    return target_definition, term_set


def parse_text(text_to_parse):
    # Define regular expression patterns to extract the target term and definitions
    term_pattern = r'\["(.+?)"\]'
    # def_pattern = r'"(.+?)"\s*=\s*"(.+?)"'
    def_pattern = r'"(.+?)"\s*=\s*"((?:.|\n)+?)"'

    # Use the search() method to find the target term in the text
    term_match = re.search(term_pattern, text_to_parse)
    target_term = term_match.group(1)

    # Use the findall() method to extract the definitions as a list of tuples
    def_matches = re.findall(def_pattern, text_to_parse)
    # print(def_matches)
    definitions = [{"term": term, "definition": definition} for term, definition in def_matches]

    # Build the final dictionary with the extracted data
    result = {"target_term": target_term, "terms_and_definitions": definitions}

    # Convert the dictionary to a JSON object and print it
    json_result = json.dumps(result, indent=4)
    json_object = json.loads(json_result)
    # print(json_object['terms_and_definitions'][0]['definition'])
    return json_object


while True:
    message = readFromFile(ROSPipe)

    json_obj = parse_text(message)
    targ_def_and_terms = find_term_definition(json_obj)
    array_of_terms_found = find_terms(targ_def_and_terms, json_obj['target_term'])

    message = 'related_terms = ' + str(array_of_terms_found)
    writeToFile(ROSPipe, message)
    print(array_of_terms_found)


