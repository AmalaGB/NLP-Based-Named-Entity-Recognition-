import spacy
from spacy.scorer import Scorer
from spacy.tokens import DocBin

nlp = spacy.load("models/custom_ner_model")
db = DocBin().from_disk("training/train.spacy")
docs = list(db.get_docs(nlp.vocab))

scorer = Scorer()
results = scorer.score(docs)
print(results)
