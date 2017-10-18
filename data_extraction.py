# -*- coding: utf-8 -*-

# Python Libraries
import MySQLdb
import json
import io
import datetime
import re

# Importing other code
from classes import *


def saveJson(json_name, objects_list, encoder_class):
    with io.open(''+json_name+'.json', 'w', encoding='utf-8') as jsonTemp:
        jsonTemp.write(unicode(json.dumps(objects_list, jsonTemp, cls=encoder_class, indent=2)))
    jsonTemp.close()


'''
Get users and data from database 
'''

print "\nGet data from database\n"

# Set the proper params
database_host = ""
database_user = ""
database_passwd = ""
database_name = ""

db = MySQLdb.connect(host=database_host,user=database_user,passwd=database_passwd, db=database_name)

users_list = []
groups_list = []
membership_list = []
friendship_list = []

cur = db.cursor()

# SQL Query
cur.execute("""SELECT PrincipalID, FirstName, LastName, Email from UserAccounts """) 
for row in cur.fetchall():
    p = User(user_id=row[0], user_name=row[1].replace("*pending* ", ""), user_surname=row[2], email=row[3])
    users_list.append(p)
saveJson("users", users_list, UserEncoder)

'''
Other queries that could be used 
  - These queries produce json files with the info. 
  - You can format these data to ARFF using utilities available in this code
 
# Interesting fields in the "UserAccounts" table
# PrincipalID
# FirstName
# LastName
# Email 
# UserLevel -> superadmins have a 100 user level. Common users an user level = 0
# UserTitle -> the label for an user, not all have one.

# "friends" Table
# PrincipalID
# Friend
# Flags ?
# Offered ?

# The "griduser" table keeps the users' positions within the virtual world

# "osgroup" table
# GroupID
# Name (of the group)
# OwnerRoleID

# "osgroupmembership" Table
# GroupID
# AgentID


# Get groups

cur.execute("""SELECT GroupID, Name, OwnerRoleID from osgroup """) 

for row in cur.fetchall():
    print row[0]
    print row[1]
    print row[2]
    g = Group(group_id=row[0], group_name=row[1], group_owner=row[2])
    groups_list.append(g)

with io.open('path/groups.json', 'w', encoding='utf-8') as groups_json:
    groups_json.write(unicode(json.dumps(groups_list, groups_json, cls=GroupEncoder, indent=2)))
groups_json.close()

# Get members of groups
cur.execute("""SELECT GroupID, AgentID from osgroupmembership """) 

for row in cur.fetchall():
    print row[0]
    print row[1]
    g = Member(group_id=row[0], user_id=row[1], )
    membership_list.append(g)

with io.open('path/groupsMembers.json', 'w', encoding='utf-8') as members_json:
    members_json.write(unicode(json.dumps(membership_list, members_json, cls=MembersEncoder, indent=2)))
members_json.close()

# Get friends
cur.execute("""SELECT PrincipalID, Friend from friends """) 

for row in cur.fetchall():
    print row[0]
    print row[1]
    g = Friend(user_id1=row[0], user_id2=row[1], )
    friendship_list.append(g)

with io.open('path/friends.json', 'w', encoding='utf-8') as json_friends:
    json_friends.write(unicode(json.dumps(friendship_list, json_friends, cls=FriendsEncoder, indent=2)))
json_friends.close()

'''


'''
Get sessions from Opensim log 
'''

session_list = []

date_temp = []
hour_temp = []
h2_temp = []

begin_session = 0
fin_session = 0

print "\nReal Sessions\n"

# path to Opensim Robust.log
log_path = ""
f = open(log_path)
line = f.readline()

for line in f:
    if line.find("OpenSim.Services.PresenceService.PresenceService [PRESENCE SERVICE]: LoginAgent") >= 0:
        begin_session = begin_session+1
    session_init = re.search("(.+).LoginAgent (.+).with session (.+).and ssession (.+)", line)
    if session_init is not None:
        date_beg_session = re.split(" ", session_init.group(1))

        date_temp = date_beg_session[0].split("-")

        hour_temp = date_beg_session[1].split(":")
        h2_temp=hour_temp[2].split(",",1)

        p = Session(session_id=str(session_init.group(3)), user_id=str(session_init.group(2)),
                    date_init=str(date_beg_session[0]), year_init=str(date_temp[0]),
                    month_init=str(date_temp[1]), day_init=str(date_temp[2]),
                    hour_init=str(date_beg_session[1]), hours_init=str(hour_temp[0]),
                    minutes_init=str(hour_temp[1]), seconds_init=str(h2_temp[0]), date_fin=0,
                    year_fin=0,  month_fin=0, day_fin=0, hour_fin=0, hours_fin=0,
                    minutes_fin=0, seconds_fin=0, session_t=0)
        session_list.append(p)
    elif line.find("OpenSim.Services.PresenceService.PresenceService [PRESENCE SERVICE]: Session") >= 0:
        fin_session = fin_session+1
        endSession = re.search("(.+).Session (.+).logout", line)
        if endSession is not None:
            date_e_session = re.split(" ", endSession.group(1))
            for x in session_list:
                if x.session_id == endSession.group(2):
                    x.date_fin = str(date_e_session[0])
                    x.hour_fin = str(date_e_session[1])

                    date_temp = date_e_session[0].split("-")
                    x.year_fin = str(date_temp[0])
                    x.month_fin = str(date_temp[1])
                    x.day_fin = str(date_temp[2])

                    hour_temp = x.hour_fin.split(":")
                    h2_temp = hour_temp[2].split(",",1)

                    x.hours_fin = str(hour_temp[0])
                    x.minutes_fin = str(hour_temp[1])
                    x.seconds_fin = str(h2_temp[0])

                    d1 = datetime.datetime.strptime(x.date_init+" "+x.hours_init+":"+x.minutes_init
                                                    + ":"+x.seconds_init, "%Y-%m-%d %H:%M:%S")
                    d2 = datetime.datetime.strptime(x.date_fin+" "+x.hours_fin+":"+x.minutes_fin
                                                    + ":"+x.seconds_fin, "%Y-%m-%d %H:%M:%S")

                    result = d2 - d1

                    x.session_t = str(result.total_seconds())
time_total_sec = 0
time_total_hours = 0.0
time_average_min = 0.0

for x in session_list:
    time_total_sec += float(x.session_t)

tMedioSeg = time_total_sec/len(session_list)
time_total_hours = time_total_sec/3660
time_average_min = tMedioSeg/60


print "With real users"
print "How many sessions started %d, complete sessions: %d" % (begin_session, fin_session)
print "Users have employed %d seconds or %.2f hours in the world" % (time_total_sec, time_total_hours)
print "Average time of %d seconds or %.2f minutes per user" % (tMedioSeg, time_average_min)

saveJson("sessions", session_list, SessionEncoder)


print "\n\nReal sessions for Weka\n\n"
arff = open ("sessions.arff", "w")
arff.write("% Title: Info about sessions\n% Creator: Juan Cruz-Benito\n% Date: June, 2013\n\n")
arff.write("@relation 'Sessions'\n")
arff.write("\n@attribute CLASE {Login, Logout}\n")
arff.write("@attribute user_id string\n@attribute fecha DATE yyyy-MM-dd HH:mm:ss\n")
arff.write("\n\n@data\n")

for x in session_list:
    if x.date_fin != 0:
        arff.write("Login,"+str(x.user_id)+","+str(x.date_init)+" "+str(x.hours_init)+":"
                   +str(x.minutes_init)+":"+str(x.seconds_init)+"\n")
        arff.write("Logout,"+str(x.user_id)+","+str(x.date_fin)+" "+str(x.hours_fin)+":"
                   +str(x.minutes_fin)+":"+str(x.seconds_fin)+"\n")

arff.close()


'''
Get movements from Virtual World's log 
'''

teleports_requests_counter = 0
teleports_incomplete_counter = 0
teleports_complete_counter = 0
teleports_list = []
out_terrain_counter = 0
close_terrain_counter = 0
close_connection_counter = 0
arrival_terrain_counter = 0

print "\nTeleports Reales\n"

# path to Opensim Opensim.log
log_path = ""
f = open(log_path)
line = f.readline()

for line in f:
    if line.find("Request Teleport to") >= 0:
        # Example
        # 2012-07-05 09:43:34,697 DEBUG - OpenSim.Region.CoreModules.Framework.EntityTransfer.EntityTransferModule
        # [ENTITY TRANSFER MODULE]: Request Teleport to http://212.128.146.39:1935/ (http://212.128.146.39:1935/)
        # USALPHARMA/<128, 128, 1.5>
        teleport_request = re.search("(.+).Request Teleport to http://(.+)/ \(http://(.+)/\) (.+)/.", line)
        if teleport_request is not None:
            teleport_date = re.split(" ", teleport_request.group(1))
            teleport_region_dest_o = teleport_request.group(4)
            teleports_requests_counter = teleports_requests_counter+1
            for line in f:
                if line.find("Closing child agents. Checking") >= 0:
                    # Example
                    # 2012-07-05 09:35:02,498 DEBUG - OpenSim.Region.Framework.Scenes.ScenePresence [SCENE PRESENCE]:
                    # Closing child agents. Checking 1 regions in USAL SIPPE
                    teleport_o = re.search("(.+).Closing child agents. Checking (.+) regions in (.+)", line)
                    if teleport_o is not None:
                        teleport_date = re.split(" ", teleport_request.group(1))
                        source_region_teleport = teleport_o.group(3)
                    horaTemp = teleport_date[1].split(",",1)
                    hour_initTemp = horaTemp[0]
                    p = Teleport(user_name="", date_init=str(teleport_date[0]), hour_init=str(hour_initTemp),
                                 teleport_source=str(source_region_teleport.replace(" ", "_")), teleport_dest="")
                    teleports_list.append(p)
                    posLisAct = len(teleports_list)
                    out_terrain_counter = out_terrain_counter+1
                elif line.find("Upgrading child to root agent") >= 0:
                    # Example
                    # 2012-07-05 09:35:04,490 DEBUG - OpenSim.Region.Framework.Scenes.ScenePresence [SCENE]:
                    # Upgrading child to root agent for Admin SIPPE in USALBIO
                    teleport_d = re.search("Upgrading child to root agent for (.+) in (.+)", line)
                    if teleport_d is not None:
                        arrival_counter = arrival_terrain_counter+1
                        if teleport_d.group(2) == teleport_region_dest_o:
                            regionteleport_d = teleport_d.group(2)
                            teleports_complete_counter = teleports_complete_counter+1
                            teleports_list[posLisAct-1].teleport_dest = str(regionteleport_d.replace (" ", "_"))
                            teleports_list[posLisAct-1].user_name = str(teleport_d.group(1).replace (" ", "_"))
                        else:
                            teleports_incomplete_counter = teleports_incomplete_counter+1
                        break
    elif line.find("Closing child agents. Checking") >= 0:
        # Example
        # 2012-07-05 09:35:02,498 DEBUG - OpenSim.Region.Framework.Scenes.ScenePresence [SCENE PRESENCE]: Closing
        # child agents. Checking 1 regions in USAL SIPPE
        teleport_source = re.search("(.+).Closing child agents. Checking (.+) regions in (.+)", line)
        if teleport_source is not None:
            out_terrain_counter = out_terrain_counter+1
    elif line.find("Removing root agent") >= 0:
        # Example
        # 2012-12-03 14:49:16,846 DEBUG - OpenSim.Region.Framework.Scenes.Scene [SCENE]: Removing root agent
        # Patricia Gonzalez f09f6a7e-2baf-4cb4-a9af-db3ca7714ad5 from USALBIO
        terrain_close = re.search(".Removing root agent (.+) (.+)from (.+)", line)
        if terrain_close is not None:
            close_terrain_counter = close_terrain_counter+1
    elif line.find("Removing child agent") >= 0:
        # Example
        # 2012-12-03 14:49:16,863 DEBUG - OpenSim.Region.Framework.Scenes.Scene [SCENE]: Removing child agent
        # Patricia Gonzalez f09f6a7e-2baf-4cb4-a9af-db3ca7714ad5 from Animal Recovery Center
        connection_close = re.search(".Removing child agent (.+) (.+)from (.+)", line)
        if connection_close is not None:
            close_connection_counter = close_connection_counter+1
    elif line.find("Upgrading child to root agent") >= 0:
        # Example
        # 2012-07-05 09:35:04,490 DEBUG - OpenSim.Region.Framework.Scenes.ScenePresence [SCENE]: Upgrading child
        # to root agent for Admin SIPPE in USALBIO
        teleport_dest = re.search(".Upgrading child to root agent for (.+) in (.+)", line)
        if teleport_dest is not None:
            arrival_terrain_counter = arrival_terrain_counter+1

teleport_source_list = []
teleport_dest_list = []
for x in teleports_list:
    if x.teleport_source not in teleport_source_list:
        teleport_source_list.append(x.teleport_source)
    if x.teleport_dest not in teleport_dest_list:
        teleport_dest_list.append(x.teleport_dest)

teleport_source_list_str = str(teleport_source_list).replace("[", "")
teleport_source_list_str = teleport_source_list_str.replace("]", "")
teleport_dest_list_str = str(teleport_dest_list).replace("[", "")
teleport_dest_list_str = teleport_dest_list_str.replace("]", "")

print "\n\nWeka Teleports\n\n"
arff = open ("teleports.arff", "w")
arff.write("% Title: Info about teleports\n% Creator: Juan Cruz-Benito\n% Date: June, 2013\n\n")
arff.write("@relation 'Teleports'\n")
arff.write("\n@attribute CLASE {CompleteTeleport, IncompleteTeleport}\n")
arff.write("@attribute user_name string\n@attribute teleport_source {"+teleport_source_list_str+"}"
           "\n@attribute teleport_dest {"+teleport_dest_list_str+"}\n@attribute date "
           "DATE yyyy-MM-dd HH:mm:ss")
arff.write("\n\n@data\n")

for x in teleports_list:
    if (x.user_name != "") or (x.teleport_dest != ""):
        arff.write("CompleteTeleport," + str(x.user_name) + "," + str(x.teleport_source) + "," + str(x.teleport_dest)
                   + "," + str(x.date_init) + " " + str(x.hour_init)+"\n")
    elif x.user_name != "":
        arff.write("IncompleteTeleport,?" + ","+str(x.teleport_source) + "," + str(x.teleport_dest)
                   + "," + str(x.date_init) + " " + str(x.hour_init)+"\n")
    elif x.teleport_dest != "":
        arff.write("IncompleteTeleport," + str(x.user_name)+"," + str(x.teleport_source)
                   + ",?," + str(x.date_init)+" " + str(x.hour_init)+"\n")
    else:
        arff.write("IncompleteTeleport,?" + "," + str(x.teleport_source) + ",?," + str(x.date_init)
                   + " " + str(x.hour_init) + "\n")

arff.close()


print "Number of teleport requests %d" % teleports_requests_counter
print "Complete teleports: %d" % teleports_complete_counter
print "Incomplete teleports: %d" % teleports_incomplete_counter
print "Departures from terrain/island: %d" % out_terrain_counter
print "Clossing connections in a terrain: %d" % close_terrain_counter
print "Clossing connections: %d" % close_connection_counter
print "Arrivals to terrain/island: %d" % arrival_terrain_counter

saveJson("real_movements", teleports_list, TeleportEncoder)
