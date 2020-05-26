from data import *
from validate import *
from plot import *

def getAminoCode(seq):
    index_row = 0
    index_col = 0
    multiplier = 1
    for i in range(0, len(seq)):
        if(i % 2 == 0):
            if(seq[i] == 'U' or seq[i] == 'u' or seq[i] == 'T' or seq[i] == 't'):
                index_row += 0 * (4 / multiplier)
            elif(seq[i] == 'C' or seq[i] == 'c'):
                index_row += 1 * (4 / multiplier)
            elif(seq[i] == 'A' or seq[i] == 'a'):
                index_row += 2 * (4 / multiplier)
            elif(seq[i] == 'G' or seq[i] == 'g'):
                index_row += 3 * (4 / multiplier)
            multiplier *= 4
        else:
            if(seq[i] == 'U' or seq[i] == 'u' or seq[i] == 'T' or seq[i] == 't'):
                index_col += 0 * (4 / multiplier)
            elif(seq[i] == 'C' or seq[i] == 'c'):
                index_col += 1 * (4 / multiplier)
            elif(seq[i] == 'A' or seq[i] == 'a'):
                index_col += 2 * (4 / multiplier)
            elif(seq[i] == 'G' or seq[i] == 'g'):
                index_col += 3 * (4 / multiplier)
    return codon[int(index_row)][int(index_col)]

def checkMultiple(n, no):
    if(n % no == 0):
        return True
    return False

def stopAtEnd(line):
    end = line[-3:]
    if(getAminoCode(end.upper())[1] == 'STOP'):
        return True
    return False

def stopInBetween(code_seq):
    for i in range(0, len(code_seq) - 3, 3):
        if(getAminoCode(code_seq[i:i+3]) == 'STOP'):
            return True
    return False
    
def allIn(line, charcters):
    for i in range(0,len(line)):
        if not(line[i].upper() in charcters):
            return False
    return True

def getNextValidSequence(file_read):

    seq_info = ''
    code_seq = ''

    line = file_read.file.readline()
    while(len(line) == 1 and line[0] == '\n'):
        line = file_read.file.readline()
    if(len(line) == 0):
        print('EOF Reached')
        return ('','',0)
    elif(line[0] == '>'):
        seq_info += line[:-1]
        line = file_read.file.readline()
        while(len(line) != 0 and line[0] != '\n' and line[0] != '>'):
            code_seq += line[:-1]
            line = file_read.file.readline()
        file_read.file.seek(file_read.file.tell() - len(line),0)
        if(checkMultiple(len(code_seq), 3) == False or stopInBetween(code_seq) == True or stopAtEnd(code_seq) == False or not(allIn(code_seq, ['A','T','G','C']) or allIn(code_seq, ['A','U','G','C']))):
            print('Invalid Sequence Found')
            print('1 - Try Next Sequence')
            print('Else - Return to Main Menu')
            response = getInt()
            if(response == 1):
                return getNextValidSequence(file_read)
            else:
                return ('','',0)
        return (seq_info, code_seq, 1)
    else:
        print('Invalid Sequence Found')
        print('1 - Try Next Sequence')
        print('Else - Return to Main Menu')
        response = getInt()
        if(response == 1):
            return getNextValidSequence(file_read)
        else:
            return('','', 0)
    return

def getAminoSequence(code_seq):
    amino_seq = ''
    for i in range(0, len(code_seq) - 3, 3):
        amino_seq += getAminoCode(code_seq[i:i+3])[1]
    return amino_seq

def processNextSequence(file_read, file_write, database):

    seq_info = ''
    code_seq = ''
    amino_seq = ''
    file_written = 0
    database_written = 0
    valid = 0

    (seq_info, code_seq, valid) = getNextValidSequence(file_read)
    
    if(valid == 0):
        return

    amino_seq = getAminoSequence(code_seq)
    
    while(True):
        print()
        print('1 - Print Amino Sequence')
        print('2 - Push to File')
        print('3 - Push to Database')
        print('4 - Plot Amino Percentage')
        print('5 - Plot AT/GC Skew')
        print('Else - Back')
        response = getInt()

        if(response == 1):
            print()
            print(seq_info)
            print(code_seq)
            print(amino_seq)
        elif(response == 2):
            if(file_written == 1):
                while(1):
                    answer = input('Write again into file? Y/N: ')
                    if(answer == 'Y'):
                        file_written = 0
                        break
                    elif(answer == 'N'):
                        break
                    else:
                        print('Enter Valid Response')
                        continue
            if(file_written == 0):
                data = seq_info + '\n' + code_seq + '\n' + amino_seq + '\n\n'
                file_write.addToFile(data)
                file_written = 1
        elif(response == 3):
            if(database_written == 1):
                while(1):
                    answer = input('Write again into database? Y/N: ')
                    if(answer == 'Y'):
                        database_written = 0
                        break
                    elif(answer == 'N'):
                        break
                    else:
                        print('Enter Valid Response')
                        continue
            if(database_written == 0):
                database.doc_count += 1
                data = {'Sl No': database.doc_count, 'Seq Info': seq_info, 'Code Seq': code_seq, 'Length Code Seq': len(code_seq), 'Amino Seq': amino_seq, 'Length Amino Seq': len(amino_seq)}
                database.dBInsertOne(data)
                database_written = 1
        elif(response == 4):
            plotAminoPercentage(amino_seq)
        elif(response == 5):
            plotATGCSkew(code_seq)
        else:
            break
    return

