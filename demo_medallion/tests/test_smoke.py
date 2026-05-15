"""Smoke tests for SCRUM-65 package bootstrap."""

import demo_medallion


def test_package_import():
    assert demo_medallion.__name__ == "demo_medallion"


def test_version_defined():
    assert demo_medallion.__version__


def test_output_root_placeholder():
    from demo_medallion import paths

    assert isinstance(paths.DEFAULT_OUTPUT_ROOT, str)
    assert len(paths.DEFAULT_OUTPUT_ROOT) > 0
