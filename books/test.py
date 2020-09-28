string = "Programming_for_Computations__-_MATLAB/Octave"

if "/" in string:
    string_format = string.replace("/", "_")
    print(string_format)
else:
    print("False")