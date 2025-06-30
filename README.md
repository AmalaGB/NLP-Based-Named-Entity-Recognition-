# NLP-Based-Named-Entity-Recognition-

# Custom NER System for Consumer Electronics Complaints

This project builds a domain-specific Named Entity Recognition (NER) model using SpaCy and Regular Expressions (RegEx) to identify key entities in consumer complaint text, especially within the electronics domain (laptops, mobiles, TVs, etc.).

## Overview

The system is designed to:
- Automatically label entities such as `BRAND`, `PROCESSOR`, `STORAGE`, `ISSUE`, etc.
- Avoid manual annotation using a hybrid approach: SpaCy's pre-trained NER + RegEx.
- Train a custom NER model with a strong F1-score (~93%).

## Project Structure

- `data/`: Raw, annotated, and processed JSON files
- `scripts/`: Python scripts for entity extraction, training, and evaluation
- `training/`: `.spacy` files for training/validation and config
- `models/`: Saved custom NER model
- `requirements.txt`: Required Python packages

