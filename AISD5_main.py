import AISD5_def
import time
import csv


size_1 = 5 #TUTAJ W OKOLICACH 12 ELEMENTÓW TAK W SAM RAZ (MAX CZAS 15s)
size_2 = 5  #DP tutaj tak 50 elementow bedzie git
size_3 = 5  #BF tutaj 12
size_4 = 5  #BF2 tutaj 18
size_5 = 5  #GH4 tutaj 20000 elem to minimum
size_6 = 50 #taki sam jak size_2 wsn

z2_times_BF = []
z2_times_BF2 = []
z2_times_DP = []
z2_times_GH4 = []

z3_times_BF_25 = []
z3_times_BF2_25 = []
z3_times_DP_25 = []
z3_times_GH4_25 = []
z3_times_BF_75 = []
z3_times_BF2_75 = []
z3_times_DP_75 = []
z3_times_GH4_75 = []

z4_results_DP_25 = []
z4_results_DP_50 = []
z4_results_DP_75 = []
z4_results_GH1_25 = []
z4_results_GH1_50 = []
z4_results_GH1_75 = []
z4_results_GH2_25 = []
z4_results_GH2_50 = []
z4_results_GH2_75 = []
z4_results_GH3_25 = []
z4_results_GH3_50 = []
z4_results_GH3_75 = []
z4_results_GH4_25 = []
z4_results_GH4_50 = []
z4_results_GH4_75 = []


############# task 2 #############
for i in range(10):
    n = size_1 + i

    items = AISD5_def.randomize_items(n)
    b = AISD5_def.b_factor(items, 0.5)

    ##### DP #####
    st = time.time()
    resultDP, array = AISD5_def.array_DP(items, b)
    en = time.time()
    z2_times_DP.append(en - st)
    print("DP ", en-st, resultDP)


    ##### BF #####
    st = time.time()
    resultBF, permutation = AISD5_def.bf(items, b)
    en = time.time()
    z2_times_BF.append(en-st)
    print("BF ", en-st, resultBF)

    ##### BF2 #####
    st = time.time()
    resultBF2 = AISD5_def.bf2(items, b)
    en = time.time()
    z2_times_BF2.append(en - st)
    print("BF2 ", en - st, resultBF2)

    ##### GH4 #####
    st = time.time()
    resultGH4 = AISD5_def.GH4(items, b)
    en = time.time()
    z2_times_GH4.append(en - st)

    print("GH4 ", en - st, resultGH4)

    print("-----", n, "-----")
print("<----------------------------------------------------------------------------------->")
############# task 3 #############
for i in range(10):
    n1 = size_2 + (i * 5)  # DP
    n2 = size_3 + i  # BF
    n3 = size_4 + i  # BF2
    n4 = size_5 * (i + 1)  # GH4

    items_1 = AISD5_def.randomize_items(n1)
    items_2 = AISD5_def.randomize_items(n2)
    items_3 = AISD5_def.randomize_items(n3)
    items_4 = AISD5_def.randomize_items(n4)

    b1_25 = AISD5_def.b_factor(items_1, 0.25)
    b1_75 = AISD5_def.b_factor(items_1, 0.75)
    b2_25 = AISD5_def.b_factor(items_2, 0.25)
    b2_75 = AISD5_def.b_factor(items_2, 0.75)
    b3_25 = AISD5_def.b_factor(items_3, 0.25)
    b3_75 = AISD5_def.b_factor(items_3, 0.75)
    b4_25 = AISD5_def.b_factor(items_4, 0.25)
    b4_75 = AISD5_def.b_factor(items_4, 0.75)

    ##### DP 0.25 #####
    st = time.time()
    resultDP, array = AISD5_def.array_DP(items_1, b1_25)
    en = time.time()
    z3_times_DP_25.append(en - st)
    print("DP 25 ", en - st, resultDP)

    ##### DP 0.75 #####
    st = time.time()
    resultDP, array1 = AISD5_def.array_DP(items_1, b1_75)
    en = time.time()
    z3_times_DP_75.append(en - st)
    print("DP 75 ", en - st, resultDP)

    ##### BF 0.25 #####
    st = time.time()
    resultDP, permutation = AISD5_def.bf(items_2, b2_25)
    en = time.time()
    z3_times_BF_25.append(en - st)
    print("BF 25 ", en - st, resultDP)

    ##### BF 0.75 #####
    st = time.time()
    resultDP, permutation1 = AISD5_def.bf(items_2, b2_75)
    en = time.time()
    z3_times_BF_75.append(en - st)
    print("BF 75 ", en - st, resultDP)

    ##### BF2 0.25 #####
    st = time.time()
    resultDP = AISD5_def.bf2(items_3, b3_25)
    en = time.time()
    z3_times_BF2_25.append(en - st)
    print("BF2 25 ", en - st, resultDP)

    ##### BF2 0.75 #####
    st = time.time()
    resultDP = AISD5_def.bf2(items_3, b3_75)
    en = time.time()
    z3_times_BF2_75.append(en - st)
    print("BF2 75 ", en - st, resultDP)

    ##### GH4 0.25 #####
    st = time.time()
    resultDP = AISD5_def.GH4(items_4, b4_25)
    en = time.time()
    z3_times_GH4_25.append(en - st)
    print("GH4 25 ", en - st, resultDP)

    ##### GH4 0.75 #####
    st = time.time()
    resultDP = AISD5_def.GH4(items_4, b4_75)
    en = time.time()
    z3_times_GH4_75.append(en - st)
    print("GH4 75 ", en - st, resultDP)

    print("-----", i+1, "-----")

print("<----------------------------------------------------------------------------------->")
############# task 3 #############
for i in range(10):
    n = size_6 + (i * 5)

    items = AISD5_def.randomize_items(n)

    b_25 = AISD5_def.b_factor(items, 0.25)
    b_50 = AISD5_def.b_factor(items, 0.50)
    b_75 = AISD5_def.b_factor(items, 0.75)

    ##### DP 25 #####
    #st = time.time()
    resultDP, array = AISD5_def.array_DP(items, b_25)
    #en = time.time()
    z4_results_DP_25.append(resultDP)
    print("DP 25 ", resultDP)

    ##### DP 50 #####
    # st = time.time()
    resultDP, array = AISD5_def.array_DP(items, b_50)
    # en = time.time()
    z4_results_DP_50.append(resultDP)
    print("DP 50 ", resultDP)

    ##### DP 25 #####
    # st = time.time()
    resultDP, array = AISD5_def.array_DP(items, b_75)
    # en = time.time()
    z4_results_DP_75.append(resultDP)
    print("DP 75 ", resultDP)

    ##### GH1 25 #####
    # st = time.time()
    resultDP, array = AISD5_def.GH1(items, b_25)
    # en = time.time()
    z4_results_GH1_25.append(resultDP)
    print("GH1 25 ", resultDP)

    ##### GH1 50 #####
    # st = time.time()
    resultDP, array = AISD5_def.GH1(items, b_50)
    # en = time.time()
    z4_results_GH1_50.append(resultDP)
    print("GH1 50 ", resultDP)

    ##### GH1 75 #####
    # st = time.time()
    resultDP, array = AISD5_def.GH1(items, b_75)
    # en = time.time()
    z4_results_GH1_75.append(resultDP)
    print("GH1 75 ", resultDP)

    ##### GH2 25 #####
    # st = time.time()
    resultDP = AISD5_def.GH2(items, b_25)
    # en = time.time()
    z4_results_GH2_25.append(resultDP)
    print("GH2 25 ", resultDP)

    ##### GH2 50 #####
    # st = time.time()
    resultDP = AISD5_def.GH2(items, b_50)
    # en = time.time()
    z4_results_GH2_50.append(resultDP)
    print("GH2 50 ", resultDP)

    ##### GH2 75 #####
    # st = time.time()
    resultDP = AISD5_def.GH2(items, b_75)
    # en = time.time()
    z4_results_GH2_75.append(resultDP)
    print("GH2 75 ", resultDP)

    ##### GH3 25 #####
    # st = time.time()
    resultDP = AISD5_def.GH3(items, b_25)
    # en = time.time()
    z4_results_GH3_25.append(resultDP)
    print("GH3 25 ", resultDP)

    ##### GH3 50 #####
    # st = time.time()
    resultDP = AISD5_def.GH3(items, b_50)
    # en = time.time()
    z4_results_GH3_50.append(resultDP)
    print("GH3 50 ", resultDP)

    ##### GH3 75 #####
    # st = time.time()
    resultDP = AISD5_def.GH3(items, b_75)
    # en = time.time()
    z4_results_GH3_75.append(resultDP)
    print("GH3 75 ", resultDP)

    ##### GH4 25 #####
    # st = time.time()
    resultDP = AISD5_def.GH4(items, b_25)
    # en = time.time()
    z4_results_GH4_25.append(resultDP)
    print("GH4 25 ", resultDP)

    ##### GH4 50 #####
    # st = time.time()
    resultDP = AISD5_def.GH4(items, b_50)
    # en = time.time()
    z4_results_GH4_50.append(resultDP)
    print("GH4 50 ", resultDP)

    ##### GH4 75 #####
    # st = time.time()
    resultDP = AISD5_def.GH4(items, b_75)
    # en = time.time()
    z4_results_GH4_75.append(resultDP)
    print("GH4 75 ", resultDP)

    print("-----", i+1, "-----")



# with open('PP task 2.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["czas DP"] + ["czas BF"] + ["czas BF2"] + ["czas GH4"])
#     for i in range(10):
#         writer.writerow([size_1 + i] + [z2_times_DP[i]] + [z2_times_BF[i]] + [z2_times_BF2[i]] + [z2_times_GH4[i]])
#
# with open('PP task 3 DP.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["czas DP 0.25"] + ["czas DP 0.75"])
#     for i in range(10):
#         writer.writerow([size_2 + (i * 5)] + [z3_times_DP_25[i]] + [z3_times_DP_75[i]])
#
# with open('PP task 3 BF.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["czas BF 0.25"] + ["czas BF 0.75"])
#     for i in range(10):
#         writer.writerow([size_3 + i] + [z3_times_BF_25[i]] + [z3_times_BF_75[i]])
#
# with open('PP task 3 BF2.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["czas BF2 0.25"] + ["czas BF2 0.75"])
#     for i in range(10):
#         writer.writerow([size_4 + i] + [z3_times_BF2_25[i]] + [z3_times_BF2_75[i]])
#
# with open('PP task 3 GH4.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["czas GH4 0.25"] + ["czas GH4 0.75"])
#     for i in range(10):
#         writer.writerow([size_5 * (i + 1)] + [z3_times_GH4_25[i]] + [z3_times_GH4_75[i]])
#
# with open('PP task 4 25.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["result DP"] + ["result GH1"] + ["result GH2"] + ["result GH3"] + ["result GH4"])
#     for i in range(10):
#         writer.writerow([size_6 + (i * 5)] + [z4_results_DP_25[i]] + [z4_results_GH1_25[i]] + [z4_results_GH2_25[i]] + [z4_results_GH3_25[i]] + [z4_results_GH4_25[i]])
#
# with open('PP task 4 50.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["result DP"] + ["result GH1"] + ["result GH2"] + ["result GH3"] + ["result GH4"])
#     for i in range(10):
#         writer.writerow([size_6 + (i * 5)] + [z4_results_DP_50[i]] + [z4_results_GH1_50[i]] + [z4_results_GH2_50[i]] + [z4_results_GH3_50[i]] + [z4_results_GH4_50[i]])
#
# with open('PP task 4 75.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Liczba paczek"] + ["result DP"] + ["result GH1"] + ["result GH2"] + ["result GH3"] + ["result GH4"])
#     for i in range(10):
#         writer.writerow([size_6 + (i * 5)] + [z4_results_DP_75[i]] + [z4_results_GH1_75[i]] + [z4_results_GH2_75[i]] + [z4_results_GH3_75[i]] + [z4_results_GH4_75[i]])