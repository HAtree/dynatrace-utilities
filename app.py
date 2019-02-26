from flask import Flask
import ut, hostUnits

app = Flask(__name__)

#TODO Read Tenant UUID and API Token from a file / environment variables
TENANT_UUID = ""
API_TOKEN = ""

@app.route('/')
def index_page():
    return("Dynatrace Utilities! pages: /untagged /hostGroupCost")

@app.route('/untagged')
def untagged_hosts():
    responseHTML=ut.returnHTML(ut.getTaggedHostsFromApi(TENANT_UUID, API_TOKEN))
    return(responseHTML)

@app.route('/hostGroupCost')
def hostGroupCcost():
    responseHTML= hostUnits.calculateHostUnitsPerHostGroup(ut.getTaggedHostsFromApi(TENANT_UUID, API_TOKEN)).__str__()
    return(responseHTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0')