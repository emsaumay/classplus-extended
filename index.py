from email import header
from flask import Flask, redirect, render_template, request
import requests as r
from dotenv import load_dotenv
import time, os
from flask_cors import CORS


load_dotenv()

app = Flask(
    __name__,
    template_folder='templates',
    )
CORS(app, resources={r"*": {"origins": "*"}})

def sign(url, token):
    headers = {
    'authority': os.environ.get('AUTHORITY'),
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'api-version': '23',
    'origin': os.environ.get("WEB"),
    'referer': os.environ.get("WEB"),
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
    req_url = os.environ.get('JW_SIGNED_URL')
    res = r.get(req_url, params=params, headers=headers).json()['url']
    vod_url = f"https://vod.saumay.dev/player/#{res}"
    return vod_url

def live_class(batchid, token):
    headers = {
    'authority': os.environ.get('AUTHORITY'),
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'api-version': '23',
    'origin': os.environ.get("WEB"),
    'referer': os.environ.get("WEB"),
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
    res = r.get(os.environ.get('LIVE_VIDEOS'), params=params, headers=headers).json()['data']
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
        'authority': os.environ.get("AUTHORITY"),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'origin': os.environ.get("WEB"),
        'referer': os.environ.get("WEB"),
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

    res = r.get(os.environ.get("BATCHES"), params=params, headers=headers).json()['data']
    total_batches = str(res['batchesCount'])
    names = res['totalBatches']

    return total_batches, names

def get_material(token):

    headers = {
        'authority': os.environ.get("AUTHORITY"),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'content-type': 'application/json;charset=UTF-8',
        'origin': os.environ.get("WEB"),
        'referer': os.environ.get("WEB"),
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

    res = r.post(os.environ.get('FOLDER'), headers=headers, json=json_data).json()['data']
    folders = res['folders']
    atts = res['attachments']
    return folders, atts

def get_folder(id, token):

    headers = {
        'authority': os.environ.get("AUTHORITY"),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'content-type': 'application/json;charset=UTF-8',
        'origin': os.environ.get("WEB"),
        'referer': os.environ.get("WEB"),
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

    res = r.post(f"{os.environ.get('FOLDER')}/{id}", headers=headers, json=json_data).json()['data']
    folders = res['folders']
    atts = res['attachments']
    return folders, atts

def get_report(token):

    headers = {
        'authority': os.environ.get("AUTHORITY"),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'origin': os.environ.get("WEB"),
        'referer': os.environ.get("WEB"),
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

    y2022 = r.get(f"{os.environ.get('REPORT')}ts2sw6st", headers=headers).json()['data']
    y2023 = r.get(f"{os.environ.get('REPORT')}ts2jdlqm", headers=headers).json()['data']
    y2024 = r.get(f"{os.environ.get('REPORT')}ts23qlno", headers=headers).json()['data']

    return y2022, y2023, y2024

def get_test(id, token):
    
    web_headers = {
        'authority': os.environ.get("AUTHORITY"),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'api-version': '23',
        'origin': os.environ.get("WEB"),
        'referer': os.environ.get("WEB"),
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
    web = r.get(f'{os.environ.get("TEST")}/{id}/stats', headers=web_headers).json()['data']
    solurl = web['solutionUrl']
    cmstoken = (solurl.split('token='))[1].split('&testId=')[0]
    studentTestId = (solurl.split('studentTestId='))[1].split('&defaultLanguage=en')[0]
    testId = (solurl.split('testId='))[1].split('&studentTestId=')[0]

    cms_headers = {
    'authority': os.environ.get("AUTHORITY_CMS"),
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en',
    'origin': os.environ.get("STUDENT_CMS"),
    'referer': os.environ.get("STUDENT_CMS"),
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-cms-access-token': cmstoken,
}
    cms = r.get(f'{os.environ.get("TEST_EVALUATE")}{studentTestId}', headers=cms_headers).json()['data']
    return cms, cmstoken, studentTestId, testId, solurl

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
    folders, atts = get_material(token)
    return render_template('material.html', folders=folders, atts=atts, token=token)

@app.route('/folder')
def folder():
    id = str(request.args.get('folderid'))
    token = str(request.args.get('token'))
    folders, atts = get_folder(id, token)
    return render_template('material.html', folders=folders, atts=atts, token=token)

@app.route('/report')
def report():
    token = str(request.args.get('token'))
    y2022, y2023, y2024 = get_report(token)
    # y2022 = get_report(token)
    return render_template('reports.html', token=token, y2022=y2022, y2023=y2023, y2024=y2024)

@app.route('/test')
def test():
    id = str(request.args.get('testid'))
    token = str(request.args.get('token'))
    cms, cmstoken, studentTestId, testId, solurl = get_test(id, token)
    return render_template('test.html', solurl=solurl, cms=cms, token=token, cmstoken=cmstoken, studentTestId=studentTestId, testId=testId)

@app.route('/solution')
def solution():
    testId = str(request.args.get('testid'))
    studentTestId = str(request.args.get('studenttestid'))
    cmstoken = str(request.args.get('cmstoken'))
    print(testId, studentTestId, cmstoken)
    cms_headers = {
        'authority': os.environ.get("AUTHORITY_CMS"),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en',
        'origin': os.environ.get("STUDENT_CMS"),
        'referer': os.environ.get("STUDENT_CMS"),
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-cms-access-token': cmstoken,
    }

    sol = r.get(f'{os.environ.get("SOLUTION_URL")}/{testId}/student/{studentTestId}/solutions?section=true', headers=cms_headers).json()['data']

    html = """<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.5.3/jspdf.min.js"></script> 
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.3/html2pdf.bundle.min.js"></script>\n"""
    html+= """<button type="button" onclick="questionspdf()" class="btn-sm btn-danger pull-right">Download Questions</button>
            <button type="button" onclick="answerspdf()" class="btn-sm btn-danger pull-right">Download Answers</button>
            <button type="button" onclick="qapdf()" class="btn-sm btn-danger pull-right">Download Questions&Answers</button>\n"""
    html += "<h2>Questions:</h2>\n<div id='paper'><div id='questions'>\n"
    for qa in sol['sections'][0]['questions']:
        html += f"""<span style="font-size: 15pt;"> <strong>Question - {qa['questionSubmitOrder']}</strong>""" + qa['name'] + "<hr>\n"
    html += "</div> <div id='answers'>\n<h2>Answers:</h2>\n"
    for qa in sol['sections'][0]['questions']:
        html += f"""<span style="font-size: 15pt;"> <strong>Solution - {qa['questionSubmitOrder']}</strong>""" + qa['solution'] + "<hr>\n"
    html += "</div></div><br>\n"
    html+="""
    <script type="text/javascript">
  function questionspdf() {
        var element = document.getElementById('questions');
        var opt = {
            margin:       0.25,
            filename:     'questions.pdf',
            image:        { type: 'jpeg', quality: 1 },
            html2canvas:  { scale: 1, useCORS: true },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
          };
        html2pdf().set(opt).from(element).save();
      }
</script>
<script type="text/javascript">
  function answerspdf() {
        var element = document.getElementById('answers');
        var opt = {
            margin:       0.25,
            filename:     'answers.pdf',
            image:        { type: 'jpeg', quality: 1 },
            html2canvas:  { scale: 1, useCORS: true },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
          };
        
        html2pdf().set(opt).from(element).save();
      }
</script>
<script type="text/javascript">
  function qapdf() {
        var element = document.getElementById('paper');
        var opt = {
            margin:       0.25,
            filename:     'qa.pdf',
            image:        { type: 'jpeg', quality: 1 },
            html2canvas:  { scale: 1, useCORS: true },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
          };
        html2pdf().set(opt).from(element).save();
      }
</script>"""
    return html

if __name__ == "__main__":
    # app.debug = True
    app.run(host="0.0.0.0",port= 5000)