from collections import defaultdict
"""
Python Implementation of Algorithm 1 found here: http://batog.info/papers/scalable-reward-distribution.pdf
"""
class Staker:
    # This class is only used to make things easier in this testing simulation. Not necessary in sol implementation
    def __init__(self, address, stake, balance):
        self.address = address
        self.balance = balance
        self.stake = stake
    def __str__(self):
        return "{}\nCurrent balance: {}\nCurrent Stake: {}\n".format(self.address, self.balance, self.stake)

def deposit(staker, amount):
    global T, S, stake, So
    stake[staker.address] += amount
    staker.stake += amount
    staker.balance -= amount
    So[staker.address] = S
    T += amount

def distribute(r):
    global T, S, stake, So
    if T != 0:
        S = S + r / T
    else:
        print("NO STAKERS")

# doesnt allow withdraw of specified amounts. You can only withdraw all of your stake
def withdraw(staker):
    global T, S, stake, So
    deposited = stake[staker.address]
    reward = deposited * (S-So[staker.address])
    T-= deposited
    stake[staker.address] = 0
    staker.stake = 0
    staker.balance += reward + deposited

if __name__ == "__main__":
    T = 0
    S = 0
    stake = defaultdict(int)
    So = defaultdict(int)

    user1 = Staker("User 1", 0, 100)
    user2 = Staker("User 2", 0, 1000)
    user3 = Staker("User 3", 0, 250)
    

    deposit(user1, 100)
    deposit(user2, 200)
    # testing distribution every week for 4 years (208 weeks = 4 years)
    for week in range (1, 208):
        if week == 104:
            # suddenly, two years in, user3 begins to stake
            deposit(user3, 250)
        distribute(19178.0821918)

    print("Users withdraw rewards\n".upper())
    withdraw(user1)
    withdraw(user2)
    withdraw(user3)    
    print(user1)
    print(user2)
    print(user3)