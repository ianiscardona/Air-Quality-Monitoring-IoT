from flask import Flask, render_template, redirect, url_for

import pandas as pd
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

	data = pd.read_csv("input.csv")

	return render_template("historypage.html", tables=[data.to_html()], titles=[''])


# columns = ["Name", "Marks"]
# df = pd.read_csv("input.csv", usecols=columns)
# print("Contents in csv file: ", df)
# plt.plot(df.Name, df.Marks)
# plt.show()

if __name__ == "__main__":
	# app.run(host="localhost", port=int(5000))
	app.run(debug=True)