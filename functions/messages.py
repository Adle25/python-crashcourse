messages = ['hello', 'ok, i will do it', 'nicely done']
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f'Sending message: {current_message}')
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)
show_messages(sent_messages)
print(messages)