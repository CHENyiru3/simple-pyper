def plus(A,B):
    c = A+B
    return c

def main(inputas_A,inputas_B,outputas_C):
    result = plus(inputas_A,inputas_B)
    with open(outputas_C, "w") as file:
        file.write(result)