from flask import Flask, request
#
app = Flask(__name__)

# we store all of our messages in that list
list_of_messages = []


@app.route('/')
def hello_world():
    return 'Messenger Flask server is running! ' \
           '<br> <a href="/status">Check status</a>'

# checking the amount of messages sent
@app.route('/status')
def status():
    return {
        'messages_count': len(list_of_messages)
    }

@app.route("/api/Messanger", methods=['POST'])
def send_message():

    # convert .json file to needed format
    msg = request.json
    print(msg)
    """
    example of msg: { "UserName":"RusAl","MessageText":"Privet na sto let!!!",
    "TimeStamp":"2021-03-05T18:23:10.932973Z"}.
    So we've got just a dictionary with the main information
    """
    list_of_messages.append(msg)
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(list_of_messages)} Посланное сообщение: {msgtext}")

    return f"Сообщение отослано успешно. Всего сообщений: {len(list_of_messages)} ", 200

@app.route("/api/Messanger/<int:id>")
def get_message(id):
    print(id)
    if id >= 0 and id < len(list_of_messages):
        print(list_of_messages[id])
        return list_of_messages[id], 200
    else:
        return "Not found", 400

"""
if __name__ == __main__ indicates that we can launch this script filly if we launch it straitforward.
If we don't have  if __name__ == __main__ then while importing the file to another file we will
launch the whole code automatically but it's not a proper way. So we should use this expression to be able of
taking just needed parts of the code while importing it.
"""
if __name__ == '__main__':
    app.run(debug=True)

