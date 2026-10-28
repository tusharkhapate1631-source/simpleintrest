import sys
prinicipal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])
interest = (prinicipal * rate * time) / 100
print("simple Interest: ",interest)