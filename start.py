import healthchecker

baymax = healthchecker.HealthChecker

baymax.start()
bodyLocations = baymax.getBigLocations()
bodySubLocations = baymax.getSubLocations(bodyLocations)

# GET SUBLOCATION
# replace text w/ chose sublocation or location
text = ""
bodySubLocation = baymax.getUserInfo(bodySubLocations, text)


symptoms = []
if(bodySubLocation is not None):
    symptoms = baymax.getSubLocations(bodySubLocation)
    print(symptoms)

# logic to get selected symptoms, get IDs only
diagnosis = []
selectedSymptoms = []
if(selectedSymptoms is not None):
    diagnosis = baymax.getDiagnosis(selectedSymptoms)
    baymax.printDiagnosis(diagnosis)





