from flask import Flask, render_template, request
import requests as r
import random

token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDg2NjI2MTEsIm9yZ0lkIjo0MzkyLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTYyNjQ3NDIzMzQiLCJuYW1lIjoiU2F1bWF5IEx1bmF3YXQiLCJlbWFpbCI6Im1haWxAc2F1bWF5LmRldiIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiZW4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5IjpmYWxzZSwiaWF0IjoxNjU3NjUyOTM3LCJleHAiOjE2NTgyNTc3Mzd9.oV_DGDxaHZ5rQZWdNUDv-unLqUu3tuGOehbsYyjVk_XOM-7klOuAVb2S9wbsozza"

app = Flask(
    __name__,
    template_folder='templates',
    )

def live_class(batchid):
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
    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDg2NjI2MTEsIm9yZ0lkIjo0MzkyLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTYyNjQ3NDIzMzQiLCJuYW1lIjoiU2F1bWF5IEx1bmF3YXQiLCJlbWFpbCI6Im1haWxAc2F1bWF5LmRldiIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiZW4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5IjpmYWxzZSwiaWF0IjoxNjU3NjUyOTM3LCJleHAiOjE2NTgyNTc3Mzd9.oV_DGDxaHZ5rQZWdNUDv-unLqUu3tuGOehbsYyjVk_XOM-7klOuAVb2S9wbsozza',
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
    return total_videos, videos

@app.route("/")
def hello_world():
    return "<p>sup!🫦 🫦</p>"

@app.route('/videos')
def videos():
    bid = str(request.args.get('batchid'))
    total_videos, videos = live_class(bid)
    return render_template('videos.html', total_videos=total_videos, videos=videos[::-1])
    # return render_template('videos.html')

if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0",port= 5000)