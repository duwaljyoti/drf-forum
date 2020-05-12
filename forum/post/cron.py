from django_cron import CronJobBase, Schedule
import datetime
import os


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'forum.MyCronJob'

    def do(self):
        file1 = open(r'/home/iw-jay/Desktop/misc/test.txt', 'a')
        file1.write('sfdsfsdf')
        file1.close()
        path = '/home/iw-jay/projects/playground/testa'
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)
        a = datetime.datetime.now()

        print('something here', "%s:%s.%s" % (a.minute, a.second, str(a.microsecond)[:2]))
