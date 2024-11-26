import matplotlib.pyplot as plt

passengers = [
    {"Surname": "Jackson", "Pieces_baggage": 3, "Weight": 20.5},
    {"Surname": "Chetwynd", "Pieces_baggage": 1, "Weight": 4.3},
    {"Surname": "Pisarev", "Pieces_baggage": 5, "Weight": 15.0}
]

names = [p["Surname"] for p in passengers]
baggage_count = [p["Pieces_baggage"] for p in passengers]

fig, ax = plt.subplots()
ax.pie(baggage_count, labels=names, autopct='%1.1f%%', startangle=90)

ax.axis('equal')

plt.title('Distribution of Baggage Pieces per Passenger')

plt.show()
