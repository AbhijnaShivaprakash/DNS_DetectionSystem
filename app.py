from flask import Flask, render_template
from logger import read_logs
from collections import Counter

app = Flask(__name__)

@app.route("/")
def home():
    logs = read_logs()

    packet_count = len(logs)
    redirect_count = len(logs)

    status = "Running" if packet_count > 0 else "Stopped"

    alert = ""
    if packet_count > 40:
        alert = "⚠ Suspicious DNS Traffic Volume Detected"

    domain_counter = Counter()

    for log in logs:
        parts = log.split("|")
        if len(parts) >= 2:
            domain = parts[1].strip()
            domain_counter[domain] += 1

    labels = list(domain_counter.keys())
    values = list(domain_counter.values())

    return render_template(
        "index.html",
        status=status,
        packets=packet_count,
        spoofed=redirect_count,
        logs=reversed(logs),
        alert=alert,
        labels=labels,
        values=values
    )

if __name__ == "__main__":
    app.run(debug=True)
