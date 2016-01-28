#NOW FOR AVERAGERS
import string
def main():
    file=open("class1.csv","a")#open the csv file : f8
    print(file)
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
        name=split_line[4]
        average=split_line[0]
    print(sorted(file))
    for line in file:
        split_line_commas=line.split(",")
        name=split_line_commas[4]
        name=split_line_commas[0]

if __name__ == '__main__':
    main()
