from flask import Flask, render_template, redirect, url_for

import pandas as pd
import csv
from matplotlib import pyplot as plt


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

app = Flask(__name__)

@app.route("/monitorpage.html")
def homePage():
	return render_template("monitorpage.html")

@app.route("/chatbotpage.html")
def chatbotPage():
	return render_template("chatbotpage.html")

@app.route("/historypage.html")
def historyPage():

	# df = [
	# 	("Jimmy", 10),
	# 	("Joe", 50),
	# 	("Jose", 100),
	# 	("Joey", 80),
	# 	("Joela", 30),
	# ]
	with open('input.csv', newline='') as csvfile:
		df = list(csv.reader(csvfile))

	labels = [row[0] for row in df]
	values = [row[1] for row in df]

	return render_template("historypage.html", labels=labels, values=values)


# columns = ["Name", "Marks"]
# df = pd.read_csv("input.csv", usecols=columns)
# print("Contents in csv file: ", df)
# plt.plot(df.Name, df.Marks)
# plt.show()

if __name__ == "__main__":
	# app.run(host="localhost", port=int(5000))
	app.run(debug=True)