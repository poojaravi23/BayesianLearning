"""
Name: Pooja Ravi
ID:   1001578517

"""

import os
import re
import math
import glob

def remove_unwantedData(data_from_file):
   

    data_from_file = data_from_file.lower()             #Lower case all the data and remove digits from the data
    data_from_file = re.sub("\d+", "", data_from_file)          
    data_from_file = data_from_file.replace('\n', ' ')
    removeList = ['<','>','?','.','"',')','(','|','-','_','#','*','+','"','$',"'",'!','/','=',',',':','\\','[',']','~','^','%','&',';']
   
    stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'aint', 'all', 'am', 'an', 'and', 'any', 'are', 'arent',
                 'aren', 'isn', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 
                 'can', 'couldn', 'couldnt', 'could', 'd', 'did', 'didnt', 'didn', 'do', 'does', 'doesnt', 'doesn', 'doing', 
                 'dont', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadnt', 'has', 'hasnt', 'have', 'shan', 
                 'havent', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 
                 'into', 'is', 'isnt', 'it', 'its', 'don', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightnt', 'more', 'most', 
                 'mustnt','must','should','would','could', 'my', 'myself', 'neednt', 'needn' 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 
                 'or', 'other', 'our', 'ours', 'b', 'r', 'w', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shant', 
                 'she', 'should', 'shouldnt', 'so', 'shan', 'hadn', 'hasn', 'haven', 'wouldn', 'also', 'mightn', 'ain', 'wasn',
                 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'weren','n' 
                 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was','et', 'jr',
                 'wasnt', 'we', 'were', 'werent', 'what', 'when', 'where', 'which', 'while', 'who', 'x', 'c', 'whom', 'why','e','v','ak', 
                 'will', 'with', 'won', 'wont', 'wouldnt', 'y', 'you', 'your', 'yours', 'yourself', 'yourselves', 'would', 'gmt','j','l','al','sh',
                 'xref', 'us', 'one', 'two', 'like', 'know', 'lines', 'messageid', 'mustn', 'shouldn','srv','cs','edu','cmu','alt','p','g','th','wed','apr','com','n','co']
    for x in removeList:
        data_from_file = data_from_file.replace(x,' ')
    word_split_cleaned_data = [word for word in data_from_file.split() if word not in stop_words]
    return word_split_cleaned_data 

"""
Calculating the probability of each collected word in every category 
"""

def calculate_probability_perWordPerCatgeory(categories,files_in_category_probability,words_per_category_list):
    probability_of_words_per_category={}  
    for category in categories:
        temp={}
        files_in_category_probability[category]=float(files_in_category_probability[category]/1000.00)
        for word_list in words_per_category_list[category]:
            temp[word_list]=float(words_per_category_list[category][word_list]/total_words_per_category[category])
        probability_of_words_per_category[category]=temp
    return probability_of_words_per_category

def get_Probability_of_wordlist(split_words_list_test,probability_of_words_per_category,category):
    probabilty=1
    for word in split_words_list_test:
        if word in probability_of_words_per_category:
            calcutaled_prob = float(probability_of_words_per_category[word])
            #print(calcutaled_prob,"for word-",word,'|',end="")
            probabilty+=calcutaled_prob
    return probabilty
 
path = '20_newsgroups'
files_in_category_probability={}
news_categories_folder_path = os.listdir(path)

categories=news_categories_folder_path
words_per_category_list={}
total_words_per_category={}
p=0;
for category_folder in news_categories_folder_path :
    per_news_categories_files_path = glob.glob(os.path.join(path, category_folder, '*'))
    bag_of_word={}
    #files_in_category_probability.append((category_folder,500))
    for category_file in per_news_categories_files_path[:500]:
        p=p+1
        file = open(category_file, encoding="utf8", errors='ignore')
        data_from_file =file.read()
        #if(category_file=='49960'):
            
        split_words_list_train=remove_unwantedData(data_from_file)
        
        for word in split_words_list_train:
               # print(bag_of_word.count(word),word)
            if word in bag_of_word:
                    bag_of_word[word]=bag_of_word[word]+1
            else:
                    bag_of_word[word]=1
    files_in_category_probability[category_folder]=p
    p=0

    words_per_category_list[category_folder]=bag_of_word
    total_words_per_category[category_folder]=sum(bag_of_word.values()) #Total number of words per category

probability_of_words_per_category=calculate_probability_perWordPerCatgeory(categories,files_in_category_probability,words_per_category_list)

#print(probability_of_words_per_category)
"""
Testing the model againist the remaining file data
""" 
correct=0
total_file=0
probablity_list={}   
print("File\t|Expected\t|Actual")
for category_folder in categories :
    per_news_categories_files_path = glob.glob(os.path.join(path, category_folder, '*'))
    for category_file in per_news_categories_files_path[500:]:
        total_file=total_file+1
        file = open(category_file, encoding="utf8", errors='ignore')
        data_from_file_test =file.read()
        split_words_list_test=remove_unwantedData(data_from_file_test)
        for category in categories:
            prob_per_category=get_Probability_of_wordlist(split_words_list_test,probability_of_words_per_category[category],category)
                #print("Returned prob for -",category,"= ",prob_per_category)
            probablity_list[category]=math.log2(files_in_category_probability[category])+math.log2(prob_per_category)
       
        key_max = max(probablity_list.keys(), key=(lambda k: probablity_list[k]))
        print(category_file,"\t|",category_folder,"\t|",key_max)
        if(key_max==category_folder):
            correct=correct+1
        
print("\n")
print("Accuracy using Naive Bayes classifier =",(correct/total_file)*100,'%')


            
