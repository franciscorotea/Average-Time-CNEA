import re

from datetime import datetime, timedelta

# Pattern for HHmm HHmm.

pattern = '^([01]\d|2[0-3]):?([0-5]\d) ([01]\d|2[0-3]):?([0-5]\d)$'

def average_time():

    i = 1

    results = []

    # Get times

    while True:
        
        answer = input(f'\nDay {i}: E-CAC S-CAC = ')
        
        if answer == 'end':
            break

        match_pattern = re.match(pattern, answer)

        if not match_pattern:
            print(f'Invalid input. Try again with the following format: HHmm HHmm, where HHmm is the entry/exit hours in 24-hour format.')
            continue
        
        start_time, end_time = answer.split()
    
        date_start_time = datetime.strptime(start_time, '%H%M')
        date_end_time = datetime.strptime(end_time, '%H%M')
        
        time = date_end_time - date_start_time

        if time < timedelta():
            print(f'Invalid input. The entry time cannot occur after the exit time.')
            continue            

        print(f'You worked {time} hours in day {i}.')

        i = i + 1

        results.append(time)

    # Average

    total_time = timedelta()

    if not results:
        
        print(f'\nAverage hours could not be calculated.')
        
    else:
        
        for result in results:
            total_time = total_time + result

        average_time = total_time/len(results)

        print(f'\nYou worked an average of {average_time} hours.')
