import pytest

# Refer to: https://docs.pytest.org/en/latest/example/simple.html
def pytest_addoption(parser):
    # Skipping Slow test
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )
    # Skipping test containing API call
    parser.addoption(
        "--runapi", action="store_true", default=False, help="run tests containing API call"
    )
    # Skipping Data Generation functions
    parser.addoption(
        "--rundatagen", action="store_true", default=False, help="run data generation"
    )

# def pytest_collection_modifyitems(config, items):
def pytest_collection_modifyitems(config, items):
    if not config.getoption("--rundatagen"):
        # --rundatagen not given in cli: skip data generation
        skip_datagen = pytest.mark.skip(reason="need --rundatagen option to run")
        for item in items:
            if "datagen" in item.keywords:
                item.add_marker(skip_datagen)

    if not config.getoption("--runslow"):
        # --runslow not given in cli: skip slow tests
        skip_slow = pytest.mark.skip(reason="need --runslow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)

    if not config.getoption("--runapi"):
        # --runapi not given in cli: skip tests containing API call
        skip_api = pytest.mark.skip(reason="need --runapi option to run")
        for item in items:
            if "api" in item.keywords:
                item.add_marker(skip_api)

    return
