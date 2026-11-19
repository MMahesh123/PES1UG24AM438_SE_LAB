import pytest
from marathon_registration import entry_fee, start_wave, finisher_status


# entry_fee: valid/invalid race, both age checks, discounts and add-on.
def test_entry_fee_true_and_false_branches():
    assert entry_fee("5k", 12, False, False) == 500
    assert entry_fee("5k", 64, True, False) == 375
    assert entry_fee("5k", 65, False, True) == 550
    assert entry_fee("half", 18, False, False) == 1200
    assert entry_fee("full", 18, True, True) == 1650

    with pytest.raises(ValueError):
        entry_fee("other", 30, False, False)
    with pytest.raises(ValueError):
        entry_fee("10k", 11, False, False)
    with pytest.raises(ValueError):
        entry_fee("half", 17, False, False)


# start_wave: D/A/B/C and both cutoff calculations.
@pytest.mark.parametrize(
    ("best_time", "race", "expected"),
    [
        (None, "full", "D"),
        (180, "full", "A"),
        (181, "full", "B"),
        (240, "full", "B"),
        (241, "full", "C"),
        (90, "10k", "A"),
        (100, "10k", "B"),
        (121, "10k", "C"),
    ],
)
def test_start_wave_all_branches(best_time, race, expected):
    assert start_wave(best_time, race) == expected


# finisher_status: DSQ has priority; then full/half/other time limits.
@pytest.mark.parametrize(
    ("elapsed", "race", "missed", "expected"),
    [
        (50, "5k", 1, "DSQ"),
        (90, "5k", 0, "finisher"),
        (91, "5k", 0, "DNF"),
        (180, "half", 0, "finisher"),
        (181, "half", 0, "DNF"),
        (360, "full", 0, "finisher"),
        (361, "full", 0, "DNF"),
        (90, "10k", 0, "finisher"),
        (91, "10k", 0, "DNF"),
    ],
)
def test_finisher_status_all_branches(elapsed, race, missed, expected):
    assert finisher_status(elapsed, race, missed) == expected
