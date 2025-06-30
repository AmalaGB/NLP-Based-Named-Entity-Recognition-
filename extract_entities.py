import re
import json
import spacy

nlp = spacy.load("en_core_web_sm")

issue_patterns = [
    r"overheat(?:ing)?", r"flicker(?:ing)?", r"shut(?:ting)? down", r"lag(?:ging)?",
    r"battery (?:draining|issue)", r"slow performance", r"screen freeze"
]
issue_regex = re.compile("|".join(issue_patterns), re.IGNORECASE)

def extract_entities(text):
    doc = nlp(text)
    entities = []

    for match in issue_regex.finditer(text):
        start, end = match.start(), match.end()
        span = doc.char_span(start, end, label="ISSUE")
        if span:
            entities.append((span.start_char, span.end_char, "ISSUE"))
    return entities

with open("data/complaints.json", "r") as f:
    complaints = json.load(f)

annotated_data = []
for c in complaints:
    text = c["complaint"]
    ents = extract_entities(text)
    annotated_data.append((text, {"entities": ents}))

with open("data/processed_complaints.json", "w") as f:
    json.dump(annotated_data, f, indent=2)
