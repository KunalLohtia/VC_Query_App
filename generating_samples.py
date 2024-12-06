# from faker import Faker
# import random

# # Initialize Faker
# fake = Faker()

# # Investment-related keywords and phrases
# investment_phrases = [
#     "investment opportunity", "stocks", "bonds", "financial growth",
#     "mutual funds", "retirement savings", "crypto assets", "real estate",
#     "equity markets", "dividends", "venture capital", "portfolio management",
#     "diversified portfolio", "fixed-income securities", "wealth maximization",
#     "retirement planning", "long-term investments", "short-term gains",
#     "asset allocation", "financial independence", "market trends",
#     "tax-efficient investing", "blue-chip stocks", "emerging markets",
#     "hedge funds", "private equity", "capital growth", "sustainable investing",
#     "ESG investments", "growth opportunities", "financial literacy",
#     "passive income", "high-yield savings", "index funds", "commodities",
#     "economic forecasts", "financial advisors", "smart money decisions"
# ]

# # General non-investment content topics
# non_investment_topics = [
#     "meeting schedule", "family updates", "travel plans", "event reminders",
#     "friendship messages", "team collaborations", "general inquiries", "casual chats"
# ]

# # Greeting lines
# greetings = [
#     "Dear {name},", "Hi {name},", "Hello,", "Good day,", "Dear Friend,"
# ]

# # Random content generators
# investment_details = [
#     "Our analysts predict a return of {percentage}% within {duration} months.",
#     "We offer exclusive access to {opportunity} with minimal risk.",
#     "This is the perfect time to invest in {sector}.",
#     "Diversify your portfolio with high-yield assets like {asset}.",
#     "Secure your financial future with expert guidance and {strategy}.",
#     "This exclusive opportunity is tailored to meet your financial goals.",
#     "Seize this moment to diversify your portfolio effectively.",
#     "Our experts have identified high-potential assets for rapid growth.",
#     "Benefit from our advanced market insights and proven strategies.",
#     "Explore stable returns through tax-efficient investment solutions.",
#     "Unlock access to exclusive hedge fund opportunities.",
#     "Take advantage of low-risk, high-reward options in emerging markets.",
#     "Our portfolio management services ensure your investments thrive.",
#     "Maximize your wealth through structured asset allocation."
# ]

# non_investment_details = [
#     "Looking forward to our meeting on {date}.",
#     "Here are the details of our travel plan to {destination}.",
#     "Just checking in to see how you are doing!",
#     "Can you share the agenda for the upcoming event?",
#     "Let's catch up soon over a call.",
#     "Don't forget to RSVP for the upcoming event by {date}.",
#     "Let’s finalize the travel itinerary for our trip to {destination}.",
#     "Please share your availability for a quick catch-up call.",
#     "Looking forward to your feedback on the project discussion.",
#     "Here's a quick update on our upcoming team collaboration.",
#     "Hope all is well! Let's plan a lunch meeting soon.",
#     "Please find attached the agenda for next week's meeting.",
#     "Let’s brainstorm ideas for the upcoming company retreat."
# ]

# closings = [
#     "Best regards,", "Sincerely,", "Warm wishes,", "Yours faithfully,", "Take care,"
# ]

# companies = [
#     "Global Investments Inc.", "Secure Wealth Solutions", "NextGen Financials",
#     "Friendly Events LLC", "Happy Travels Inc.",
#     "Capital Growth Partners", "Prestige Wealth Advisors", "Green Future Investments",
#     "Safe Haven Financial", "Fortune Builders LLC", "Alpha Equity Group",
#     "Stellar Mutual Funds", "BlueWave Capital", "Summit Asset Management",
#     "Golden Horizon Wealth", "Strategic Growth Partners", "Infinity Capital Group",
#     "ProEdge Investments", "Steady Growth Advisors", "Lighthouse Capital"
# ]

# # Function to create random investment email
# def generate_investment_email():
#     name = fake.name()
#     subject = f"{random.choice(['Hot Investment Tips', 'Exclusive Offer', 'Portfolio Update'])}: {random.choice(investment_phrases).capitalize()}"
#     greeting = random.choice(greetings).format(name=name)
#     detail = random.choice(investment_details).format(
#         percentage=random.randint(5, 20),
#         duration=random.randint(6, 24),
#         opportunity=random.choice(["crypto assets", "real estate funds"]),
#         sector=random.choice(["stocks", "bonds", "crypto"]),
#         asset=random.choice(["mutual funds", "real estate"]),
#         strategy=random.choice(["diversification", "long-term growth strategy"])
#     )
#     closing = random.choice(closings)
#     company = random.choice(companies)

#     # Random structure
#     email_structure = [
#         f"{greeting}",
#         f"{detail}",
#         f"{closing}",
#         f"{company}"
#     ]
#     #random.shuffle(email_structure)  # Shuffle sections for randomness
#     return {"label": 1, "subject": subject, "body": "\n\n".join(email_structure)}

# # Function to create random non-investment email
# def generate_non_investment_email():
#     name = fake.name()
#     subject = f"{random.choice(['Meeting Update', 'Casual Chat', 'Event Reminder'])}: {random.choice(non_investment_topics).capitalize()}"
#     greeting = random.choice(greetings).format(name=name)
#     detail = random.choice(non_investment_details).format(
#         date=fake.date_this_month(),
#         destination=fake.city()
#     )
#     closing = random.choice(closings)
#     company = random.choice(companies)

#     # Random structure
#     email_structure = [
#         f"{greeting}",
#         f"{detail}",
#         f"{closing}",
#         f"{company}"
#     ]
#     #random.shuffle(email_structure)  # Shuffle sections for randomness
#     return {"label": 0, "subject": subject, "body": "\n\n".join(email_structure)}

# # Generate a dataset of emails
# def generate_email_dataset(num_emails=50):
#     emails = []
#     for _ in range(num_emails):
#         if random.choice([True, False]):  # Randomly decide category
#             emails.append(generate_investment_email())
#         else:
#             emails.append(generate_non_investment_email())
#     return emails



# investment_phrases.extend([
#     "diversified portfolio", "fixed-income securities", "wealth maximization",
#     "retirement planning", "long-term investments", "short-term gains",
#     "asset allocation", "financial independence", "market trends",
#     "tax-efficient investing", "blue-chip stocks", "emerging markets",
#     "hedge funds", "private equity", "capital growth", "sustainable investing",
#     "ESG investments", "growth opportunities", "financial literacy",
#     "passive income", "high-yield savings", "index funds", "commodities",
#     "economic forecasts", "financial advisors", "smart money decisions"
# ])


# investment_details.extend([
#     "This exclusive opportunity is tailored to meet your financial goals.",
#     "Seize this moment to diversify your portfolio effectively.",
#     "Our experts have identified high-potential assets for rapid growth.",
#     "Benefit from our advanced market insights and proven strategies.",
#     "Explore stable returns through tax-efficient investment solutions.",
#     "Unlock access to exclusive hedge fund opportunities.",
#     "Take advantage of low-risk, high-reward options in emerging markets.",
#     "Our portfolio management services ensure your investments thrive.",
#     "Maximize your wealth through structured asset allocation."
# ])


# non_investment_details.extend([
#     "Don't forget to RSVP for the upcoming event by {date}.",
#     "Let’s finalize the travel itinerary for our trip to {destination}.",
#     "Please share your availability for a quick catch-up call.",
#     "Looking forward to your feedback on the project discussion.",
#     "Here's a quick update on our upcoming team collaboration.",
#     "Hope all is well! Let's plan a lunch meeting soon.",
#     "Please find attached the agenda for next week's meeting.",
#     "Let’s brainstorm ideas for the upcoming company retreat."
# ])


# companies.extend([
#     "Capital Growth Partners", "Prestige Wealth Advisors", "Green Future Investments",
#     "Safe Haven Financial", "Fortune Builders LLC", "Alpha Equity Group",
#     "Stellar Mutual Funds", "BlueWave Capital", "Summit Asset Management",
#     "Golden Horizon Wealth", "Strategic Growth Partners", "Infinity Capital Group",
#     "ProEdge Investments", "Steady Growth Advisors", "Lighthouse Capital"
# ])


# # Generate 10 sample emails for testing
# emails = generate_email_dataset(10)
# output_file = "gen.txt"
# with open(output_file, "w") as file:
#     for email in emails:
#         file.write(f"Label: {'Investment' if email['label'] == 1 else 'Not Investment'}\n")
#         file.write(f"Subject: {email['subject']}\n")
#         file.write(f"Body:\n{email['body']}\n")
#         file.write("-" * 80 + "\n")  # Separator between emails

# print(f"Emails have been written to {output_file}")


from faker import Faker
import random

# Initialize Faker
fake = Faker()


non_investment_details = [
    "Looking forward to our meeting on {date}.",
    "Here are the details of our travel plan to {destination}.",
    "Just checking in to see how you are doing! Let me know if there’s anything new.",
    "Can you share the agenda for the upcoming event on {date}?",
    "Let’s finalize the itinerary for our trip to {destination}.",
    "Please share your availability for a quick catch-up call.",
    "Looking forward to your feedback on the project discussion we had on {date}.",
    "Hope all is well! Let’s plan a lunch meeting soon at {place}.",
    "Here's the updated schedule for our next team collaboration session.",
    "Let’s brainstorm some ideas for the company retreat in {destination}.",
    "Just a friendly reminder about the RSVP deadline for the event on {date}.",
    "Please review the attached document for next week’s meeting.",
    "We’re looking forward to seeing you at the event in {destination} on {date}.",
    "Do let me know if you need additional details for our upcoming project."
]

# Additional filler sentences for context and richness
filler_content = [
    "Feel free to reach out if you have any questions or need further details.",
    "I hope this update helps. Looking forward to hearing back from you soon!",
    "Please let me know if there’s anything else I can assist with.",
    "If you have any preferences for the meeting agenda, do let me know.",
    "Looking forward to seeing everyone there and sharing updates.",
    "Let’s ensure everything is ready ahead of the meeting next week."
]

# Investment-related keywords and phrases
investment_phrases = [
    "diversified portfolio", "fixed-income securities", "wealth maximization",
    "retirement planning", "long-term investments", "short-term gains",
    "asset allocation", "financial independence", "market trends",
    "tax-efficient investing", "blue-chip stocks", "emerging markets",
    "hedge funds", "private equity", "capital growth", "sustainable investing",
    "ESG investments", "growth opportunities", "financial literacy",
    "passive income", "high-yield savings", "index funds", "commodities",
    "economic forecasts", "financial advisors", "smart money decisions"
]

# General non-investment content topics
non_investment_topics = [
    "meeting schedule", "family updates", "travel plans", "event reminders",
    "friendship messages", "team collaborations", "general inquiries", "casual chats"
]

# New categories for startup content
startups = [
    {"name": "TechNova AI", "description": "an AI-powered platform that simplifies customer service with automated solutions."},
    {"name": "GreenFuture", "description": "a renewable energy company focused on solar solutions for residential properties."},
    {"name": "Healthify", "description": "a mobile app providing personalized health and fitness plans."},
    {"name": "FoodieHub", "description": "an online marketplace connecting home chefs to local customers."},
    {"name": "EduNext", "description": "a platform revolutionizing online education with live tutoring and AI analytics."}
]

purposes = [
    "We are looking to raise an additional $500,000 in seed funding to expand our operations.",
    "Our goal is to raise $1M to accelerate product development and market penetration.",
    "We are seeking $750,000 to grow our team and improve customer acquisition strategies.",
    "We aim to secure $2M to scale our platform and enhance user experience.",
    "Our purpose for contacting you is to raise $3M in Series A funding for global expansion."
]

vc_complements = [
    "We admire your proven track record in scaling startups.",
    "Your expertise in AI and tech investments makes you a perfect fit for our vision.",
    "We've been impressed by your support for early-stage companies like ours.",
    "We value your experience in renewable energy investments, which aligns with our mission.",
    "Your portfolio showcases your ability to help companies achieve sustainable growth."
]

next_steps = [
    "We’d love to schedule a call to discuss this further. Please let us know your availability.",
    "Could we set up a 15-minute call this week to go over the details?",
    "We’d appreciate an opportunity to share more about our vision over a brief call.",
    "Let us know if we could schedule a meeting to discuss potential collaboration.",
    "We’d be happy to present our detailed pitch deck in a call at your convenience."
]

closings = [
    "Best regards,", "Sincerely,", "Warm wishes,", "Yours faithfully,", "Take care,"
]

# # Greeting lines
greetings = [
    "Dear {name},", "Hi {name},", "Hello,", "Good day,", "Dear Friend,"
]

companies = [
    "Capital Growth Partners", "Prestige Wealth Advisors", "Green Future Investments",
    "Safe Haven Financial", "Fortune Builders LLC", "Alpha Equity Group",
    "Stellar Mutual Funds", "BlueWave Capital", "Summit Asset Management",
    "Golden Horizon Wealth", "Strategic Growth Partners", "Infinity Capital Group",
    "ProEdge Investments", "Steady Growth Advisors", "Lighthouse Capital"
]

non_investment_details = [
    "Looking forward to our meeting on {date}.",
    "Here are the details of our travel plan to {destination}.",
    "Just checking in to see how you are doing!",
    "Can you share the agenda for the upcoming event?",
    "Let's catch up soon over a call.",
    "Don't forget to RSVP for the upcoming event by {date}.",
    "Let’s finalize the travel itinerary for our trip to {destination}.",
    "Please share your availability for a quick catch-up call.",
    "Looking forward to your feedback on the project discussion.",
    "Here's a quick update on our upcoming team collaboration.",
    "Hope all is well! Let's plan a lunch meeting soon.",
    "Please find attached the agenda for next week's meeting.",
    "Let’s brainstorm ideas for the upcoming company retreat."
]

# Function to create a randomized investment email
def generate_investment_email():
    startup = random.choice(startups)
    funding = f"We have raised ${random.randint(100, 500)}K in funding and currently have over {random.randint(10, 100)}K active users."
    growth_stats = f"Our potential market size is estimated at ${random.randint(50, 300)}M, and we have already achieved ${random.randint(50, 500)}K in annual revenue."
    pitch_deck_link = f"You can find our pitch deck here: {fake.uri()}"

    purpose = random.choice(purposes)
    vc_complement = random.choice(vc_complements)
    next_step = random.choice(next_steps)

    # Random structure and content
    email_structure = [
        f"Dear {fake.name()},",
        f"My name is {fake.name()}, and I am the founder of {startup['name']}, {startup['description']}.",
        funding,
        growth_stats,
        pitch_deck_link,
        purpose,
        vc_complement,
        next_step,
        f"{random.choice(closings)}",
        startup['name']
    ]
    #random.shuffle(email_structure)  # Randomize sections for diversity

    subject = f"{startup['name']} - Funding Opportunity"
    return {"label": 1, "subject": subject, "body": "\n\n".join(email_structure)}






    # Additional details for enriching non-investment emails
extended_non_investment_details = [
    "We’re excited to announce that the team meeting on {date} will cover updates on the {project} project.",
    "Here's the preliminary agenda for our upcoming event in {destination} on {date}.",
    "I wanted to follow up on the travel plans for {destination}. Let’s confirm the itinerary.",
    "Thanks for sharing the details about the {topic}. Let me know if we need to adjust the schedule.",
    "Looking forward to discussing the {event} next week. Please share any additional inputs you might have.",
    "Here’s the current status of the {project} initiative: We’ve completed phase 1 and are on track for phase 2 by {date}.",
    "I wanted to check if {name} will be attending the team collaboration session on {date}.",
    "Here's the draft for our upcoming company retreat in {destination}. Feel free to share your feedback.",
    "Attached is the latest version of the {document}. Let me know your thoughts before the deadline."
]

# Filler content for richer context
complex_filler_content = [
    "Please find the attached document for reference. Let me know if there are any changes needed.",
    "If you have additional ideas or inputs, feel free to share them ahead of the meeting.",
    "Looking forward to discussing this further in our next conversation.",
    "Feel free to share any suggestions or concerns ahead of the event.",
    "Let me know if there’s anything I can assist with as we finalize the details."
]

# Updated function to generate complex non-investment emails
def generate_complex_non_investment_email():
    name = fake.name()
    subject = f"{random.choice(['Meeting Update', 'Casual Chat', 'Event Reminder', 'Project Status'])}: {random.choice(non_investment_topics).capitalize()}"
    greeting = random.choice(greetings).format(name=name)
    detail = random.choice(extended_non_investment_details).format(
        date=fake.date_this_month(),
        destination=fake.city(),
        project=fake.bs().capitalize(),
        topic=fake.catch_phrase(),
        event=fake.bs().capitalize(),
        document=fake.file_name()
    )
    filler = random.choice(complex_filler_content)
    closing = random.choice(closings)
    company = random.choice(companies)

    # Optional additional context or updates
    additional_context = random.choice([
        f"By the way, {fake.first_name()} mentioned an important point about the {fake.catch_phrase()}. We might want to consider that.",
        f"As a quick note, the last meeting on {fake.date_this_month()} had some insightful discussions that we could build upon.",
        None  # Optional to exclude this section for variability
    ])

    # Email body structure
    email_structure = [
        f"{greeting}",
        f"{detail}",
        f"{filler}",
        additional_context if additional_context else "",
        f"{closing}",
        f"{company}"
    ]
    email_structure = [section for section in email_structure if section]  # Remove empty sections
    #random.shuffle(email_structure)  # Shuffle sections for randomness

    return {"label": 0, "subject": subject, "body": "\n\n".join(email_structure)}

# Updated dataset generator to include complex non-investment emails
def generate_email_dataset_with_complexity(num_emails=50):
    emails = []
    for _ in range(num_emails):
        if random.choice([True, False]):  # Randomly decide category
            emails.append(generate_investment_email())
        else:
            emails.append(generate_complex_non_investment_email())
    return emails

# Generate and write complex emails to file
emails = generate_email_dataset_with_complexity(10)
output_file = "complex_non_investment_emails.txt"
with open(output_file, "w") as file:
    for email in emails:
        file.write(f"Label: {'Investment' if email['label'] == 1 else 'Not Investment'}\n")
        file.write(f"Subject: {email['subject']}\n")
        file.write(f"Body:\n{email['body']}\n")
        file.write("-" * 80 + "\n")  # Separator between emails

print(f"Emails have been written to {output_file}")


# Function to create random non-investment email
# def generate_non_investment_email():
#     name = fake.name()
#     subject = f"{random.choice(['Meeting Update', 'Casual Chat', 'Event Reminder'])}: {random.choice(non_investment_topics).capitalize()}"
#     greeting = random.choice(greetings).format(name=name)
#     detail = random.choice(non_investment_details).format(
#         date=fake.date_this_month(),
#         destination=fake.city()
#     )
#     closing = random.choice(closings)
#     company = random.choice(companies)

#     # Random structure
#     email_structure = [
#         f"{greeting}",
#         f"{detail}",
#         f"{closing}",
#         f"{company}"
#     ]
#     #random.shuffle(email_structure)  # Shuffle sections for randomness
#     return {"label": 0, "subject": subject, "body": "\n\n".join(email_structure)}
# def generate_non_investment_email():
#     name = fake.name()
#     subject = f"{random.choice(['Meeting Update', 'Casual Chat', 'Event Reminder', 'Project Status'])}: {random.choice(non_investment_topics).capitalize()}"
#     greeting = random.choice(greetings).format(name=name)
#     detail = random.choice(non_investment_details).format(
#         date=fake.date_this_month(),
#         destination=fake.city(),
#         place=fake.company()
#     )
#     filler = random.choice(filler_content)
#     closing = random.choice(closings)
#     company = random.choice(companies)

#     # Email body structure
#     email_structure = [
#         f"{greeting}",
#         f"{detail}",
#         f"{filler}",
#         f"{closing}",
#         f"{company}"
#     ]
#     #random.shuffle(email_structure)  # Shuffle sections for randomness

#     return {"label": 0, "subject": subject, "body": "\n\n".join(email_structure)}


# # Generate a dataset of emails
# def generate_email_dataset(num_emails=50):
#     emails = []
#     for _ in range(num_emails):
#         if random.choice([True, False]):  # Randomly decide category
#             emails.append(generate_investment_email())
#         else:
#             emails.append(generate_non_investment_email())
#     return emails

# # Generate 10 sample emails for testing
# emails = generate_email_dataset(10)
# output_file = "extended_emails.txt"
# with open(output_file, "w") as file:
#     for email in emails:
#         file.write(f"Label: {'Investment' if email['label'] == 1 else 'Not Investment'}\n")
#         file.write(f"Subject: {email['subject']}\n")
#         file.write(f"Body:\n{email['body']}\n")
#         file.write("-" * 80 + "\n")  # Separator between emails

# print(f"Emails have been written to {output_file}")







