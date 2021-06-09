from  flask import  Flask
from hostinfo import get_hostinfo
from cpuinfo import get_cpuinfo
from meminfo import get_meminfo
from diskinfo import get_diskinfo
from  flask import  render_template
from flask_cors import CORS
# from flask_cache import Cache
from flask_caching import Cache

app  =  Flask(__name__)
cache = Cache()

config = {
'CACHE_TYPE': 'RedisCache',
'CACHE_KEY_PREFIX': 'data',
'CACHE_REDIS_HOST': '192.168.2.30',
'CACHE_REDIS_PORT': 6379,
'CACHE_REDIS_DB': '1',
'CACHE_REDIS_PASSWORD': 'sensetime'
}
  
app.config.from_object(config)
cache.init_app(app,config)

CORS(app, resources=r'/*')

@app.route('/hello')

@app.route('/hello/<name>')



def  hello(name=None):

    return  render_template('hello.html',  name=name)
# 获取主机信息
@app.route('/hostinfo',methods=['POST', 'GET'])
@cache.cached(timeout=60*2)
def get_host():
    
    return get_hostinfo()

# 获取CPU5分钟平局占用
@app.route('/cpuinfo',methods=['POST', 'GET'])
@cache.cached(timeout=60*2)
def get_cpu():
    
    return get_cpuinfo()

# 获取当前内存利用率
@app.route('/meminfo',methods=['POST', 'GET'])
@cache.cached(timeout=60*2)
def get_mem():
    
    return get_meminfo()

# 获取当前磁盘利用率
@app.route('/diskinfo',methods=['POST', 'GET'])
@cache.cached(timeout=60*5)
def get_disk():
    
    return get_diskinfo()



if  __name__  ==  '__main__':

    app.run(host='0.0.0.0',  debug=True)