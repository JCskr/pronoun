[ParseTree操作若干-Tregex and Stanford CoreNLP](http://www.shuang0420.com/2017/03/24/ParseTree%E6%93%8D%E4%BD%9C%E8%8B%A5%E5%B9%B2-Tregex%20and%20Stanford%20CoreNLP/)<br>https://stanfordnlp.github.io/CoreNLP/corenlp-server.html<br>https://stanfordnlp.github.io/CoreNLP/api.html

1. download the [official java CoreNLP release](https://stanfordnlp.github.io/CoreNLP/#download), unzip it, and define an environment variable `$CORENLP_HOME` that points to the unzipped directory.

2. Other Human Languages Support

   download an additional model file and place it in the `.../stanford-corenlp-full-....-..-..` folder. For example, you should download the `stanford-chinese-corenlp-....-..-..-models.jar` file if you want to process Chinese.

3.  go to the path of the unzipped Stanford CoreNLP and execute the below command:

   `java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt`

   notes:

   Test the file `input.txt`, the output will be in the same path.

4. run the server using the selected annotators:

   ```java
   java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,ner,depparse,dcoref" -port 9000 -timeout 30000
   ```

   ```java
   # Run a server using Chinese properties
   java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -annotators "tokenize,ssplit,pos,lemma,ner,depparse,dcoref" -port 9000 -timeout 15000
   ```

5. sending HTTP request

   tregex:

   ```python
   import requests
   
   url = "http://localhost:9000/tregex"
   request_params = {"pattern": "(NP[$VP]>S)|(NP[$VP]>S\\n)|(NP\\n[$VP]>S)|(NP\\n[$VP]>S\\n)"}
   text = "Pusheen and Smitha walked along the beach."
   r = requests.post(url, data=text, params=request_params)
   print(r.json())
   ```

   output: `{u'sentences': [{u'0': {u'namedNodes': [], u'match': u'(NP (NNP Pusheen)\n  (CC and)\n  (NNP Smitha))\n'}}]}`

   parse:

   ```python
   import requests
   
   url = 'http://localhost:9000/?properties={"annotators": "parse", "outputFormat": "text"}'
   text='Harry Potter, a young boy, is very famous in US'
   r = requests.post(url, data=text)
   print(r.content)
   ```

   output: `...`

   dcoref:

   ```python
   import requests
   
   url = 'http://localhost:9000/?properties={"annotators": "tokenize,ssplit,pos,lemma,ner,depparse,dcoref", "outputFormat": "text"}'
   text='狗蛋他这个人怎么样？'
   r = requests.post(url, data=text.encode('utf-8'))
   print(r.content)
   ```

   output: `java.util.concurrent.ExecutionException: java.lang.IllegalArgumentException: No head rule defined for IP using class edu.stanford.nlp.trees.SemanticHeadFinder in ...` 

   solution:

   https://stanfordnlp.github.io/CoreNLP/coref.html

   https://nlp.stanford.edu/software/dcoref.html

   https://stackoverflow.com/questions/30010340/how-do-i-use-chinese-co-reference-in-stanford-corenlp-3-5-2

   https://github.com/jingyuanz/stanfordnlp_chinese_coreference

6. ..



