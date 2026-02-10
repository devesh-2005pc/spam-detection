from flask import Flask, render_template, request, redirect, url_for
from pickle import load
from reader import read_latest
import threading
import time

app = Flask(__name__)

# ---------------- LOAD ML MODEL ---------------- #

with open("model.pkl", "rb") as f:
    model = load(f)

with open("tv.pkl", "rb") as f:
    tv = load(f)


# ---------------- SIMPLE CLEAN FUNCTION ---------------- #

def clean_function(text):
    if not text:
        return ""
    return text.lower()


# ---------------- LIVE SIMULATION ---------------- #

latest_body = None
latest_subject = None
latest_result = None
started = False


def live_checker():
    global latest_body, latest_subject, latest_result

    while True:
        subject, body = read_latest()

        if body and body != latest_body:
            latest_body = body
            latest_subject = subject

            clean_body = clean_function(body)
            vector_body = tv.transform([clean_body])
            result = model.predict(vector_body)[0]

            if result.lower() == "ham":
                latest_result = "Not Spam"
            else:
                latest_result = "Spam"

        time.sleep(10)


@app.route("/live")
def live():
    global started
    if not started:
        started = True
        threading.Thread(target=live_checker, daemon=True).start()

    return redirect(url_for("live_status"))


@app.route("/live-status")
def live_status():
    return render_template(
        "home.html",
        subject=latest_subject,
        body=latest_body,
        result=latest_result,
        live_mode=True
    )


# ---------------- CHECK RECENT ---------------- #

@app.route("/check-recent")
def check():
    subject, body = read_latest()

    if not body:
        return render_template("home.html", result="No Email Found")

    clean_body = clean_function(body)
    vector_body = tv.transform([clean_body])
    result = model.predict(vector_body)[0]

    if result.lower() == "ham":
        result = "Not Spam"
    else:
        result = "Spam"

    return render_template(
        "home.html",
        result=result,
        body=body,
        subject=subject
    )


# ---------------- MANUAL TEXT CHECK ---------------- #

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text")

        clean_text = clean_function(text)
        vector_text = tv.transform([clean_text])
        result = model.predict(vector_text)[0]

        if result.lower() == "ham":
            result = "Not Spam"
        else:
            result = "Spam"

        return render_template("home.html", result=result)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
