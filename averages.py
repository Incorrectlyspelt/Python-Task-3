#NOW FOR AVERAGERS
import string
import csv#f8
def main():
    row_printed=0
    row_count=-1
    alpha_pos=0#set loop counter to zero
    alphabet=list(string.ascii_lowercase) #get lowercase alphabet
    file=open("class1.csv")#open the csv file : f8
   # file=csv.reader(file,delimiter=",")#read the csv file
    print(file)
    file=open("class1.csv","ar")#open the csv file : f8
    for line in file:
        split_line_commas=line.split(",")
        name=split_line_commas[0]
        score1=split_line_commas[1]
        score2=split_line_commas[2]
        score3=split_line_commas[3]
        total_of_scores=str(score1)+str(score2)+str(score3)
        average=(total_of_scores%3)
        print(total_of_scores)
        print(average)
