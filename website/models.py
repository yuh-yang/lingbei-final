from django.db import models
from collections import Counter
# Create your models here.

class Tweet(models.Model):
    username = models.TextField()
    date = models.TextField()
    time = models.TextField()
    place = models.TextField()
    thing = models.TextField()
    thought = models.TextField()

    def __str__(self):
        return self.username, self.date, self.time, self.place,self.thing,self.thought

def save_tweets(un,dt,tm,pl,th, tho): #存储一条发布
    Tweet.objects.create(username=un, date=dt, time=tm, place=pl, thing=th, thought=tho)

#以下为决赛要加入功能
'''
def contrast(user1, user2):
    import jieba
    from gensim import corpora, models, similarities
    #比较相似性
    '''    '''按A过去七天的行为，排出各个时间段最常做事+地点前四名。外层按时间段排，内层按常见度排，输入到一个列表 list1 = []
    对B同样，得到list2 = []
   对两个列表进行文本相似度分析。''''''
    text1 = []
    text2 = []
    # 1、将【文本1】生成【分词列表】
    texts1 = [jieba.cut(text1) for text in text1]
    # 2、基于文本集建立【词典】，并提取词典特征数
    dictionary = corpora.Dictionary(texts1)
    feature_cnt = len(dictionary.token2id.keys())
    # 3、基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】
    corpus = [dictionary.doc2bow(text) for text in texts1]
    # 4、使用【TF-IDF模型】处理语料库
    tfidf = models.TfidfModel(corpus)
    # 5、同理，用【词典】把【搜索词】也转换为【稀疏向量】
    kw_vector = dictionary.doc2bow(jieba.cut(text2))
    # 6、对【稀疏向量集】建立【索引】
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    # 7、相似度计算
    sim = index[tfidf[kw_vector]]
    sim1 = int(sim*100)
    return sim + "%"
'''


def mostdone(current_user):
    logs = Tweet.objects.filter(username=current_user).order_by('time')
    timebox = (["6:00--8:00", "8:00--11:00", "11:00--14:00", "14:00--17:00", "17:00--19:00", "19:00--21:00",
                "21:00--23:00"])
    result_time_thing = {}  #时间--事情结果字典
    result_place_thing = {} #地点--事情结果字典
    result = [] #存两个字典
    for s in range(len(timebox)): #遍历每个时间段
        things = []
        for j in logs.filter(time=timebox[s]): #遍历当前时间段的每件事
            things.append(j.thing)
        things_counts = Counter(things)
        result_time_thing[timebox[s]] = things_counts.most_common(1)[0][0]
    thingsv = result_time_thing.values()
    things_list = []
    for i in thingsv:
        things_list.append(i)
    for k in things_list: #遍历每个最常做事件
        places = []
        for r in logs.filter(thing=k):  #按最常做事搜索地点，然后遍历地点
            places.append(r.place)
        places_counts = Counter(places)
        try:
            result_place_thing[k] = places_counts.most_common(1)[0][0]
        except:
            continue
    result.append(result_time_thing)
    result.append(result_place_thing)
    return result

