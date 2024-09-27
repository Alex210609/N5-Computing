#Test scores

testscore = int(input("What did u get on the test"))
while testscore < 0 or testscore > 100:
    print("INVALID RESPONSE")
    testscore = int(input("What did u get on the test"))

print("Gud")
