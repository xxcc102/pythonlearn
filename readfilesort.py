import re

globaltimecount = 0

def processline(line):

    minute = int(line[5])
    second = int(float(line[6]))
    #sumtime =
    return minute * 60 + second



def read():
    try:
        global globaltimecount
        file_object = open('xc.obs','r')

        list_of_all_the_lines = file_object.readlines()

        for line in list_of_all_the_lines:
            if re.match('> 2018',line) == None:
                continue
            else:
                list1 = line.split()
                time = processline(list1)

                if (globaltimecount == 0):
                    globaltimecount = time
                    continue
                globaltimecount+=1
                if globaltimecount == time:
                    continue
                else:
                    print (list1[4],list1[5],list1[6])
                    globaltimecount = 0

            '''print line'''

    finally:
        if file_object:
            file_object.close()

if __name__ == "__main__":
    # a=0
    read()