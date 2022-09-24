from stats_calculator import Stats_Calculator

class Player():
    def __init__(self):

        # lists of raw extracted data
        self.two = []
        self.cornerThree = []
        self.nonCornerThree = []

        # count of attempted shots
        self.attempted2PT = 0
        self.attemptedC3 = 0
        self.attemptedNC3 = 0
        self.attempted = 0

        # count of made shots
        self.made2PT = 0
        self.madeC3 = 0
        self.madeNC3 = 0
        self.made = 0

        # percentage of shots taken
        self.zone2PT = 0.0
        self.zoneC3 = 0.0
        self.zoneNC3 = 0.0
        self.zone3 = 0.0    #C3 + NC3

        # effective field goal percentage
        self.eFGp2PT = 0.0
        self.eFGpC3 = 0.0
        self.eFGpNC3 = 0.0
        self.eFGp3 = 0.0    #C3 + NC3

    # extracts data from given row in CSV File
    def addShot(self, row):
        if(abs(float(row[2])) <= 7.8):  # if shot was taken within 7.8 ft from the x-axis (x <= 7.8)
            if(abs(float(row[1])) < 22):   # inside 22ft from the corner = two pt
                self.attempted2PT += 1  # +1 to 2pt attempt
                self.attempted += 1 # +1 to total attempt
                
                if(int(row[3]) == 1):   # +1 to 2pt made and shot made
                    self.made2PT += 1
                    self.made += 1    
                
                self.updateZones() # update zones after new shot attempt
                self.eFGp2PT = Stats_Calculator.updateEFGP(self.made2PT, self.attempted2PT)   # update 2PT EFG%
                
                self.two.append(row)    # add data to two pointers list 

            else:   # 22ft and beyond from the corner = corner three
                self.attemptedC3 += 1  # +1 to corner 3 attempt
                self.attempted += 1 # +1 to total attempt

                if(int(row[3]) == 1):   # +1 to corner 3 and shot made
                    self.madeC3 += 1    
                    self.made += 1

                self.updateZones() # update zones after new shot attempt
                self.eFGpC3 = Stats_Calculator.update3EFGP(self.madeC3, self.attemptedC3)   # update C3 EFG%
                
                self.cornerThree.append(row)    # add data to corner 3 list 
            
        else:   # if shot was taken beyond 7.8 ft from the x-axis (x > 7.8 ft)
            if(float(row[1])**2 + float(row[2])**2 < 564.0625):   #pyt. theorem - inside 23.75ft from the arc = two pt
                self.attempted2PT += 1  # +1 to 2pt attempt
                self.attempted += 1 # +1 to total attempt

                if(int(row[3]) == 1):   # +1 to 2pt made and shot made
                    self.made2PT += 1
                    self.made += 1
                
                self.updateZones() # update zones after new shot attempt
                self.eFGp2PT = Stats_Calculator.updateEFGP(self.made2PT, self.attempted2PT)   # update 2PT EFG%
                self.two.append(row)    # add data to two pointers list 

            else:   # 23.75ft and beyond from the arc = non corner three
                self.attemptedNC3 += 1  # +1 to non corner 3 attempt
                self.attempted += 1 # +1 to total attempt

                if(int(row[3]) == 1):   # +1 to non corner 3 made and shot made
                    self.madeNC3 += 1
                    self.made += 1    
                
                self.updateZones() # update zones after new shot attempt
                self.eFGpNC3 = Stats_Calculator.update3EFGP(self.madeNC3, self.attempted)   # update NC3 EFG%

                self.nonCornerThree.append(row)    # add data to non corner 3 list
    
    # updates zones after new shot attempt
    def updateZones(self):
        self.zone2PT = Stats_Calculator.updateZone(self.attempted2PT, self.attempted) # update 2PT zone
        self.zoneC3 = Stats_Calculator.updateZone(self.attemptedC3, self.attempted) # update C3 zone
        self.zoneNC3 = Stats_Calculator.updateZone(self.attemptedNC3, self.attempted) # update NC3 zone
        


    # prints calculated percentages for each zone
    def printStats(self):
        print("Percentage of shots attempted in 2PT Zone: " + str(self.zone2PT))
        print("Percentage of shots attempted in NC3 Zone: " + str(self.zoneNC3))
        print("Percentage of shots attempted in C3 Zone: " + str(self.zoneC3))
        print("Effective FG Percentage in 2PT Zone: " + str(self.eFGp2PT))
        print("Effective FG Percentage in NC3 Zone: " + str(self.eFGpNC3))
        print("Effective FG Percentage in C3 Zone: " + str(self.eFGpC3))
