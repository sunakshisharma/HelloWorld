# import time
#
# print(time.gmtime(0))
#
# print(time.localtime(time.time()))
#
# print(time.time())

# import time
#
# print(time.gmtime(0))
#
# time_here = time.localtime()
# print(time_here)
# print("Year:-", time_here[0], time_here.tm_year) # named tuple
# print("Month:- ", time_here[1], time_here.tm_mon)
# print("Day:- ", time_here[2], time_here.tm_mday)

# Elapse Time

import time
from time import monotonic as my_timer # time or "perf_counter" (best one) or monotonic(cant not go backwards)  or process_time(not used for
# this game bcoz it give the time spent by the CPU on particular task)  is used to calculate the Elapse time
import random

input("Press enter  to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds". format(end_time - start_time))