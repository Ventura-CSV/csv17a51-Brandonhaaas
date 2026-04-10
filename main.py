from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    # === TODO ===
    # Your code here
    domain : set = set()
    for x in mapping.keys():
        domain.add(x)
    return domain
    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    # === TODO ===
    # Your code here
    range : set = set()
    for y in mapping.values():
        range.add(y)
    return range
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # === TODO ===
    # Your code here
    return get_range(mapping).issubset(target)
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # === TODO ===
    # Your code here
    hashset : set = set()
    for value in mapping.values():
        if value in hashset:
            return False
        hashset.add(value)
    return True
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    # === TODO ===
    # Your code here
    return get_range(mapping) == target
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
