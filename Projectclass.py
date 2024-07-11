class project:

    def __init__(self, Projectname, savedatafolder):
      self.savedata = savedatafolder
      self.Projectname = Projectname
      self.projectslist= f"{self.savedata}/savedata.txt"

# all the diffrent types of ways to open the project save file
      self.fileR = open(self.projectslist, "r")
      self.filew = open(self.projectslist, "w")
      self.fileA = open(self.projectslist, "a")

      backup = open("savedata/backup/backupsavedataPRJList.txt", "w")
      backup.write(self.fileR.read())
      self.fileR.close


#all the stuff for the project list
    def displaylist(self):
        self.fileR

        self.fileR.close()
    def saveproject(self):
        self.filew

        self.filew.close()

    #all the things for the project items
    def newItem(self):
        print("made new item")
    def removeItem(self):
        print("item removed")
    def setItemTodone():
        print("item finished")
    def setItemtoWorkingon(self):
        print("you are now working on this item")
    def SetItemToNotFinished(self):
        print("item is now in not finished list")