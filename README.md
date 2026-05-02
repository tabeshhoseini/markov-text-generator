# Markov Chain Text Generator

A simple Python script that learns from any text file and generates new text using a trigram Markov chain.

## What is a Markov chain?

A system that predicts the next word based on the previous two words. It learns probabilities from your text, then walks through them to create new sequences.

**Example:** After seeing "the cat sat" → it learns that "the cat" is followed by "sat". Then "cat sat" might be followed by "on", and so on.

**Why it matters:** This is the same core idea behind LLMs like GPT — predict the next token from previous ones. Markov chains are the simple, transparent version.

## How to run

1. Replace `sample.txt` with any long `.txt` file (book, article, your own writing)
2. Run the script:
   ```bash
   python main.py
