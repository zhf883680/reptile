import os,sys
#import msvcrt

if __name__=='__main__':
    fileList=os.listdir(sys.path[0])
    for fileName in fileList:
        try:
            if len(fileName)>19 and fileName.index('[电影天堂www.dy2018.com]')>-1:
                os.rename(fileName,fileName[20:])
        except ValueError as err:
            print(fileName+"\n")
        
           
            
    
    