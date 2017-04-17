from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("Ratings")
sc = SparkContext(conf = conf)

lines = sc.textFile("/Users/grace/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
results = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(results.items()))

for k, v in results.items():
    print(k, v)
    
for k, v in sortedResults.items():
    print("%s %i" % (k,v))

#(u'1', 6110)
#(u'3', 27145)
#(u'2', 11370)
#(u'5', 21201)
#(u'4', 34174)
#1 6110
#2 11370
#3 27145
#4 34174
#5 21201
