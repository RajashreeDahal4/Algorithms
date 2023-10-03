'''
Date: October 2, 2023
Name: Rajashree Dahal
Problem:
You are given a DNA sequence consisting of the letters A, C, G, T. Your goal is
to write a program to find the longest chain of the same letter in this sequence.
The program should take its input from a single line and output the length of
the longest single character repetition and the start position and end position
of this repetition.
Note:: In case of more than two longest chain of same letter in the sequence, the program
considers any longest chain of sequence when moving from left to right.

'''

def longest_chain(sequence):
    max_len=0
    start_position,end_position=0,0
    each_len=1  #keeps track of each sequence of same letters
    counter=0  #This is used to track the start position of the sequence with maximum length lateron
    for i in range(len(sequence)):
        if (i+1)<len(sequence) and sequence[i]==sequence[i+1]:
            counter=counter+1
            each_len=each_len+1
        elif max_len<=each_len:
            max_len=each_len
            end_position=i+1
            start_position=end_position-counter
            counter=0
            letter=sequence[i]
            each_len=1
        else:
            each_len=1
            counter=0
            continue
    print("Output:")
    print(sequence)
    print(max_len)
    print(start_position)
    print(end_position)

longest_chain('TTTAAAGGGGGGGGGG')
            
