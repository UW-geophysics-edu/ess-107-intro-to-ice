import os
import csv
def main():
    filepath = '/home/bradlipovsky/notebooks/ess-107-intro-to-ice/assignments/'
    filename = 'orbit91'
    with open('students.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            name = row[0]
            netid= row[1]

            cmd1 = 'sudo cp %s /home/%s/notebooks/'%(filepath+filename,netid)
            print(cmd1)
            os.system(cmd1)

            cmd2 = f'sudo chgrp {netid} /home/{netid}/notebooks/{filename}' 
            print(cmd2)
            os.system(cmd2)

            cmd3 = f'sudo chown {netid} /home/{netid}/notebooks/{filename}' 
            print(cmd3)
            os.system(cmd3)

if __name__ == "__main__":
    main()
