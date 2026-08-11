"""
Count the total number of tokens across all files in the corpus/ directory.

Usage:
    pip install tiktoken
    python3 count_tokens.py

By default this counts tokens for every file in ../corpus using the
"cl100k_base" encoding (the tokenizer used by GPT-3.5/GPT-4 models).
"""

import glob
import os

import tiktoken

# Directory containing the corpus files, relative to this script.
CORPUS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")

# Encoding used by GPT-3.5 / GPT-4 models. Swap this if you want a
# different model's tokenizer (e.g. "o200k_base" for GPT-4o).
ENCODING_NAME = "cl100k_base"


# Per-file breakdown version — kept "just in case" but commented out since
# it takes noticeably longer to run and the breakdown usually isn't needed.
# Uncomment and call this instead of count_total_tokens() if you want to see
# the token count for each individual file.
#
# def count_tokens_in_corpus(corpus_dir: str, encoding_name: str) -> None:
#     encoding = tiktoken.get_encoding(encoding_name)
#
#     total_tokens = 0
#     file_count = 0
#
#     for file_path in sorted(glob.glob(os.path.join(corpus_dir, "*"))):
#         # Skip anything that isn't a regular file (e.g. .DS_Store, subfolders).
#         if not os.path.isfile(file_path) or file_path.endswith(".DS_Store"):
#             continue
#echo ".DS_Store" >> .gitignore
#         with open(file_path, encoding="utf-8", errors="ignore") as f:
#             text = f.read()
#
#         token_count = len(encoding.encode(text))
#         total_tokens += token_count
#         file_count += 1
#
#         print(f"{os.path.basename(file_path):<55} {token_count:>8,} tokens")
#
#     print("-" * 72)
#     print(f"Files counted: {file_count}")
#     print(f"Total tokens ({encoding_name}): {total_tokens:,}")


def count_total_tokens(corpus_dir: str, encoding_name: str) -> None:
    """Print only the grand total token count across all corpus files."""
    encoding = tiktoken.get_encoding(encoding_name)

    total_tokens = 0
    file_count = 0

    for file_path in sorted(glob.glob(os.path.join(corpus_dir, "*"))):
        # Skip anything that isn't a regular file (e.g. .DS_Store, subfolders).
        if not os.path.isfile(file_path) or file_path.endswith(".DS_Store"):
            continue

        with open(file_path, encoding="utf-8", errors="ignore") as f:
            text = f.read()

        total_tokens += len(encoding.encode(text))
        file_count += 1

    print(f"Files counted: {file_count}")
    print(f"Total tokens ({encoding_name}): {total_tokens:,}")


if __name__ == "__main__":
    count_total_tokens(CORPUS_DIR, ENCODING_NAME)