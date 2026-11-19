import pytest
from marathon_registration import entry_fee, start_wave, finisher_status


# Entry fee tests: base prices, discounts, add-ons, and validation.
@pytest.mark.parametrize(
    ("race", "expected"),
    [("5k", 500), ("10k", 800), ("half", 1200), ("full", 1800)],
)
def test_base_entry_fees(race, expected):
    assert entry_fee(race, 30, False, False) == expected


def test_early_bird_discount():
    assert entry_fee("5k", 30, True, False) == 375


def test_senior_discount():
    assert entry_fee("5k", 65, False, False) == 250


def test_tshirt_charge():
    assert entry_fee("5k", 30, False, True) == 800


def test_combined_discounts_and_tshirt():
    assert entry_fee("10k", 65, True, True) == 600


@pytest.mark.parametrize(
    ("race", "age"),
    [("unknown", 30), ("5k", 11), ("half", 17), ("full", 17)],
)
def test_invalid_race_or_age(race, age):
    with pytest.raises(ValueError):
        entry_fee(race, age, False, False)


def test_minimum_age_and_long_race_age_boundary():
    assert entry_fee("5k", 12, False, False) == 500
    assert entry_fee("full", 18, False, False) == 1800


# Start-wave tests: no previous time, A/B/C decisions and boundaries.
def test_first_timer_wave():
    assert start_wave(None, "full") == "D"


@pytest.mark.parametrize(
    ("time", "race", "expected"),
    [
        (180, "full", "A"),
        (181, "full", "B"),
        (240, "full", "B"),
        (241, "full", "C"),
        (90, "10k", "A"),
        (100, "10k", "B"),
        (120, "10k", "B"),
        (121, "10k", "C"),
    ],
)
def test_start_wave_boundaries(time, race, expected):
    assert start_wave(time, race) == expected


# Finisher tests: disqualification takes precedence over the time limit.
@pytest.mark.parametrize(
    ("elapsed", "race"),
    [(90, "5k"), (180, "half"), (360, "full")],
)
def test_finisher_at_time_limit(elapsed, race):
    assert finisher_status(elapsed, race, 0) == "finisher"


@pytest.mark.parametrize(
    ("elapsed", "race"),
    [(91, "5k"), (181, "half"), (361, "full")],
)
def test_dnf_after_time_limit(elapsed, race):
    assert finisher_status(elapsed, race, 0) == "DNF"


def test_disqualification_precedes_time_result():
    assert finisher_status(50, "5k", 1) == "DSQ"
    assert finisher_status(400, "full", 2) == "DSQ"
