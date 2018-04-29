import helper
import random
import config
import sys
import json


class HealthChecker:

    # initialize w/ username and password
    def __init__(self):
        username = config.username
        password = config.password
        authUrl = config.priaid_authservice_url
        healthUrl = config.priaid_healthservice_url
        language = config.language
        self._printRawOutput = config.pritnRawOutput

        self._diagnosisClient = helper.Helper(username, password, authUrl, language, healthUrl)

    # starts here
    def start(self):
        # load in bodyLocations and SubLocations
        bodyLocations = self._diagnosisClient.loadBodyLocations()


    # takes in a list of bodyLocations and all body subLocations and determines the user's affected areas
    # will return a sublocation
    def getUserInfo(self, bodySubLocations, text):
        # get bodyLocation and subLocation based on inputif applicable
        bodySubLocation = self.findBodySubLocation(bodySubLocations, text)
        return bodySubLocation


    # returns a list of all big locations
    def getBigLocations(self):
        return self._diagnosisClient.loadBodyLocations()

    # returns a concatenated list of all sublocations
    def getSubLocations(self, bodyLocations):
        bodySubLocations = []
        for bodyLocation in bodyLocations:
            bodySubLocations = bodySubLocations + self._diagnosisClient.loadBodySubLocations(bodyLocation["ID"])
        return bodySubLocations


    # find body location / sublocation & ID based on user input
    def findBodyLocation(self, bodyLocations, text):
        # look for input in each bodyLocation name
        bodyLocation = ""
        for bodyL in bodyLocations:
            if text in bodyL["Name"]:
                bodyLocation = bodyL  # set the body location
        return bodyLocation

    # check for body sublocation on first user input
    def findBodySubLocation(self, bodySubLocations, text):
        # look for input use that instead of larger body Location
        for bodySL in bodySubLocations:
            if text in bodySL["Name"]:
                bodySubLocation = bodySL  # set body sub location
        return bodySubLocation



    # print out all body Locations
    def printBodyLocations(bodyLocations):
        for bodyLocation in bodyLocations:
            print(bodyLocation["Name\n"])

    # print out all sublocation based on body location
    def printBodySubLocations(bodySubLocations):
        for bodySubLocation in bodySubLocations:
            print(bodySubLocation["Name\n"])

    # get symptoms of sublocation
    def getSymptoms(self, bodySubLocation):
        symptoms = self._diagnosisClient.loadSublocationSymptoms(bodySubLocation["ID"], helper.SelectorStatus.Man)
        return symptoms


    # print all symptoms based on bodyLocation
    def printSymptoms(self, symptoms):
        print("Which of these symptoms are you experiencing?")
        print("Choose IDs separated by a comma")
        for symptom in symptoms:
            print(symptom["ID"], symptom["Name"])



    # get diagnosis based on selected symptoms and user info like gender and age
    def getDiagnosis(self, selectedSymptoms):
        return self._diagnosisClient.loadDiagnosis(selectedSymptoms, helper.Gender.Male, 1988)


    def printDiagnosis(self, diagnosis):
        for d in diagnosis:
            print("{0} - {1}% \n".format(d["Issue"]["Name"], d["Issue"]["Accuracy"]))

