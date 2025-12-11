# test_cli.py
import pytest
from click.testing import CliRunner
from Lab1.cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_predict_command(runner, tmp_path):
    # Create a dummy file to serve as img_path
    img_file = tmp_path / "dummy.jpg"
    img_file.write_text("fake image content")

    result = runner.invoke(cli, ["predict", str(img_file)])
    assert result.exit_code == 0
    assert "Prediction:" in result.output


def test_rescale_command(runner, tmp_path):
    # Create a dummy file to serve as img_path
    img_file = tmp_path / "dummy.jpg"
    img_file.write_text("fake image content")

    result = runner.invoke(cli, ["rescale", str(img_file), "128"])
    assert result.exit_code == 0
    assert f"Rescaled {img_file} to 128x128" in result.output
