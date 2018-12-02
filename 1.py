from website.models import save_tweets, Tweet, mostdone, UserInfo

"""
([{"id":"0","place":"一食堂","option":["吃喜欢吃的饭","吃不喜欢吃的饭","自习（壮士！）"]},
              {"id":"1","place":"二食堂","option":["吃喜欢吃的饭","吃不喜欢吃的饭","自习（壮士！）"]},
              {"id":"2","place":"信操","option":["上体育课","心情烦闷，仅仅想走走","跑汉姆","看美女（帅哥）",
                                               "思考人生和哲学(ass we do)","和男（女）票一起玩耍","社团活动","球队训练",
                                               "做球场陈独秀","默默提升球技","踢着玩",]},
              {"id":"3","place":"信部篮球场","option":["心情烦闷，仅仅想走走","看美女（帅哥）",
                                               "思考人生和哲学(ass we do)","和男（女）票一起玩耍","社团活动","球队训练",
                                               "做球场陈独秀","默默提升球技","打着玩"]},
              {"id":"4","place":"网安操场","option":["上体育课","心情烦闷，仅仅想走走","跑汉姆","看美女（帅哥）",
                                               "思考人生和哲学(ass we do)","和男（女）票一起玩耍","社团活动","球队训练",
                                               "做球场陈独秀","默默提升球技","踢着玩",]},
              {"id":"5","place":"网安教学楼","option":["上喜欢的课","上不喜欢的课","上课玩手机","听讲座","开会"]},
              {"id":"6","place":"青楼","option":["上喜欢的课","上不喜欢的课","上课玩手机","听讲座","开会"]},
              {"id":"7","place":"德仁广场","option":["心情烦闷仅仅走走","和男（女）票一起玩耍","赶路",]},
              {"id":"8","place":"星湖园","option":["吃喜欢吃的饭","吃不喜欢吃的饭","自习（壮士！）"]},
              {"id":"9","place":"图书馆","option":["自习","读书","划水",]},
              {"id":"10","place":"星湖","option":["赏景","思考人生和哲学（ass we do）","心情不好",]},
              {"id":"11","place":"友谊广场","option":["心情烦闷仅仅走走","和男（女）票一起玩耍","赶路",]},
              {"id":"12","place":"游泳池","option":["游泳","和男（女）票一起玩耍","期待游泳",]}])'''
time 6:00--8:00--11:00--14:00--17:00--19:00--21:00--23:00

e.g.  Tweet.objects.create(username="wang", date="2018-11-DD", time="", place="", thing="", thought="")
"""

Tweet.objects.create(username="David", date="2018-11-01", time="19:00--21:00", place="图书馆", thing="自习", thought="学习使我快乐啊")
Tweet.objects.create(username="David", date="2018-11-01", time="21:00--23:00", place="星湖", thing="思考人生和哲学(ass we do)", thought="所以我们是老乡")
Tweet.objects.create(username="David", date="2018-11-29", time="6:00--8:00", place="信部篮球场", thing="做球场陈独秀", thought="骚！")
Tweet.objects.create(username="David", date="2018-11-29", time="8:00--11:00", place="青楼", thing="上喜欢的课", thought=".")
Tweet.objects.create(username="David", date="2018-11-29", time="11:00--14:00", place="星湖园", thing="自习（壮士！）", thought="学习使我超快乐")
Tweet.objects.create(username="David", date="2018-11-05", time="14:00--17:00", place="图书馆", thing="自习", thought="『划水也不错的』")
Tweet.objects.create(username="David", date="2018-11-05", time="11:00--14:00", place="星湖园", thing="吃不喜欢吃的饭", thought="我要学习！")
Tweet.objects.create(username="David", date="2018-11-05", time="19:00--23:00", place="图书馆", thing="划水", thought="『那么就划水好了』")
Tweet.objects.create(username="David", date="2018-11-06", time="6:00--8:00", place="二食堂", thing="吃喜欢吃的饭", thought="今天也是好天气")
Tweet.objects.create(username="David", date="2018-11-06", time="8:00--23:00", place="图书馆", thing="划水", thought="『今天也是一如既往地划水呢』")
Tweet.objects.create(username="David", date="2018-11-11", time="8:00--23:00", place="德仁广场", thing="心情烦闷仅仅走走", thought="『剁手快乐』")
Tweet.objects.create(username="David", date="2018-11-29", time="19:00--21:00", place="信操", thing="思考人生和哲学(ass we do)", thought="汉姆可能跑不完了")
Tweet.objects.create(username="David", date="2018-11-13", time="19:00--21:00", place="信操", thing="跑汉姆", thought="完了")
