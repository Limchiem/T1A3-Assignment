class atm_user():
    def __init__(self, userId, userPin):
        self.userId = userId
        self.userPin = userPin

    def get_userId(self):
        return self.userId
    
    def get_userPin(self):
        return self.userPin
    
    def set_userId(self, x):
        self.userId = x
        
    def set_userPin(self, x):
        self.userPin = x
        
    def run(self):
        print("User: ", self.userId)
        print("Pin: ", self.userPin)