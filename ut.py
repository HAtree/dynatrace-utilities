import json, requests
"""Utilities for returning the list of hosts with a specific Tag from the Dynatrace API: use case of finding hosts which do not match the customers tagging strategy"""


def outputHTML(outputFileName, unTaggedHostsDict):
    with open(outputFileName, "w") as outputFile:
        print("<html>\n<body>\n<table>\n", file=outputFile)
        print("<tr><th>Display Name</th><th>Discovered Name</th><th>Ip Addresses</th><th>Tags</th>", file=outputFile)
        for host in unTaggedHostsDict:
            tags = ""
            ipAddresses = ""
            for ip in host['ipAddresses']:
                ipAddresses += ip
            for tag in host["tags"]:
                try:
                    tags += (tag["key"] + ":" + tag["value"] + "<br />")
                except KeyError:
                    tags += (tag["key"] + "\n")
            outputFile.write(f"<tr>\n\t<td>{host['displayName']}</td><td>{host['discoveredName']}</td><td>{ipAddresses}</td><td>{tags}</td>\n</tr>\n")
        print("</table>\n</body>\n</html>", file=outputFile)

def returnHTML(unTaggedHostsDict):
    htmlString = ""
    htmlString += "<html>\n<body>\n<table>\n"
    htmlString += "<tr><th>Display Name</th><th>Discovered Name</th><th>Ip Addresses</th><th>Tags</th>"
    for host in unTaggedHostsDict:
        tags = ""
        ipAddresses = ""
        for ip in host['ipAddresses']:
            ipAddresses += ip
        for tag in host["tags"]:
            try:
                tags += (tag["key"] + ":" + tag["value"] + "<br />")
            except KeyError:
                tags += (tag["key"] + "\n")
        htmlString += f"<tr>\n\t<td>{host['displayName']}</td><td>{host['discoveredName']}</td><td>{ipAddresses}</td><td>{tags}</td>\n</tr>\n"
    htmlString += "</table>\n</body>\n</html>"
    return(htmlString)


def outputCSV(outputFileName, unTaggedHostsDict):
    with open(outputFileName, "w") as outputFile:
        print('"DisplayName","Discovered Name","IP Addresses","Tags"\n', file=outputFile)
        for host in unTaggedHostsDict:
            tags = '"'
            ipAddresses = '"'
            for ip in host['ipAddresses']:
                ipAddresses += ip
            ipAddresses += '"'
            for tag in host["tags"]:
                try:
                    tags += (tag["key"] + ":" + tag["value"] + ", ")
                except KeyError:
                    tags += (tag["key"] + ", ")
            tags+='"'
            outputFile.write(f'"{host["displayName"]}","{host["discoveredName"]}","{ipAddresses}","{tags}"\n')

def getTaggedHostsFromApi(tennantUUID, apiToken, tagString=None):
    #API Constants
    HOSTS_API_URI="/api/v1/entity/infrastructure/hosts?relativeTime=hour&showMonitoringCandidates=false"
    HOSTS_API_URL="https://" + tennantUUID + ".live.dynatrace.com" + HOSTS_API_URI + "&Api-Token=" + apiToken
    if tagString != None:
        HOSTS_API_URL += "&tag=" + tagString
    print("Requesting: {}".format(HOSTS_API_URL))
    return(requests.get(HOSTS_API_URL).json())

if (__name__ == "__main__"):
    #API Constants
    UNTAGGED_HOSTS_API_URI="/api/v1/entity/infrastructure/hosts?relativeTime=hour&tag=Untagged&showMonitoringCandidates=false"
    UNTAGGED_PG_API_URI=""
    API_TOKEN=""
    TENANT_UUID=""
    UNTAGGED_HOSTS_API_URL="https://" + TENANT_UUID + ".live.dynatrace.com" + UNTAGGED_HOSTS_API_URI + "&Api-Token=" + API_TOKEN
    UNTAGGED_PG_API_URL="https://" + TENANT_UUID + ".live.dynatrace.com" + UNTAGGED_PG_API_URI + "&Api-Token=" + API_TOKEN

    #OutputFile Constants
    OUTPUT_FILE_NAME = "untaggedhosts.html"


    unTaggedHostsResponse = requests.get(UNTAGGED_HOSTS_API_URL)
    utHosts = unTaggedHostsResponse.json()

    #Just as a debug, lets try print that out as a table ourselves
    print("Display Name\t DiscoveredName \n")
    for host in utHosts:
        print(host["displayName"] + "\t" + host["discoveredName"] + "\n")

    #Test HTML and CSV Outputs
    outputCSV("untaggedHosts.csv", utHosts)
    outputHTML(OUTPUT_FILE_NAME, utHosts)


