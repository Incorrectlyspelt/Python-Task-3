#NOW FOR AVERAGERS
def main():
    file=open("class1.csv")#open the csv file : f8
    for line in file:
        split_line_commas=line.split(",")
        name=split_line_commas[0]
        score1=split_line_commas[1]#get scores
        score2=split_line_commas[2]
        score3=split_line_commas[3]
        remove_line_ender=score3.split(" ")
        score3=remove_line_ender[0:1]
        total_of_scores=str(score1)+str(score2)+str(score3)
        average=(total_of_scores%3)
        print(total_of_scores)
        listed_score=list(score3)
        score3=listed_score[0]
        total_of_scores=int(score1)+int(score2)+int(score3)#Total of scores for dividing by 3
        average=total_of_scores/3
        print(average)
        line=format(score1,score2,score3,name)
        print(line)
        file.write(format(score1,score2,score3,name))#rewrite the line in the new formatted way
    print(sorted(file))
##
##    print(sorted(file))
##    for line in file:
##        split_line_commas=line.split(",")#split by commas
##        score1=split_line_commas[1]#get scores
##        score2=split_line_commas[2]
##        score3=split_line_commas[3]
##        name=split_line_commas[4]#get name
##        blank=split_line_commas[4]=""#clear column 4
##        file.write[name,score1,score2,score3,blank]



#if __name__ == '__main__':
main()
