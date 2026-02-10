# Spam Detection App

A **Flask-based Spam Detection application** using Machine Learning to classify emails or text as **Spam** or **Not Spam (Ham)**.  
It also supports **live email checking simulation** and manual text input for testing.  

---

## 🌐 Live Demo

Try it online here: [Spam Detection Live](https://spam-detection-43wv.onrender.com/)

---

## 🛠 Features

- **Manual Text Check:** Enter any text to see if it's spam or not.
- **Check Most Recent Email:** Quickly check the latest email fetched by the system.
- **Live Simulation:** Automatically checks incoming emails every 10 seconds in the background.
- **Simple and Clean UI** using HTML templates.
- **Machine Learning Powered:** Uses a trained model (`model.pkl`) and a text vectorizer (`tv.pkl`) for predictions.

---

## 📦 Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn (Pickle for model serialization)
- **Frontend:** HTML, CSS (Jinja templates)
- **Deployment:** [Render](https://render.com/)

---

## 🚀 Installation & Setup (Local)

1. **Clone the repository**  
```bash
git clone <your-repo-link>
cd <repo-folder>
