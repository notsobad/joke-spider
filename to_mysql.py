#coding=utf-8
import sys,os
import json
import codecs
import traceback

import sys
import time
import socket
import hashlib

reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append('/home/notsobad/myapp/ishuoxiao')
from ui import Jokes,db


name = sys.argv[1]
print sys.getdefaultencoding()
with codecs.open(name, 'r', 'utf-8') as f:
	for line in f:
		m = hashlib.md5()
		item = json.loads(line)
		print "####", item['cont'].encode('utf-8'), "###"
		cont_s = item['cont'].encode('utf-8')
		if 'url' in item:
			del item['url']
		source = os.path.basename(name).split('.')[0]
		item['source'] = source
		item['cont'] = unicode(item['cont']).strip()
		if not item['cont']:
			continue
		
		if 'score' in item:
			del item['score']

		if 'tags' in item:
			item['tags'] = ','.join(item['tags'])
		else:
			item['tags'] = ''

		m.update(cont_s)
		md5 = m.hexdigest()
		item['md5'] = unicode(md5)
		#db.jokes.update({'md5':md5}, {'$set':item}, upsert=True)

		joke = Jokes(**item)
		db.session.add(joke)
		try:
			db.session.commit()
		except:
			traceback.print_exc()
			db.session.rollback()

	db.session.commit()
