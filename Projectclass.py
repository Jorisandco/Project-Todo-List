import os.path

class project:

    def __init__(self, Projectname, savedatafolder):
      self.savedata = savedatafolder
      self.Projectname = Projectname
      self.projectslistpath= f"{self.savedata}/savedata.txt"

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


    def openProject(self, name):
        self.CProcject = name
        with open(self.CProcject , "r") as PRJ:
            print(PRJ.read())

    def saveproject(self):
        self.fileR

        self.fileR.close()

    def createNewProject(self, name):
        projectLocation = f"{self.savedata}/{name}"
        newproject = open (f"{self.savedata}/{name}", "w")

        newproject.write("Unfinished-\nworking on-\ncomplete-")
        newproject.close()
        with open(self.projectslistpath , "a+") as fileR:
            fileR.write(f"project.{name}-{projectLocation}\n-")
            self.openProject(projectLocation)




    #all the things for the project items
    def newItem(self, name):
        print("made new item")
    def removeItem(self):
        print("item removed")
    def setItemTodone():
        print("item finished")
    def setItemtoWorkingon(self):
        print("you are now working on this item")
    def SetItemToNotFinished(self):
        print("item is now in not finished list")