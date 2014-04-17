__author__ = 'Mael Beuget, Pierre Monnin & Thibaut Smith'

from XMLAnalyser import *
from google.appengine.api import memcache

class ADECommunicator():
    parser = None

    def __init__(self):
        self.parser = XMLAnalyser()

    def get_students_groups(self):
        groups = memcache.get("group_list")

        if groups is None:
            logging.error("CACHE MISS StudentsListHandler l. 24")
            groups = self.parser.get_members()
            memcache.set("group_list", groups, time=604800)

        return groups

    def get_teacher_class(self, teacher, time, date):
        #WARNING should be coded
        return {"class_name": "TP PGWEB 2A IL", "group": ["2A IL", "2A TRS"], "start_time": "10h00", "end_time": "12h00",
                "teacher_name": "CHAROY FRANCOIS"}