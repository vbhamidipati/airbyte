#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

import pytest
from octavia_cli.list import formatting


@pytest.mark.parametrize(
    "test_data,padding,expected_col_width",
    [([["a", "___10chars"], ["e", "f"]], 2, 2 + 10), ([["a", "___10chars"], ["e", "____11chars"]], 2, 2 + 11), ([[""]], 2, 2)],
)
def test_compute_col_width(test_data, padding, expected_col_width):
    col_width = formatting.compute_col_width(test_data, padding)
    assert col_width == expected_col_width


@pytest.mark.parametrize("input_camelcased,expected_output", [("camelCased", "CAMEL CASED"), ("notcamelcased", "NOTCAMELCASED")])
def test_camelcased_to_uppercased_spaced(input_camelcased, expected_output):
    assert formatting.camelcased_to_uppercased_spaced(input_camelcased) == expected_output


@pytest.mark.parametrize(
    "test_data,col_width,expected_output",
    [
        ([["a", "___10chars"], ["e", "____11chars"]], 13, "a            ___10chars   \ne            ____11chars  "),
    ],
)
def test_display_as_table(mocker, test_data, col_width, expected_output):
    mocker.patch.object(formatting, "compute_col_width", mocker.Mock(return_value=col_width))
    assert formatting.display_as_table(test_data) == expected_output


def test_format_column_names(mocker):
    columns_to_format = ["camelCased"]
    formatted_columns = formatting.format_column_names(columns_to_format)
    assert len(formatted_columns) == 1
    for i, c in enumerate(formatted_columns):
        assert c == formatting.camelcased_to_uppercased_spaced(columns_to_format[i])
