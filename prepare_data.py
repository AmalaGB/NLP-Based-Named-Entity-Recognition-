import spacy
from spacy.tokens import DocBin
import json

nlp = spacy.blank("en")
doc_bin = DocBin()

with open("data/processed_complaints.json", "r") as f:
    data = json.load(f)

for text, annot in data:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label)
        if span:
            ents.append(span)
    doc.ents = ents
    doc_bin.add(doc)

doc_bin.to_disk("training/train.spacy")
