import matplotlib.pyplot as plt
from sort import *


def plotAminoPercentage(amino_seq):
    amino_count = {}
    list_x = []
    list_y = []

    for i in range(0, len(amino_seq)):
        if not(amino_seq[i] in amino_count.keys()):
            amino_count[amino_seq[i]] = 0
        amino_count[amino_seq[i]] += 1

    total_count = 0
    for value in amino_count.values():
        total_count += value

    for key, value in amino_count.items():
        list_x.append(key)
        list_y.append((value * 100.0) / total_count)

    merge_sort(list_x, list_y, 0, len(list_x)-1)

    plt.bar([i for i in range(1, len(list_x) + 1)], list_y, tick_label = list_x, width = 0.9, color = ['blue', 'red'])
    for index, value in enumerate(list_y):
        plt.text(index + 1, value, str(int(value * 10) / 10.0), ha = 'center')

    plt.xlabel('Amino Acid')
    plt.ylabel('Percentage')

    plt.title('Amino Acid Percentage Bar Chart')

    figManager = plt.get_current_fig_manager()
    figManager.window.state("zoomed")

    plt.show()
    return

def plotATGCSkew(code_seq):
    length = int(len(code_seq) / 100) * 100
    code_seq = code_seq[:length]

    A_Freq = []
    T_Freq = []
    G_Freq = []
    C_Freq = []
    for i in range(0, len(code_seq), 100):
        ATGC_Freq = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        for j in range(i, i + 100):
            ATGC_Freq[code_seq[j].upper()] += 1
        A_Freq.append(ATGC_Freq['A'])
        T_Freq.append(ATGC_Freq['T'])
        G_Freq.append(ATGC_Freq['G'])
        C_Freq.append(ATGC_Freq['C'])

    AT_Freq = []
    GC_Freq = []
    for i in range(0, len(A_Freq)):
        AT_Freq.append((A_Freq[i] - T_Freq[i]) / (A_Freq[i] + T_Freq[i]))
        GC_Freq.append((G_Freq[i] - C_Freq[i]) / (G_Freq[i] + C_Freq[i]))

    AT_Cumulative_Freq = []
    GC_Cumulative_Freq = []
    AT_Current_Freq = 0
    GC_Current_Freq = 0
    for i in range(0, len(AT_Freq)):
        AT_Current_Freq += AT_Freq[i]
        GC_Current_Freq += GC_Freq[i]
        AT_Cumulative_Freq.append(AT_Current_Freq)
        GC_Cumulative_Freq.append(GC_Current_Freq)

    x_axis = [i for i in range(0, len(AT_Cumulative_Freq))]

    plt.figure()
    plt.plot(x_axis, AT_Cumulative_Freq)
    if(AT_Cumulative_Freq != []):
        ATmaxIndex = AT_Cumulative_Freq.index(max(AT_Cumulative_Freq))
        ATminIndex = AT_Cumulative_Freq.index(min(AT_Cumulative_Freq))
        ATscatterPlotX = [ATminIndex, ATmaxIndex]
        ATscatterPlotY = [AT_Cumulative_Freq[ATminIndex], AT_Cumulative_Freq[ATmaxIndex]]
        plt.scatter(ATscatterPlotX, ATscatterPlotY, color = 'red')
        plt.annotate('Min', (ATscatterPlotX[0], ATscatterPlotY[0]))
        plt.annotate('Max', (ATscatterPlotX[1], ATscatterPlotY[1]))
    plt.title('AT-Skew')

    figManager = plt.get_current_fig_manager()
    figManager.window.state("zoomed")

    plt.figure()
    plt.plot(x_axis, GC_Cumulative_Freq)
    if(GC_Cumulative_Freq != []):
        GCmaxIndex = GC_Cumulative_Freq.index(max(GC_Cumulative_Freq))
        GCminIndex = GC_Cumulative_Freq.index(min(GC_Cumulative_Freq))
        GCscatterPlotX = [GCminIndex, GCmaxIndex]
        GCscatterPlotY = [GC_Cumulative_Freq[GCminIndex], GC_Cumulative_Freq[GCmaxIndex]]
        plt.scatter(GCscatterPlotX, GCscatterPlotY, color = 'red')
        plt.annotate('Min', (GCscatterPlotX[0], GCscatterPlotY[0]))
        plt.annotate('Max', (GCscatterPlotX[1], GCscatterPlotY[1]))
    plt.title('GC_Skew')

    figManager = plt.get_current_fig_manager()
    figManager.window.state("zoomed")

    plt.show()
    return
