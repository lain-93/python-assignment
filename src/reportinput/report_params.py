import sys
import re
from typing import List, Set


def gen_params(a , b) -> List[str]:
    a = a.strip()
    b = b.strip()

    if not a or not b:
        print("a or b is empty.")
        sys.exit(1)
    
    a_items: List[str] = extract_items(a)
    b_items: List[str] = extract_items(b)

    return extract_common_items(a_items, b_items)


def extract_items(a: str) -> List[str]:
    items = re.findall(r'\b\w+\b', a, flags=re.IGNORECASE)
    return [item.lower() for item in items]


def extract_common_items(a: List[str], b: List[str]) -> List[str]:
    return list(set(a) & set(b))