#NOW FOR AVERAGERS
import string
def main():
    file=open("class1.csv","a")#open the csv file : f8
    print(file)
    for line in file:
        split_line_commas=line.split(",")#split line by commas
        name=split_line_commas[0]#gets name from list and stores as a variable 
        score1=split_line_commas[1]
        score2=split_line_commas[2]
        score3=split_line_commas[3]
        total_of_scores=str(score1)+str(score2)+str(score3)#Total of scores for dividing by 3 
        average=(total_of_scores%3)#divide total of 3 scores by 3 to create an average score
        print(total_of_scores)#dev
        print(average)#dev
        name=split_line[4]
        average=split_line[0]
    print(sorted(file))
    for line in file:
        split_line_commas=line.split(",")
        name=split_line_commas[0]
        split_line_commas[4]=""

#if __name__ == '__main__':
main()
