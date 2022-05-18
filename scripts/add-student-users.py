import os
import csv
def main():
    with open('new-users.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            name = row[0]
            netid= row[1]
            cmd1 = 'sudo useradd -c "%s,Students,-,@uw" %s'%(name,netid)
            cmd2 = 'sudo usermod -a -G jupyter_users %s'%netid
            os.system(cmd1)
            os.system(cmd2)

if __name__ == "__main__":
    main()
