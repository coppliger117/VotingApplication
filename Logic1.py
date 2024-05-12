from PyQt6.QtWidgets import *
from gui1 import *
import csv

class Logic(QMainWindow, Ui_Dialog):
    def __init__(self):
        '''
        Tells the window what to do on startup and gives color to submission notices
        
        If a csv file does not exist, a new one is created with field names.
        '''
        super().__init__()
        self.setupUi(self)
        self.hideoutput()
        self.Submit.clicked.connect(self.submit)
        self.InvalidID.setStyleSheet("color: rgb(255, 0, 0);")
        self.AlreadyVoted.setStyleSheet("color: rgb(255, 0, 0);")
        self.MustChooseCandidate.setStyleSheet("color: rgb(255, 0, 0);")
        self.SuccessfullyVoted.setStyleSheet("color: rgb(0, 0, 255);")
        
        self.votes = "votes.csv"
        
        try:
            with open(self.votes, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                firstrow = next(csvfile)
                if firstrow[0] == 'VoterID':
                    return
        except:
            with open(self.votes, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['VoterID', 'Candidate'])
                writer.writeheader()
    
    def hideoutput(self):
        '''
        Submission notices are hidden.
        '''
        self.SuccessfullyVoted.hide()
        self.AlreadyVoted.hide()
        self.MustChooseCandidate.hide()
        self.InvalidID.hide()
        
    def submit(self):
        '''
        VoterID is taken in. If it is not a 6 digit number, a notice is given.
        
        If it's the voter's first time and the vote is successfully cast, it is sent to the csv.
        '''
        VoterID = self.IDInput.text()
        if self.JaneVote.isChecked() or self.JohnVote.isChecked():
            with open(self.votes, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == VoterID:
                        self.hideoutput()
                        self.AlreadyVoted.show()
                        return
            if len(VoterID) != 6:
                self.hideoutput()
                self.InvalidID.show()
            elif not VoterID.isdigit():
                self.hideoutput()
                self.InvalidID.show()
            else:
                with open(self.votes, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    if self.JaneVote.isChecked():
                        candidate = "Jane"
                    else:
                        candidate = "John"
                    writer.writerow([VoterID, candidate])
                self.hideoutput()
                self.SuccessfullyVoted.show()
        else:
            self.hideoutput()
            self.MustChooseCandidate.show()
