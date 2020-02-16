import GetSingleCommit as getSingleCommit
import os
path1=os.path.abspath('.')   # the path of current file
#print(path1)
path2=os.path.abspath('..')  # the Upper path of current file
#print(path2)
import sys
sys.path.append(path2+str('\\')+str('textrank_example'))
import get_summary as get_summary


# convert the web address to api address
def commit_url_transform(str):
    tem = str.split('/')
    final = 'https://api.github.com/repos/' + tem[3] + '/' + tem[4] + '/commits/' + tem[6]
    return final

def init_Summary():
    commit_summary_list = []
    fork_summary = ''
    input_1 = ''
    input_2 = ''

    # input the commit address
    print('Input lastest commit url')
    commit_htmurl_lastest = 'https://github.com/typeorm/typeorm/commit/5e004cbcd0fb1d3bdb7f9bb7b98579752cf0bdcf'
    # commit_htmurl_lastest=input()
    input_1=commit_htmurl_lastest
    commit_url_lastest = commit_url_transform(commit_htmurl_lastest)
    # print(commit_url_lastest)

    print('Input Former commit url')
    commit_htmurl_former = 'https://github.com/typeorm/typeorm/commit/b571f5dd69a941b06b59bb1e440ef5b00749138f'
    # commit_htmurl_former=input()
    input_2=commit_htmurl_former
    commit_url_former = commit_url_transform(commit_htmurl_former)
    # print(commit_url_former)

    # begin the first commit
    feature_content = []
    bug_content = []
    contribution_content = []
    temp_url = commit_url_lastest
    n = 1
    while True:
        content, author, parent, label = getSingleCommit.get_content(temp_url, False)
        if (label == 'feature'): feature_content.append(content)
        if (label == 'bug'): bug_content.append(content)
        if (label == 'contribution'): contribution_content.append(content)
        str_1='Commit ' + str(n) + ' : ' + str(getSingleCommit.getSingleSummary(temp_url, False))
        print(str_1)
        commit_summary_list.append(str_1)
        # print('Parent is :'+ str(parent))
        n = n + 1
        if (temp_url == commit_url_former): break
        temp_url = parent

    # the data of feature,bug,contribution
    temp_sentence = ''
    feature_num = 0
    bug_num = 0
    contribution_num = 0

    '''feature'''
    for item in feature_content:
        temp_sentence = temp_sentence + str(item)
        feature_num = feature_num + 1
    if (feature_num > 0):
        feature_content = get_summary.get_summary(temp_sentence, 1, False)
        feature_sentence = str(feature_num) + ' features about ' + str(feature_content)
    else:
        feature_sentence = ''

    '''bug'''
    temp_sentence = ''
    for item in bug_content:
        temp_sentence = temp_sentence + str(item)
        bug_num = bug_num + 1
    if (bug_num > 0):
        bug_content = get_summary.get_summary(temp_sentence, 1, False)
        bug_sentence = str(bug_num) + ' bugs about ' + str(bug_content)
    else:
        bug_sentence = ''

    '''contribution'''
    temp_sentence = ''
    for item in contribution_content:
        temp_sentence = temp_sentence + str(item)
        contribution_num = contribution_num + 1
    if (contribution_num > 0):
        contribution_content = get_summary.get_summary(temp_sentence, 1, False)
        contribution_sentence = str(contribution_num) + ' contributions about ' + str(contribution_content)
    else:
        contribution_sentence = ''

    # generate the fork summary
    str_2='The Commits of Fork which you select contain ' + feature_sentence + bug_sentence + contribution_sentence
    print(str_2)
    fork_summary=str_2

    return input_1,input_2,commit_summary_list,fork_summary
