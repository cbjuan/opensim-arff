# -*- coding: utf-8 -*-

import json


class User(object):
    def __init__(self, user_id, user_name, user_surname, email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_surname = user_surname
        self.email = email
        # self.userLevel = userLevel
        # self.userTitle = userTitle


class Group(object):
    def __init__(self, group_name, group_island):
        self.group_name = group_name
        self.group_island = group_island
        self.listUsers = []
        
    def __init__(self, group_id, group_name, group_owner, group_island):
        self.group_id = group_id
        self.group_name = group_name
        self.group_owner = group_owner
        self.listUsers = []
        self.group_island = group_island

    def addUser(self, user_id):
        self.listUsers.append(user_id)


class Member(object):
    def __init__(self, group_id, user_id):
        self.group_id = group_id
        self.user_id = user_id


class Friend(object):
    def __init__(self, user_id1, user_id2):
        self.user_id1 = user_id1
        self.user_id2 = user_id2


class Session(object):
    def __init__(self, session_id, user_id, date_init, hour_init, date_fin, hour_fin, session_t):
        self.session_id = session_id
        self.user_id = user_id
        self.date_init = date_init
        self.hour_init = hour_init
        self.date_fin = date_fin
        self.hour_fin = hour_fin
        self.session_t = session_t

    def __init__(self, session_id, user_id, date_init, year_init,  month_init, day_init, hour_init, hours_init, minutes_init, seconds_init, date_fin, year_fin,  month_fin, day_fin, hour_fin, hours_fin, minutes_fin, seconds_fin, session_t):
        self.session_id = session_id
        self.user_id = user_id
        self.date_init = date_init
        self.year_init = year_init
        self.month_init = month_init
        self.day_init = day_init
        self.hour_init = hour_init
        self.hours_init = hours_init
        self.minutes_init = minutes_init
        self.seconds_init = seconds_init
        self.date_fin = date_fin
        self.year_fin = year_fin
        self.month_fin = month_fin
        self.day_fin = day_fin
        self.hour_fin = hour_fin
        self.hours_fin = hours_fin
        self.minutes_fin = minutes_fin
        self.seconds_fin = seconds_fin
        self.session_t = session_t


class Teleport(object):
    def __init__(self, user_name, date_init, hour_init, teleport_source, teleport_dest):
        self.user_name = user_name
        self.date_init = date_init
        self.hour_init = hour_init
        self.teleport_source = teleport_source
        self.teleport_dest = teleport_dest


class Click(object):
    def __init__(self, user_name, date_init, hour_init, event_type, object_id):
        self.user_name = user_name
        self.date_init = date_init
        self.hour_init = hour_init
        self.event_type = event_type
        self.object_id = object_id


class TeleportRule(object):
    def __init__(self, user_name, teleport_source, teleport_dest, probability):
        self.user_name = user_name
        self.teleport_source = teleport_source
        self.teleport_dest = teleport_dest
        self.probability = probability


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, User):
            return super(UserEncoder, self).default(obj)
        return obj.__dict__


class GroupEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Group):
            return super(GroupEncoder, self).default(obj)
        return obj.__dict__


class MembersEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Member):
            return super(GroupEncoder, self).default(obj)
        return obj.__dict__


class FriendsEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Friend):
            return super(GroupEncoder, self).default(obj)
        return obj.__dict__


class SessionEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Session):
            return super(SessionEncoder, self).default(obj)
        return obj.__dict__


class TeleportEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Teleport):
            return super(TeleportEncoder, self).default(obj)
        return obj.__dict__


class ClickEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Click):
            return super(ClickEncoder, self).default(obj)
        return obj.__dict__

class TeleportRuleEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, TeleportRule):
            return super(TeleportRuleEncoder, self).default(obj)
        return obj.__dict__

