import pytest
from marathon_registration import entry_fee, start_wave, finisher_status


def test_entry_fee_base_prices_and_discount_lines():
    assert entry_fee("5k", 30, False, False) == 500
    assert entry_fee("10k", 30, True, False) == 600
    assert entry_fee("5k", 65, False, False) == 250
    assert entry_fee("5k", 30, False, True) == 800


def test_entry_fee_validation_lines():
    with pytest.raises(ValueError):
        entry_fee("unknown", 30, False, False)
    with pytest.raises(ValueError):
        entry_fee("5k", 11, False, False)
    with pytest.raises(ValueError):
        entry_fee("half", 17, False, False)


def test_start_wave_lines():
    assert start_wave(None, "full") == "D"
    assert start_wave(180, "full") == "A"
    assert start_wave(200, "full") == "B"
    assert start_wave(250, "full") == "C"


def test_finisher_status_lines():
    assert finisher_status(100, "5k", 1) == "DSQ"
    assert finisher_status(90, "5k", 0) == "finisher"
    assert finisher_status(181, "half", 0) == "DNF"
    assert finisher_status(360, "full", 0) == "finisher"
