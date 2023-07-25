import json
import re
import spacy
from bs4 import BeautifulSoup


nlp = spacy.load('en_core_web_sm')

# we're scrubbing markdown
curly_braces_pattern = r'\{.*?\}'

unicode_characters_pattern = r'\\u[0-9a-fA-F]+'

spaces_pattern = r'\s{2,}'

double_backslash_pattern = r'\\\\([^ ]+)'


def remove_within_curly_braces(text):
    return re.sub(curly_braces_pattern, '', text)

def remove_unicode_characters(text):
    return re.sub(unicode_characters_pattern, '', text)

def remove_consecutive_spaces(text):
    return re.sub(spaces_pattern, '', text)

def remove_double_backslash_tokens(text):
    return re.sub(double_backslash_pattern, '', text)

def remove_strings_with_double_pipe(text):
    return re.sub(r'\|\|.*?\|\|', '', text)

def remove_words_with_double_braces(text):
    return re.sub(r'\b\w*(?:\{\{|}})\w*\b', '', text)

def remove_irrelevant_text(text):
    # Parse the text with spaCy
    doc = nlp(text)

    # Create a list of tokens to keep
    relevant_tokens = []
    for token in doc:
        # Filter out irrelevant entities and parts of speech
        if not token.is_space and not token.is_punct and not token.is_digit and not token.is_stop:
            relevant_tokens.append(token.text)

    # Join the relevant tokens back into a clean text
    clean_text = ' '.join(relevant_tokens)
    return clean_text

def remove_script_style_elements(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    return soup.get_text()

# Save the documents as a JSON file
with open('wikipedia_entries.json', 'r', encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

print(type(json_data))

updated_json_data = {}

for k, v in json_data.items():

    cleaned_html = remove_script_style_elements(v)
    stripped_val = cleaned_html.replace('\n', '')
    # Remove content within curly braces
    cleaned_val = remove_within_curly_braces(stripped_val)
    # Remove any Unicode characters

    cleaned_val = remove_unicode_characters(cleaned_val)

    # Remove three or more consecutive spaces
    cleaned_val = remove_consecutive_spaces(cleaned_val)

    cleaned_val = remove_double_backslash_tokens(cleaned_val)

    cleaned_val = remove_strings_with_double_pipe(cleaned_val)

    cleaned_val = remove_words_with_double_braces(cleaned_val)


    cleaned_val = cleaned_val.encode("ascii", "ignore")
    cleaned_val = cleaned_val.decode()

    updated_json_data[k] = cleaned_val


updated_wiki_json = json.dumps(updated_json_data)


with open('scrubbed_wiki_data.json', 'w') as json_file_new:
    json.dump(updated_json_data, json_file_new, ensure_ascii=True)
