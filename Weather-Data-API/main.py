from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


stations = pd.read_csv("D:\\02-Learning\\Python\\Udemy\\60DaysPython\\Weather-Data-API\\data_small\\stations.txt", skiprows=17)
stations = stations[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv(f"data_small/TG_STAID{str(station).zfill(6)}.txt",
                     skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {'station': station, 'date': date, 'temperature': temperature}


@app.route("/api/v1/<station>")
def all_station_data(station):
    df = pd.read_csv(f"data_small/TG_STAID{str(station).zfill(6)}.txt",
                     skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def all_station_years_data(station, year):
    df = pd.read_csv(f"data_small/TG_STAID{str(station).zfill(6)}.txt",
                     skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True, port=2222)
