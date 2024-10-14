import textwrap

def wrap_labels(labels, width=20):
    """
    Wrap text to a specified width for visualisation purposes.
    
    Parameters:
    labels (list): List of strings to wrap.
    width (int): The maximum number of characters per line.
    
    Returns:
    list: A list of wrapped labels.
    """
    return [textwrap.fill(label, width) for label in labels]