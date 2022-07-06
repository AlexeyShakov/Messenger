import sys
import datetime
import json
import requests
from requests.exceptions import HTTPError
from PyQt6 import uic, QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    server_adress = "http://localhost:5000"
    message_id = 0

    def __init__(self, *args, **kwargs):
        # inherit from the class
        super(MainWindow, self).__init__(*args, **kwargs)
        # upload the ui file with to the program
        uic.loadUi('Qtclient.ui', self)
        # create a button which sends messages
        self.pushButton1.clicked.connect(self.push_button1_clicked)

    def push_button1_clicked(self):

        self.send_message()

    def send_message(self):

        # we type this variable in the upper line in Gui
        username = self.lineEdit1.text()
        # we type it in the other line in GUI
        message_text = self.lineEdit2.text()
        # the time when a message is sent
        timestamp = str(datetime.datetime.today())
        # form the string like json format. Afterwards we will convert it to json
        msg = f"{{\"username\": \"{username}\", \"message_text\":\
        \"{message_text}\", \"timestamp\": \"{timestamp}\"}}"
        # adress where we will post the json/message
        url = self.server_adress + "/api/Messanger"
        # convert string to json
        data = json.loads(msg)
        # send post-request to serever
        r = requests.post(url, json=data)

    def get_message(self, id):

        # form the url where we get messages from
        url = self.server_adress + "/api/Messanger" + str(id)
        try:
            response = requests.get(url)
            # if the response is successful then exceptions won't be raised
            response.raise_for_status()
        except HTTPError as http_err:
            return None
        except Exception as err:
            return None
        else:
            text = response.text
            return text


    def timer_event(self):

        # get message by its id
        msg = self.get_message(self.message_id)
        """ 
        we will show all messages in the list-box in the interval of time(5000) 
        until we have not zero(len) messages
        """
        while msg is not None:
            # convert json to python dictionary
            msg = json.loads(msg)
            username = msg["username"]
            message_text = msg["message_text"]
            timestamp = msg["timestamp"]
            # we will add the text in that format to list-box
            msgtext = f"{timestamp} : <{username}> : {message_text}"
            print(msgtext)
            # add text to list-box
            self.listWidget.insertItem(self.message_id, msgtext)
            self.message_id += 1
            msg = self.get_message(self.message_id)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # open GUI
    w = MainWindow()
    w.show()
    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)
    timer.timeout.connect(w.timer_event)
    timer.start(5000)

    sys.exit(app.exec())
