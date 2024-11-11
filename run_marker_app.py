import os
import subprocess


def run():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(cur_dir, "marker_app.py")
    cmd = ["streamlit", "run", app_path, "--server.port", "9199", "--server.address", "0.0.0.0"]
    subprocess.run(cmd, env={**os.environ, "IN_STREAMLIT": "true", "PDFTEXT_CPU_WORKERS": "1"})


if __name__ == "__main__":
    run()
