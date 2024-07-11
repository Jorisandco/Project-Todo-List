import os.path

class projectList:
    def __init__(self, Projectname, savedatafolder):
      self.savedataFolder = savedatafolder
      self.Projectname = Projectname
      self.projectslistpath= f"{self.savedataFolder}/savedata.txt"

# all the diffrent types of ways to open the project save file
      with open(self.projectslistpath , "r+") as fileR:
        backup = open("savedata/backup/backupsavedataPRJList.txt", "w")
        backup.write(fileR.read())
        fileR.close()

#all the stuff for the project list
    def displaylist(self):
        actualNames = []
        locations = []
        with open(self.projectslistpath, "r") as PRJList:

            string = PRJList.read()
            
            unsorted = string.split("-")

            count = True

            for item in unsorted:
                if count == True:
                    name = item
                    actualNames.append(name)
                    count = False
                else:
                    locations.append(item)
                    count = True
            
            print("names: ", actualNames)
            print("locations: ", locations)
        return actualNames, locations


    def openProjectFile(self, name):
        self.CProcject = name
        with open(self.CProcject , "r") as PRJ:
            print(PRJ.read())
        return PRJ.read

    def saveproject(self):
        with open(self.Projectname , "a+") as save:
            print("implement save system")

    def createNewProject(self, name):
        projectLocation = f"{self.savedataFolder}/{name}"
        newproject = open (f"{self.savedataFolder}/{name}", "w")

        newproject.write("Unfinished-\nworking on-\ncomplete-")
        newproject.close()
        with open(self.projectslistpath , "a+") as fileR:
            fileR.write(f"project.{name}-{projectLocation}\n-")
            self.openProject(projectLocation)