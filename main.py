import os
import schedule
import time

# asks user for current energy bar number
current_energy = int(input("What is your current energy? "))


# runs if current energy is 50
def energy50():
    title = "Your energy bar is at 50"
    message = "Your energy bar is getting full."
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


# runs if current energy is 60
def energy60():
    title = "Your energy bar is at 60"
    message = "Your energy bar is nearly full."
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


# runs if current energy is 70
def energy70():
    title = "Your energy bar is at 70"
    message = "Your energy bar is FULL!"
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


# MacOS event notification 1
def job():
    title = "Objectives Refreshed at Noon"
    message = "Remember to do your objectives!"
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


# MacOS event notification 2
def job2():
    title = "Collect your Calendar"
    message = "The calendar refreshed at 7pm."
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


# MacOS event notification 3
def job3():
    title = "Collectors Card Refreshed"
    message = "The collectors card refreshed at midnight."
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


# run notification 1 at noon
schedule.every().day.at("12:00").do(job)

# run notification 2 at 7PM
schedule.every().day.at("19:00").do(job2)

# run notification 3 at midnight
schedule.every().day.at("00:00").do(job3)


# adds energy point to the current_energy
def energy_adder():
    global current_energy
    current_energy = current_energy + 1
    if current_energy >= 70:
        energy70()
        current_energy = 70
        print(current_energy)
    elif current_energy == 60:
        energy60()
        print(current_energy)
    elif current_energy == 50:
        energy50()
        print(current_energy)
    else:
        print(current_energy)


# runs the energy_adder every 6 minutes
schedule.every(6).minutes.do(energy_adder)

# loops the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
