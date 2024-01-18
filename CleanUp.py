import os
import shutil
def cleanUp(imgfolder,audfolder):
  shutil.rmtree(imgfolder[2::],ignore_errors=True) #To Delete All Downloaded Images
  shutil.rmtree(audfolder[2::],ignore_errors=True) #To Delete All Generated Audio
  shutil.rmtree("__pycache__",ignore_errors=True) #To Delete Cache formed in the process

if __name__ == "__main__":
  cleanUp('./images/',
          './audio/'
          )