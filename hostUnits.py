import json, requests

def calculateHostUnitsPerHostGroup(hostsDict):
    """Calculates the host units consumed per Host_Group and returns a dictionary of Host_Group:consumedHostUnits
    Keyword Arguments:
    hostsDict: A dictionary with the unmarshalled contents of the Dynatrace Hosts API response
    Returns:
    a dictionary of form {"Host_Group_Name":consumedHostUnits}
    """
    hostGroupAndCosts = {}
    for host in hostsDict:
        try:
            hostGroupName = host["hostGroup"]["name"]
        except KeyError:
            hostGroupName = "No-Host-Group"

        print(hostGroupName)
        if hostGroupName in hostGroupAndCosts.keys():
            hostGroupAndCosts[hostGroupName] += float(host["consumedHostUnits"])
        else:
            hostGroupAndCosts[hostGroupName] = float(host["consumedHostUnits"])
        
    return hostGroupAndCosts

def returnHtml(managementZonesAndCostsDict):
    """
    converts the managementZones and Costs into an HTML Table as a string
    """
    return None


#if __name__ == "__main__":
    # do your stuff here :)