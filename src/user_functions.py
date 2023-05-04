class atm_user():
    def __init__(self, userId, userPin):
        self.userId = userId
        self.userPin = userPin

    def get_userId(self):
        return self.userId
    
    def get_userPin(self):
        return self.userPin
    
    def run(self):
        print("User: ", self.userId)
        print("Pin: ", self.userPin)