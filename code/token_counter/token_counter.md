# Token Counter

A simple utility for estimating token usage using `tiktoken`.

This helps understand how many tokens a piece of text consumes before sending it to an LLM.

You can use similar logic in real AI applications to measure:
- user input tokens
- system prompt tokens
- conversation history
- model response tokens

This becomes useful for:
- estimating API cost
- preventing context overflow
- monitoring token usage
- optimizing prompts

---

## Install

```bash
pip install tiktoken
