#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

from typing import List


def compute_col_width(data: List[List[str]], padding: int = 2) -> int:
    """Compute column width for display purposes:
    Find largest column size, add a padding of two characters.
    Returns:
        data (List[List[str]]): Tabular data containing rows and columns.
        padding (int): Number of character to adds to create space between columns.
    Returns:
        col_width (int): The computed column width according to input data.
    """
    col_width = max(len(col) for row in data for col in row) + padding
    return col_width


def camelcased_to_uppercased_spaced(camelcased: str) -> str:
    """Util function to transform a camelCase string to a UPPERCASED SPACED string
    e.g: dockerImageName -> DOCKER IMAGE NAME
    Args:
        camelcased (str): The camel cased string to convert.

    Returns:
        (str): The converted UPPERCASED SPACED string
    """
    return "".join(map(lambda x: x if x.islower() else " " + x, camelcased)).upper()


def display_as_table(data: List[List[str]]) -> str:
    """Formats tabular input data into a displayable table with columns.
    Args:
        data (List[List[str]]): Tabular data containing rows and columns.
    Returns:
        table (str): String representation of input tabular data.
    """
    col_width = compute_col_width(data)
    table = "\n".join(["".join(col.ljust(col_width) for col in row) for row in data])
    return table


def format_column_names(camelcased_column_names: List[str]) -> List[str]:
    """Format camel cased column names to uppercased spaced column names

    Args:
        camelcased_column_names (List[str]): Column names in camel case.

    Returns:
        (List[str]): Column names in uppercase with spaces.
    """
    return [camelcased_to_uppercased_spaced(column_name) for column_name in camelcased_column_names]
