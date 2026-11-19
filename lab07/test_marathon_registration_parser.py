from hypothesis import given, settings, strategies as st

from marathon_registration_parser import (
    average_split,
    format_bib_name,
    parse_finish_time,
)


# Hypothesis fuzz tests: invalid or unexpected input should not crash.
@settings(max_examples=200)
@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.integers())))
def test_format_bib_name_handles_unexpected_inputs(value):
    result = format_bib_name(value)
    assert isinstance(result, str)
    assert len(result) <= 12


@settings(max_examples=300)
@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.integers())))
def test_parse_finish_time_handles_unexpected_inputs(value):
    result = parse_finish_time(value)
    assert result is None or isinstance(result, int)


@settings(max_examples=300)
@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.integers())))
def test_average_split_handles_unexpected_inputs(value):
    result = average_split(value)
    assert result is None or isinstance(result, float)


# Valid-input properties.
@given(st.text())
def test_bib_name_is_trimmed_uppercased_and_limited(value):
    result = format_bib_name(value)
    assert result == value.strip().upper()[:12]


@given(
    st.integers(min_value=0, max_value=999),
    st.integers(min_value=0, max_value=59),
    st.integers(min_value=0, max_value=59),
)
def test_valid_finish_time_conversion(hours, minutes, seconds):
    value = f"{hours}:{minutes:02d}:{seconds:02d}"
    assert parse_finish_time(value) == hours * 3600 + minutes * 60 + seconds


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def test_valid_split_average(values):
    text = " ".join(map(str, values))
    assert average_split(text) == sum(values) / len(values)
