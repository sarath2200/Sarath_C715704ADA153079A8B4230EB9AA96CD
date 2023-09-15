# Python3 program to calculate strike
# rate of a batsman
 
# function to calculate strike
# rate of a batsman
def strikerate(bowls, runs):
 
    z = (float(runs) / bowls) * 100;
    return z;
 
# Driver Code
A = 264;
B = 173;
print(strikerate(B, A));
 
# This code is contributed by Code_Mech
