from flask import *
import yaml 

app = Flask(__name__)

with open("config.yml") as configfile:
    conf = yaml.safe_load(configfile)["settings"]



@app.route("/")
def  index():
    return render_template('./index.html')




if __name__ == '__main__':
    app.run(host=conf["host_ip"],port=conf["port"],debug=True)     