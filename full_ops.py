# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
# Determines the output shape and operation count of a fully-connected layer
#
# Parameters:
#   c_in: input channel count
#   n_wv: number of weight vectors
#
# Output:
#   Output channel count, output height count, output width count,
#   number of additions performed, number of multiplications performed, number of divisions performed
#
# Written by: Owen Davies
# Other contributors: None
#
# import Python modules
import math  # math module
import sys   # argv

# initialize script arguments
c_in = float('nan')  # input channel count
n_wv = float('nan')  # number of weight vectors

# parse script arguments
if len(sys.argv) == 3:
    try:
        c_in = float(sys.argv[1])
        n_wv = float(sys.argv[2])
    except ValueError:
        print("Error: c_in and n_wv must be numeric.")
        print("Usage: python3 full_ops.py c_in n_wv")
        exit()
else:
    print("Usage: python3 full_ops.py c_in n_wv")
    exit()

# determine output parameters and operation counts
c_out = int(n_wv)  # output channel count
h_out = 1          # output height for fully-connected layers
w_out = 1          # output width for fully-connected layers
muls = int(n_wv * c_in)  # number of multiplications performed
adds = muls               # number of additions performed
divs = 0                  # fully-connected layers typically do not require division

# print outputs
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed