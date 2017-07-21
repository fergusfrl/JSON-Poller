# Retrieves ORC flow data every 30 minutes and saves it as a json file
import urllib.request, json, sched, time

schedule = sched.scheduler(time.time, time.sleep)

def pollWeb(sc):
    with urllib.request.urlopen(
            "http://data.orc.govt.nz/v1/sql/TEL_RIVF/?format=json") as url:
        data = json.loads(url.read().decode())
        with open('C:/Users/Fergus/Documents/PaddleSoftware/DatabaseAccess/data.json', 'w') as outfile:
            json.dump(data, outfile)
    print("Polled")
    schedule.enter(1800, 1, pollWeb, (sc,))

schedule.enter(1800, 1, pollWeb, (schedule,))
schedule.run()