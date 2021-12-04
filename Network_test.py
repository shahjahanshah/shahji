import logging
import socket


from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
PORT = 22

# @sched.scheduled_job('interval', seconds=10)
def timed_job():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_dict = {"u1e175528a4925e": "10.219.214.63", "ud2c7b9e89cb851": "10.219.214.63",
               "u1d52c748966c51": "10.219.214.28"}

    for x in my_dict.values():
        print("Getting Ip address",x)
        location = (x, PORT)
        result_of_check = a_socket.connect_ex(location)
        print("Test", result_of_check)
        if result_of_check == 0:
           print("Host is up and running", x)
        else:
           print("Port is not open")


        print('checking other Hosts')


scheduler.add_job(timed_job, 'interval', seconds=5)
scheduler.start()
