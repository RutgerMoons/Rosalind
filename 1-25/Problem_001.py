__author__ = 'rutger'

toParse = "GAAAGGGCGGGCATACTCTGGTGAATCAGACGGGACGTGGACATTTGGCATAGCTATGTCAATTGTCCCTTACCGATTACGTTTTACGAAGCTAGGAAAGATAAGGAGAAGAAGGACTTTGATACGGGATATCTTTGAAAGATTAAGATAAGTAATCTCTTATTATCGCATCAGCTCGCGTGGCCTAGATGCTTGTACATGGGAAGGGCCATTCCTCAGACGAAGATGATGGCTCAATCAAGTTTAAGTTGAAACCTCACTGGAGATTAGGCAACAAGAGATGGAATGTAGTAGCTTTTGTTCGAAATTGGACACGCGTCCCTACACTCTTTCAAGATGGTTCATTTTGGCATTGTCTGCCGTTATAAGGTAGCAGTTGGCCTACCTCGTGCGCGGTTATGTGGAGCCCCTATAGTCCATTTCTTAGCCCGGTTTCTGTACATTGGGAGGATACAGGTTTTGGAAGGGCTCTTTAAAACTATTCACCTTGATTAGGCTCATCCTCACCCTAACACGTACTAACCAGGAATAGCGAACAAACGCGCACATCCCTGGACGAGCCAGAAATGGCTTACAAAGGACGTGTATCCTGTTTTAGAGCAGTCAATAAATTAGGGGGGAGGTCAGGCACATAGGTAGATGCTTTTTAGAGGGGGGGGAAGCCCCGGCAATACGTATACCCGTCGGAAAACGAACACACCATCTCAGAAGTTTTTCTACATTGCCCTATTTAATGTATCGATATGTATCAGTGGTATAGCACGAATGCGAATGGCTACAGCCCGAACATGTACTGACAGTAACCGCTCGTATTTTCACGGAGCTGGACCGAAAG"
a = 0
c = 0
g = 0
t = 0

for i in range(len(toParse)):
    char = toParse[i]
    if char == "A":
        a += 1
    elif char == "C":
        c += 1
    elif char == "G":
        g += 1
    elif char == "T":
        t += 1
print("%d %d %d %d" % (a, c, g, t))