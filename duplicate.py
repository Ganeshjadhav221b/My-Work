# Driver function 
import os
import re
if __name__ == "__main__":
    duplicateFiles=0
    success = 0
    failed = 0 
    total = 0
    path = "H:\Pics\Mabbuuu"
    for (root,dirs,files) in os.walk(path): 
        print (root) 
        #print (files)
        for file in files:
            print(file)
            total += 1
            x = re.compile(r'(.*)- Copy.jpg')
            y = x.search(file)
            if y != None:
                print(y.groups())    
                duplicateFiles += 1
                fileToRemove = path+'\\'+file
                try:
                    os.remove(fileToRemove)
                    success += 1
                    print("Removed succesfully: ",fileToRemove)
                except Exception as e:
                    print("Error while removing file: ",fileToRemove)
                    print(e)
                    failed += 1
                    
    print("No. of files: ",total)
    print("No. of duplicate files : ",duplicateFiles)
    print("No. of duplicate files removed successfully: ",success)
    print("No. of duplicate files failed to remove: ",failed)
