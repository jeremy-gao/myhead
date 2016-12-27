#!/usr/bin/env python
#-*-coding:utf-8-*-

from bottle import Bottle, run, route ,view, static_file, request
from EasticModule.Elastic import Elastic
import ConfigParser

# myhead=Bottle();
cf = ConfigParser.ConfigParser()
cf.read('config.conf')
httpurl = cf.get('url', 'elasticsearch.url')


urlhealth = httpurl + cf.get('api', 'urlhealth')
urllistnode = httpurl + cf.get('api', 'urllistnode')
urlallocate = httpurl + cf.get('api','urlallocate')
indicesurl = httpurl + cf.get('api','indicesurl')
url = 'curl -s ' + '"' + httpurl + cf.get('api', 'indexsizeurl') + '"'
cmd = '|sort -rnk4|head -n ' + cf.get('limit', 'limit')

@route('/assets/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./assets/')

elastic = Elastic()
def status(url):
    state = elastic.health(url)
    return state

def listnodes(url):
    listnode = elastic.nodelist(url)
    return listnode

def allocates(url):
    allocate = elastic.allocation(url)
    return allocate

def indice(url,cmd):
    indices = elastic.indexsize(url, cmd)
    return indices

def indiceslist(url):
    indlist = elastic.allindex(url)
    return indlist

def indexmapping(url):
    indexmaps = elastic.indextypes(url)
    return indexmaps
def delindex(url):
    sigjson = elastic.delindex(url)
    return sigjson


@route('/')
@view('index')
def index():
    state = status(urlhealth)
    listnode = listnodes(urllistnode)
    allocate = allocates(urlallocate)
    indices = indice(url, cmd)
    return dict(state=state,listnode=listnode,allocate=allocate,signal=indices[0],indices=indices[1])

@route('/list.html')
@route('/list.html',method='POST')
@view('list')
def indexlist():
    if request.forms.get('indexname'):
        indexname = request.forms.get('indexname')
        delurl = httpurl + indexname
#         print delurl.rstrip(',')
        delindex(delurl.rstrip(','))
    state = status(urlhealth)
    listnode = listnodes(urllistnode)
    indices = indiceslist(indicesurl)
    return dict(state=state,listnode=listnode,indices=indices)

@route('/info.html')
@view('info')
def indexinfo():
    indexname = request.query.get('indexname')
    mapurl = httpurl + indexname + "/_mappings"
    indexmaps = indexmapping(mapurl)
    return dict(indexmaps=indexmaps)

@route('/stats.html')
@view('stats')
def indexstats():
    indexname = request.query.get('indexname')
    staurl = httpurl + indexname + "/_stats"
    indexstat = indexmapping(staurl)
    return dict(indexstat=indexstat)

# run()



