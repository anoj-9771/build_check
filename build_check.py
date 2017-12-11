import shutil
import os
import logging
import time
import pygal
from input_question import question, make_pie

pending = []
upgraded = []
failed = []
final = []
# codeword = "WAYSTATION"
answer = raw_input("What would you like to query? \n 1.WAYSTATION \n 2.XPe STAGING \n 3.PRODUCTION \n")

# to import "question" function from file "input_question.py" and use it to process answer
codeword = question(answer)
print ("Collecting information for ") + codeword


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

sc = '//aussydrw001/Stores/Upgrade/healthcheck/incoming/'
dt = 'C:/Source/healthcheck/stores/'

###########################################################################
# to copy files from remoteware server to local drive
for filename in os.listdir(sc):
    if filename.endswith('.txt') and filename.startswith('AU'):
        shutil.copy(sc + filename, dt)
        logging.debug('Copying ' + filename)
time.sleep(10)
###########################################################################

###########################################################################
##to read the files and check for new version - Waystation
for file in os.listdir("C:/Source/healthcheck/stores/"):
    if file.endswith('.txt') and file.startswith('AU'):
        text_file = open("C:/Source/healthcheck/stores/" + file, "r")
        lines = text_file.readlines()
        for line in lines:
            if codeword + " - Version : 6130 RC2" in line:
                upgraded.append(file)
        text_file.close()

print ("The list of upgraded stores is below :")
for store in upgraded:
    print (store[0:7])

print ("The total count of upgraded sites :")
print (len(upgraded))
###########################################################################

###########################################################################
##to read the files and check for old version - Waystation
for file in os.listdir("C:/Source/healthcheck/stores/"):
    if file.endswith('.txt') and file.startswith('AU'):
        text_file = open("C:/Source/healthcheck/stores/" + file, "r")
        lines = text_file.readlines()
        for line in lines:
            if codeword + " - Version : 6130 RC1" in line:
                pending.append(file)
        text_file.close()

print ("The list of pending sites is below :")

for store in pending:
    print (store[0:7])

print ("The total count of pending sites :")
print (len(pending))
###########################################################################

###########################################################################
#Use the below section of code to see the list and count of stores with Kiosks
# for file in os.listdir("C:/Source/healthcheck/stores/"):
#     if file.endswith('.txt'):
#         text_file = open("C:/Source/healthcheck/stores/" + file, "r")
#         lines = text_file.readlines()
#         for line in lines:
#             if "Area: CSO" in line:
#                 stores.append(file)
#         text_file.close()
#
# for store in list(set(stores)):
#     if "AU" in store:
#         final.append(store)
#
# print sorted(final)
# print len(final)
###########################################################################

###########################################################################
#to import make_pie function from "input_question.py" and render pie chart
make_pie(answer, upgraded, pending)

###########################################################################
#Debug
# print (codeword)

###########################################################################
