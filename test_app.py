import subprocess

def test_script_runs():
    """Verifica che app.py si esegua senza errori."""
    result = subprocess.run(["python", "app.py"], input="no\n", text=True, capture_output=True)
    assert "Let's start!" in result.stdout
