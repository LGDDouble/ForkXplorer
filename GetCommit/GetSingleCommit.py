
import os
path1=os.path.abspath('.')   # the path of current file
#print(path1)
path2=os.path.abspath('..')  # the Upper path of current file
#print(path2)
import sys
sys.path.append(path2+str('\crawler'))
import crawler_single_commit as crawler_single_commit
sys.path.append(path2+str('\classifier'))
import classifier_predict as classifier_predict
sys.path.append(path2+str('\\')+str('textrank_example'))
import get_summary as get_summary
global test_print
test_print=True

def get_content(commit_url,test_print_input):
    global test_print
    test_print = test_print_input

    author, message, sha, date,parent = crawler_single_commit.crawler(commit_url)

    if (test_print):
        print('Author:' + author)
        print('Message:' + message)
        print(sha, date)

    # classifier
    commit_text = message
    label=''
    commit_label = classifier_predict.predict([commit_text])
    if (test_print):print(commit_label)
    if (commit_label=='1'):label='feature'
    if (commit_label == '2'): label = 'bug'
    if (commit_label == '0'): label = 'contribution'

    # generate the content
    key_sentences = get_summary.get_summary(commit_text, 5,test_print)
    # print (key_sentences)

    temp_sentence = ''
    for item in key_sentences:
        temp_sentence = temp_sentence + str(item)
    content = get_summary.get_summary(temp_sentence, 1,test_print)

    return content,author,parent,label

def getSingleSummary(commit_url,test_print_input):
    # combine the summary
    global test_print
    test_print=test_print_input

    # get the address of commit
    # commit_url = 'https://api.github.com/repos/apache/incubator-mxnet/commits/01cf29d0aaf8af7424fa82d8100cbb967860c712'

    content,author,parent,label=get_content(commit_url,test_print_input)
    summary = author + ' has a '+str(label)+' about ' + str(content)
    if (test_print):print('The final summary is :' + str(summary))
    return summary

