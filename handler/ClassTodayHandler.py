import time

from handler.BaseHandler import *


class ClassTodayHandler(BaseHandler):


    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        self.page_name = "class_today"

    def get(self):
        ClassTodayHandler.renderTemp(self)

    def post(self):
        self.redirect('/class_today')


    def renderTemp(self):


        # based on ADECommunicator example
        # I create empty space which name is None to have an easy display
        # The height of each class_box is computed with start_time and end_time
        classes = dict()

        class0_example = {"class_name": "CM TRAD 2 2A IL", "group": ["2A IL", "2A TRS"], "start_time": "9h00", "end_time": "10h00",
                "teacher_name": "CHAROY FRANCOIS"}
        class1_example =  {"class_name": "TP PGWEB 2A IL", "group": ["2A IL", "2A TRS"], "start_time": "10h00", "end_time": "12h00",
                "teacher_name": "CHAROY FRANCOIS"}
        class2_example = {"class_name": "None", "group": [], "start_time": "12h45", "end_time": "14h00",
                "teacher_name": ""}
        class3_example =  {"class_name": "TD MOCI 2A G1", "group": ["2A G1"], "start_time": "14h00", "end_time": "16h00",
                "teacher_name": "CHAROY FRANCOIS"}
        class4_example = {"class_name": "Exam PWEB", "group": ["2A IL"], "start_time": "16h00", "end_time": "17h00",
                "teacher_name": ""}
        class5_example =  {"class_name": "Something ...", "group": ["2A"], "start_time": "17h00", "end_time": "18h00",
                "teacher_name": "CHAROY FRANCOIS"}

        classes[0]=class0_example
        classes[1]=class1_example
        #classes[2]=class2_example
        classes[2]=class3_example
        #classes[3]=class4_example
        #classes[4]=class5_example

        hour = time.strftime("%H:%M")
        day = time.strftime("%A %d %B %Y")

        class_parameters = {'classes':classes,'day':day,'hour':hour}

        self.render('class_today.html', **class_parameters)