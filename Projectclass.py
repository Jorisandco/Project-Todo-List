class project:

    def __init__(self, Projectname, savedatafolder):
      self.savedata = savedatafolder
      self.Projectname = Projectname
      self.projectslist= f"{self.savedata}/savedata.txt"

      file = open(self.projectslist, "r")
      
      backup = open("savedata/backup/backupsavedataPRJList.txt", "w")

      backup.write(file.read())

      print(file.read())


    def newItem():
        print("made new item")
    def removeItem():
        print("item removed")
    def setItemTodone():
        print("item finished")
    def setItemtoWorkingon():
        print("you are now working on this item")
    def SetItemToNotFinished():
        print("item is now in not finished list")