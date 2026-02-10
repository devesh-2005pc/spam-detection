import random

dummy_emails = [
    ("Meeting Reminder",
     "Hi Devesh, please attend the project meeting tomorrow at 10 AM."),

    ("Lottery Winner!!!",
     "Congratulations! You have won 10 lakh rupees. Click here to claim now."),

    ("Internship Shortlisted",
     "We are pleased to inform you that you have been shortlisted for the internship."),

    ("Urgent Account Suspension",
     "Your bank account has been suspended. Verify immediately by clicking this link."),

    ("Amazon Big Sale",
     "Limited time offer! Get 80 percent discount on electronics. Shop now."),

    ("Team Lunch",
     "Hey team, we are planning lunch at 1 PM today. Please confirm your availability.")
]

def read_latest():
    return random.choice(dummy_emails)
