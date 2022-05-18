import os
import csv

def main():
    filepath = '/home/bradlipovsky/notebooks/ess-107-intro-to-ice/grading/'
    fileprefix = 'qa2'
    filesuffix = '.ipynb'
    
    with open('students.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            name = row[0]
            netid= row[1]
            
            cmd1 = f'sudo cp /home/{netid}/notebooks/{fileprefix}{filesuffix} {filepath}{fileprefix}-{netid}{filesuffix}'
            print(cmd1)
            os.system(cmd1)

if __name__ == "__main__":
    main()
