from email import header
from flask import Flask, redirect, render_template, request
import requests as r
import random
import time


app = Flask(
    __name__,
    template_folder='templates',
    )

def sign(url, token):
    headers = {
    'authority': 'api.classplusapp.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'api-version': '23',
    'origin': 'https://web.classplusapp.com',
    'referer': 'https://web.classplusapp.com/',
    'region': 'IN',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-access-token': token,
    }

    params = {
        'url': url,
    }
    req_url = f"https://api.classplusapp.com/cams/uploader/video/jw-signed-url"
    res = r.get(req_url, params=params, headers=headers).json()['url']
    vod_url = f"https://vod.saumay.dev/player/#{res}"
    return vod_url

def live_class(batchid, token):
    headers = {
    'authority': 'api.classplusapp.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'api-version': '23',
    'origin': 'https://web.classplusapp.com',
    'referer': 'https://web.classplusapp.com/',
    'region': 'IN',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-access-token': token,
    }

    params = {
        'type': '3',
        'entityId': batchid,
        'limit': '50',
        'offset': '0',
    }
    res = r.get('https://api.classplusapp.com/v2/live/classes/list/videos', params=params, headers=headers).json()['data']
    total_videos = str(res['totalCount'])
    videos = res['list']
    sec = 0
    for v in videos:
        duration = v['duration']
        l = duration.split(':')
        sec += int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
    tt = time.strftime('%H:%M:%S', time.gmtime(sec))
    return total_videos, videos, tt

def get_batches(token):

    headers = {
        'authority': 'api.classplusapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'origin': 'https://web.classplusapp.com',
        'referer': 'https://web.classplusapp.com/',
        'region': 'IN',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-access-token': token,
    }

    params = {
        'limit': '50',
        'offset': '0',
        'sortBy': 'createdAt',
    }

    res = r.get('https://api.classplusapp.com/v2/batches/details', params=params, headers=headers).json()['data']
    total_batches = str(res['batchesCount'])
    names = res['totalBatches']

    return total_batches, names

def get_maerial(token):

    headers = {
        'authority': 'api.classplusapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://web.classplusapp.com',
        'referer': 'https://web.classplusapp.com/',
        'region': 'IN',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-access-token': token,
    }

    json_data = {
        'batchFreeResource': 1,
        'batchId': '304146',
        'limit': 30,
        'offset': 0,
        'sortBy': 'createdAt',
    }

    res = r.post('https://api.classplusapp.com/v2/folder', headers=headers, json=json_data).json()['data']
    folders = res['folders']
    atts = res['attachments']
    return folders, atts

def get_folder(id, token):

    headers = {
        'authority': 'api.classplusapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://web.classplusapp.com',
        'referer': 'https://web.classplusapp.com/',
        'region': 'IN',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-access-token': token,
    }

    json_data = {
        'batchFreeResource': 1,
        'batchId': '304146',
        'limit': 30,
        'offset': 0,
        'sortBy': 'createdAt',
        'folderId': id,
    }

    res = r.post(f'https://api.classplusapp.com/v2/folder/{id}', headers=headers, json=json_data).json()['data']
    folders = res['folders']
    atts = res['attachments']
    return folders, atts

@app.route("/")
def hello_world():
    return "<p>sup!🫦 🫦</p>"

@app.route('/videos')
def videos():
    bid = str(request.args.get('batchid'))
    token = str(request.args.get('token'))
    total_videos, videos, tt = live_class(bid, token)
    return render_template('videos.html', total_videos=total_videos, videos=videos[::-1], token=token, tt=tt)

@app.route('/vod')
def vod():
    token = str(request.args.get('token'))
    url = str(request.args.get('url'))
    vod_url = sign(url, token)
    return redirect(vod_url)

@app.route('/batches')
def batches():
    token = str(request.args.get('token'))
    total_batches, names = get_batches(token)
    return render_template('batches.html', total_batches=total_batches, names=names, token=token)

@app.route('/material')
def material():
    token = str(request.args.get('token'))
    folders, atts = get_maerial(token)
    return render_template('material.html', folders=folders, atts=atts, token=token)

@app.route('/folder')
def folder():
    id = str(request.args.get('folderid'))
    token = str(request.args.get('token'))
    folders, atts = get_folder(id, token)
    return render_template('material.html', folders=folders, atts=atts, token=token)

if __name__ == "__main__":
    # app.debug = True
    app.run(host="0.0.0.0",port= 5000)