#Sort by highest score
def main():
    file=open("class1.csv")
    for line in file:
        split_line_commas=line.split(",")#split line by commas
        name=split_line_commas[0]#gets name from list and stores as a variable
        score1=split_line_commas[1]
        score2=split_line_commas[2]
        score3=split_line_commas[3]
        if score1 < score2 and score3:
            hs=score1
        if score2 < score1 and score3:
            hs=score1
        if score3 < score2 and score1:
            hs=score1
if __name__ == '__main__':
    main()

#open file
#each line, workout the highest score
#write to file with hs at front