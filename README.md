# LingPatLab: Linguistic Pattern Laboratory

## Overview

LingPatLab is a robust API designed to perform advanced Natural Language Processing (NLP) tasks, utilizing the capabilities of the spaCy library. This tool is expertly crafted to convert raw textual data into structured, analyzable forms. It is ideal for developers, researchers, and linguists who require comprehensive processing capabilities, from tokenization to sophisticated text summarization.

## Features

- **Tokenization**: Splits raw text into individual tokens.
- **Parsing**: Analyzes tokens to construct sentences with detailed linguistic annotations.
- **Phrase Extraction**: Identifies and extracts significant phrases from sentences.
- **Text Summarization**: Produces concise summaries of input text, optionally leveraging extracted phrases.

## Usage

To get started with LingPatLab, you can set up the API as follows:

```python
from spacy_core.api import SpacyCoreAPI

api = LingPatLab()
```

### Tokenization and Parsing

To tokenize and parse input text into structured sentences:

```python
parsed_sentence: Sentence = api.parse_input_text("Your input text here.")
print(parsed_sentence.to_string())
```

### Phrase Extraction

To extract phrases from a structured Sentences object:

```python
phrases: List[str] = api.extract_topics(parsed_sentences)
for phrase in phrases:
    print(phrase)
```

### Summarization

To generate a summary of the input text:

```python
summary: str = api.generate_summary("Your input text here.")
print(summary)
```

### Data Classes

LingPatLab utilizes several custom data classes to structure the data throughout the NLP process:

- `Sentence`: Represents a single sentence, containing a list of tokens (`SpacyResult` objects).
- `Sentences`: Represents a collection of sentences, useful for processing paragraphs or multiple lines of text.
- `SpacyResult`: Encapsulates the detailed analysis of a single token, including part of speech, dependency relations, and additional linguistic features.
- `OtherInfo`: Contains additional information about a token, particularly in relation to its syntactic head.
