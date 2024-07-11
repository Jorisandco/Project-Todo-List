import os.path

class project:

    def __init__(self, Projectname, savedatafolder):
      self.savedata = savedatafolder
      self.Projectname = Projectname
      self.projectslist= f"{self.savedata}/savedata.txt"

# all the diffrent types of ways to open the project save file
      self.fileR = open(self.projectslist, "r+")


      backup = open("savedata/backup/backupsavedataPRJList.txt", "w")
      backup.write(self.fileR.read())
      self.fileR.close


#all the stuff for the project list
    def displaylist(self):
        self.fileR

        self.fileR.close()

    def openProject(self, name):
        self.CProcject = name
        with open(self.CProcject , "r") as PRJ:
            print(PRJ.read())

    def saveproject(self):
        self.fileR

        self.fileR.close()

    def createNewProject(self, name):
       projectLocation = f"{self.savedata}/{name}"
       newproject =  open (f"{self.savedata}/{name}", "w")

       newproject.write("Unfinished- \n working on- \n complete-")
       newproject.close()

       self.fileR.write(f"\n \n {name}.Project \n {projectLocation} \n -")

       self.fileR.close()
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