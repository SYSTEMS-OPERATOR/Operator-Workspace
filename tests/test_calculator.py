import subprocess
import sys
from pathlib import Path


def test_e8_calculator_cli():
    script = Path(__file__).resolve().parents[1] / "scripts" / "e8_calculator.py"
    cmd = [sys.executable, str(script), "1", "0", "0", "0", "0", "0", "0", "0"]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )
    value = float(result.stdout.strip())
    assert value == 1.0
