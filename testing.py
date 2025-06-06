"""
This module demonstrates a simple greeting function.
"""

def greet(name: str) -> str:
    """
    Return a greeting message for the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
