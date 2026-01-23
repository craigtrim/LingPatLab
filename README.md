# LingPatLab

[![PyPI version](https://badge.fury.io/py/lingpatlab.svg)](https://badge.fury.io/py/lingpatlab)
[![Downloads](https://static.pepy.tech/badge/lingpatlab)](https://pepy.tech/project/lingpatlab)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: autopep8](https://img.shields.io/badge/code%20style-autopep8-blue.svg)](https://github.com/hhatto/autopep8)
[![spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)

> Linguistic Pattern Laboratory: Advanced NLP pipeline for text analysis, entity extraction, and pattern recognition.

## Features

- **Tokenization**: Custom Graffl tokenizer with intelligent handling of contractions, abbreviations, and punctuation
- **Parsing**: Deep linguistic analysis with POS tagging, dependency parsing, and WordNet integration
- **Entity Extraction**: Pattern-based extraction of people and topics with anaphora resolution
- **Segmentation**: Paragraph and sentence boundary detection
- **Rich Annotations**: Sentiment, lemmatization, stemming, and morphological features

## Installation

```bash
pip install lingpatlab
```

## Quick Start

```python
from lingpatlab import LingPatLab

api = LingPatLab()

# Parse text into structured tokens
sentence = api.parse_input_text("Admiral Nimitz commanded the Pacific Fleet.")
print(sentence.to_string())

# Extract people with anaphora resolution
text = "Admiral William Halsey led the fleet. Halsey was known for his aggressive tactics."
sentence = api.parse_input_text(text)
people = api.extract_people(sentence)
# Returns: {'Halsey': ['Admiral William Halsey', 'Halsey']}

# Extract topics and named entities
topics = api.extract_topics(sentence)
```

## Usage Examples

### Parse Multiple Lines

```python
lines = [
    "The Battle of Midway was a turning point.",
    "Admiral Nimitz made crucial decisions."
]
sentences = api.parse_input_lines(lines)

for sentence in sentences:
    print(sentence.to_string())
```

### Segmentation

```python
from lingpatlab import segment_input_text

text = "First sentence. Second sentence. Third sentence."
segments = segment_input_text(text)
# Returns: ['First sentence.', 'Second sentence.', 'Third sentence.']
```

### Access Token Details

```python
sentence = api.parse_input_text("The quick brown fox jumps.")

for token in sentence:
    print(f"Text: {token.text}")
    print(f"POS: {token.pos}")
    print(f"Lemma: {token.normal}")
    print(f"Is WordNet: {token.is_wordnet}")
    print(f"Dependency: {token.dep}")
```

## Data Classes

- **`Sentence`**: Single sentence with token list
- **`Sentences`**: Collection of sentences
- **`SpacyResult`**: Individual token with full linguistic annotation
- **`OtherInfo`**: Additional morphological and dependency metadata

## Architecture

```
LingPatLab
├── tokenizer/     # Custom tokenization with Graffl
├── parser/        # spaCy integration + enhancements
├── analyzer/      # Entity extraction with pattern matching
├── segmenter/     # Sentence and paragraph segmentation
└── utils/         # WordNet, Porter stemmer, utilities
```

## Requirements

- Python 3.10+
- spaCy 3.8.2
- spaCy model: `en_core_web_sm`

## Development

```bash
# Install with dev dependencies
pip install -e ".[linting,testing]"

# Run tests
pytest

# Run regression suite
python regression/regression_runner.py
```

## Links

- [PyPI Package](https://pypi.org/project/lingpatlab/)
- [GitHub Repository](https://github.com/craigtrim/lingpatlab)
- [Issue Tracker](https://github.com/craigtrim/lingpatlab/issues)

## License

MIT License - see [LICENSE](https://github.com/craigtrim/lingpatlab/blob/master/LICENSE) for details.

## Author

**Craig Trim** - [craigtrim@gmail.com](mailto:craigtrim@gmail.com)

More NLP articles and demos at [craigtrim.com](http://craigtrim.com/)
