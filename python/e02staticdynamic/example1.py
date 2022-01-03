class Worker:
    def do_work(self):
        ...


def function(argument: Worker):
    argument.do_work()


class MyWorker(Worker):
    def do_work(self):
        print("I am doing a very useful thing")


function(MyWorker())
