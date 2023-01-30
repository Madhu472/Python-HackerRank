### Input List

devicelist=['tv','lamp','tv','lamp','tv','lamp']

## Function for Naming devices

def nameDevices(devicelist):
    uniquedevices = []
    for i,device in enumerate(devicelist):
        # print(i,device)
        # print(devicelist[:i])
        occurence = devicelist[:i].count(device)
        # print(occurence)
        # print("--------------")
        if(occurence > 0):
            uniquedevices.append(device + str(occurence))
        else:
            uniquedevices.append(device)
    return uniquedevices
  
  
  ## Output
  out = ['tv', 'lamp', 'tv1', 'lamp1', 'tv2', 'lamp2']
