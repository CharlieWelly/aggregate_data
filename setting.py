import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {"ticker": "B8", "interval": "E8", "start": "14"}
config["DN"] = {}
config["DN"]["BS_length"] = "122"
config["DN"]["first_item"] = "TÀI SẢN NGẮN HẠN"

with open("./example.ini", "w") as configfile:
    config.write(configfile)
