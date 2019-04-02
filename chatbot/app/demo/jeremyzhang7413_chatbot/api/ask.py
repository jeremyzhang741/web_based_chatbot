# -*- coding: utf-8 -*-


from flask import request, g, jsonify
from rivescript import RiveScript

from . import Resource
from .. import schemas

import os
import requests
import json

bot = RiveScript()
bot.load_directory(os.path.join(os.path.dirname(__file__), "brain"))
bot.sort_replies()

class Ask(Resource):


    def post(self):
        params = request.json
        msg = params.get("input")
        if not params:
            return "Request must be of the application/json type!", 400
        username = 'apple'
        reply = bot.reply(username,msg)
        #print(reply)
        if 'appointment' in reply:
            answer = self.process_appointment(reply)
            #print(answer)
            return {"reply": answer}, 200
        elif 'hi' in msg or 'hello' in msg or 'my name' in msg:
            return {"reply": reply}, 200
        elif 'available list' in reply:
            answer = self.process_list(reply)
            #print(answer)
            return {"reply": answer}, 200
        elif 'which dentist you need' in reply:
            return {"reply": 'We have Dr.Jim, Dr.Alan and Dr.Jane. Which dentist you need?'}, 200
        elif len(reply.split()) == 1:
            answer = self.process_info(reply)
            return {"reply":answer}, 200
        elif 'timetable' in reply:
            answer = self.process_selected_list(reply)
            return {"reply": answer}, 200
        elif 'cancel' in reply and 'booking' in reply and 'id' not in reply:
            return {"reply": 'sorry you need to provide your booked time ID, after that I can help you cancel the booking.'}, 200
        elif 'cancel' in reply and 'id' in reply and 'booking' in reply:
            answer = self.process_cancel(reply)
            return {"reply": answer}, 200
        elif 'ok, sure' in reply:
            answer = self.process_list(reply)
            # print(answer)
            return {"reply": answer}, 200
        elif 'ok, wait a moment' in reply:
            return {"reply": "we have Dr.Jim, Dr.Alan and Dr.Jane here for you."}, 200
        else:
            return {"reply": reply}, 200


    def process_appointment(self,reply):
        elements = reply.split()
        if elements[1] == 'jim':
            dentist_id = 123122
            url = 'http://127.0.0.1:5000/jeremyzhang7413/DentistReservation/timeslots'
            time_id = int(elements[2])
            message = {'dentistId':dentist_id,'timeId':time_id}
            data = requests.post(url,json=message)
            data1 = data.json()
            #print(data1)
            if 'time already booked' in data1:
                query = self.process_selected_list('jim')
                result = 'sorry, your appointment time has already been booked. The following information may help {query}'.format(query=query)
                return result
            elif 'wrong input' in data1:
                return 'your input is wrong, please try again'
            else:
                return 'ok, your appointment has been reserved'
        elif elements[1] == 'alan':
            dentist_id = 123152
            url = 'http://127.0.0.1:5000/jeremyzhang7413/DentistReservation/timeslots'
            time_id = int(elements[2])
            message = {'dentistId': dentist_id, 'timeId': time_id}
            data = requests.post(url, json=message)
            data1 = data.json()
            # print(data1)
            if 'time already booked' in data1:
                query = self.process_selected_list('alan')
                result = 'sorry, your appointment time has already been booked. The following information may help {query}'.format(
                    query=query)
                return result
            elif 'wrong input' in data1:
                return 'your input is wrong, please try again'
            else:
                return 'ok, your appointment has been reserved'
        elif elements[1] == 'jane':
            dentist_id = 132112
            url = 'http://127.0.0.1:5000/jeremyzhang7413/DentistReservation/timeslots'
            time_id = int(elements[2])
            message = {'dentistId': dentist_id, 'timeId': time_id}
            data = requests.post(url, json=message)
            data1 = data.json()
            # print(data1)
            if 'time already booked' in data1:
                query = self.process_selected_list('jane')
                result = 'sorry, your appointment time has already been booked. The following information may help {query}'.format(
                    query=query)
                return result
            elif 'wrong input' in data1:
                return 'your input is wrong, please try again'
            else:
                return 'ok, your appointment has been reserved'
        else:
            return "oh, you made a mistake i can't understand."

    def process_list(self,reply):
        url = 'http://127.0.0.1:5001/jeremyzhang7413/dentist_chatbot/dentist/available_list'
        data = requests.get(url)
        data1 = data.json()
        #answer = ''
        answer = []
        for item in data1:
            if item['available'] == []:
                continue
            #answer += "{name} is available at ".format(name=item['name'])
            for n in range(len(item['available'])):
                first = item['available'][n]
                #answer += "{ll[2]}, {ll[1]} and time ID is {ll[0]}. ".format(ll=first)
                answer.append([item['name'],first[0],first[2],first[1]])
        #answer.append('please remember the time id which is shown after the doctor name, this is very useful for me.')
        return answer

    def process_info(self,reply):
        name = reply
        answer = ''
        if name == 'jim':
            id = 123122
            url = 'http://127.0.0.1:5001/jeremyzhang7413/dentist_chatbot/dentist/{id}/information'.format(id=id)
            data = requests.get(url)
            data1 = data.json()
            answer += "Dr.Jim is {age} years old, he is a {education} degree, and his specialization is {specialization}".format(
                age=data1['age'], education=data1['education'], specialization=data1['specialization'])
            return answer
        elif name == 'alan':
            id = 123152
            url = 'http://127.0.0.1:5001/jeremyzhang7413/dentist_chatbot/dentist/{id}/information'.format(id=id)
            data = requests.get(url)
            data1 = data.json()
            answer += "Dr.Alan is {age} years old, he is a {education} degree, and his specialization is {specialization}".format(
                age=data1['age'], education=data1['education'], specialization=data1['specialization'])
            return answer
        elif name == 'jane':
            id = 132112
            url = 'http://127.0.0.1:5001/jeremyzhang7413/dentist_chatbot/dentist/{id}/information'.format(id=id)
            data = requests.get(url)
            data1 = data.json()
            #print(data1)
            answer += "Dr.Jane is {age} years old, he is a {education} degree, and his specialization is {specialization}".format(
                age=data1['age'],education=data1['education'],specialization=data1['specialization'])
            return answer
        else:
            return "oh, you made a mistake i can't understand."

    def process_selected_list(self,reply):
        elements = reply.split()
        url = 'http://127.0.0.1:5000/jeremyzhang7413/DentistReservation/timeslots'
        data = requests.get(url)
        data1 = data.json()
        #answer = 'Dr.Jim is available at:<br /> '
        #answer1 = 'Dr.Alan is available at:<br /> '
        #answer2 = 'Dr.Jane is available at:<br /> '
        answer = []
        answer1 = []
        answer2 = []
        for item in data1:
            if elements[0] == 'jim':
                dentist_id = 123122
                if item['dentistId'] == dentist_id:
                    answer.append(['Jim',item['timeId'],item['timeslot'],item['data']])
                    continue
            elif elements[0] == 'alan':
                dentist_id = 123152
                if item['dentistId'] == dentist_id:
                    answer1.append(['Alan', item['timeId'], item['timeslot'], item['data']])
                    continue
            elif elements[0] == 'jane':
                dentist_id = 132112
                if item['dentistId'] == dentist_id:
                    answer2.append(['Jane', item['timeId'], item['timeslot'], item['data']])
                    continue
            else:
                return "oh, you made a mistake i can't understand."
        if elements[0] == 'jim':
            if answer == []:
                return 'Sorry, Dr.Jim does not have any time. You can try other doctors, Alan or Jane.'
            else:
                return answer
        elif elements[0] == 'alan':
            if answer1 == []:
                return 'Sorry, Dr.Alan does not have any time. You can try other doctors, Jim or Jane.'
            else:
                return answer1
        elif elements[0] == 'jane':
            if answer2 == []:
                return 'Sorry, Dr.Jane does not have any time. You can try other doctors, Alan or Jim.'
            else:
                return answer2
        else:
            return "oh, you made a mistake i can't understand."


    def process_cancel(self,reply):
        elements = reply.split()
        if len(elements) == 4:
            return 'sorry, your input id is wrong, try again.'
        time_id = int(elements[4])
        #print(time_id)
        url = 'http://127.0.0.1:5000/jeremyzhang7413/DentistReservation/timeslots'
        timedir = {'timeId':time_id}
        data = requests.put(url,json=timedir)
        #print(data.status_code)
        if data.status_code == 200:
            return 'your appointment is canceled, you can check it by asking show me the timetable now.'
        data1 = data.json()
        #print(data1)
        if data1 == 'this timeslot not been reserved':
            return 'sorry, this timeslot is not reserved. Maybe your input is wrong.'
        if data1 == "wrong input":
            return 'sorry, your input id is wrong, try again.'
