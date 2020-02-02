from typing import Dict, Any
import webbrowser
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
from flask import jsonify
import json

class splitBotHandler(object):
    META = {
        'name': 'splitbot',
        'description': 'A bot to manage your finances using Zulip chat platform and splitwise API.',
    }

    def usage(self) -> str:
        return '''
        Helps you manage your finances using Zulip chat platform and splitwise API.
        '''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        headers = {
            "Host": "www.splitwise.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cookie": "swdid=IjIwYjhjMjc1LWU3ZDctNDhlZC1iNjJkLTJkNDA5YTE3MTE5YiI%3D--d08ceb75ee8a47413a3ef3252d637bdd4af02560; uvts=52fea51b-fdbe-49c5-6a7d-e063346974fa; __utma=36641634.1133715041.1580549383.1580549383.1580555316.2; __utmz=36641634.1580549383.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=36641634.|1=Signup%20Week=2018-37=1^2=Signup%20Type=registered=1; __gads=ID=939d1eb0569031e2:T=1580549383:S=ALNI_MbzXncMcx3Y5cyaDBtumnXau7rfFw; _ga=GA1.2.1133715041.1580549383; _gid=GA1.2.657783383.1580550450; _splitwise_session=R0JMbXZTREVMMzUwcXRHa0Vua0JDQm92M3pZVzhVYzBlQkJuczRXNGlNaUpvWVFVN2hlanBCdENMb0J2WEh0cm9qZElMUEVvUjdjeFdNWnM2c25RMUVaWHZvMlpkRHRPVGV2Z2dUaWZZRFh3VEovUEJZWVFWb2NZcVlFREZidTVZSTFIK1VzMFBYM0ZRSEpvZWVRRUE0OWMrS3VER3EzTUgzSklWMm52Tlp3MnNEd1llaDRkREpaTTRNRlZ4TG1Nd0hEV0wxb0MzVDY5SGZkeXVnSFR0RlBBbHN0dzU3MFo2WDJWb1F5VXhoNk5wVjUyaFVRVUZXbFJDUmM0TnlZV0VWcGI5aWNEcWNWSnIvK0I1TklpNnJ6WWt5RHU4cmFtVXFGVno4Ykk3dGF4TmpQeERVSWUxSVIwckkzVjBDTVdCSE9mWGJnQjF0RCt4Zi9tdjF1bWh2QklXeXhrR2JNZ0ZyT0VlK3BadVlVa2Q1M0JlTFFWNEdiSlhqc2V1d2swaGZ4b2ZTQUZBaHRIZnorNGs1cXNXdz09LS1VeEY5SFB6OG93OHBsTHJ3Q2RxUzN3PT0%3D--e3ca6f8afffade97a3c46b0e8690f9b0f67b2eca; user_credentials=003307406fbf4cf61ef4b12d6d4181f829d2752ab26fdf0cd0f1ad2e1ba8c3a9bab7fba15bd57af5bf9fe6f2094e4330ae3d72202503bd7933887fa14d021cda%3A%3A17964305%3A%3A2020-05-01T23%3A27%3A12%2B05%3A30",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"
        }

        res = requests.get("https://www.splitwise.com/api/v3.0/get_current_user", headers = headers)
        print(res.status_code)
        if(res.status_code == 200):
            print("Logged In")
            print(message['content'])
            if(message['content'] == "friends"):

                newheader = {
                    # "Host": "localhost:5000",
                    # "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
                    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    # "Accept-Language": "en-US,en;q=0.5",
                    # "Accept-Encoding": "gzip, deflate",
                    # "Connection": "keep-alive",
                    "Cookie": "__stripe_mid=46f91668-48b6-4449-96cb-cf7bcce6a95c; csrftoken=Q1tTftcuQwjqbaPA1xud8b1gev0bIs8d1gpWqtV0osQBgXP0SDrjJCnqy1SimrUb; _tccl_visitor=22317f10-6470-42de-9e31-0ba89483e2cd; sessionid=xfh43mgvcwks0a806mkxgt06nrc1dmpm; session=.eJxNy8EKgjAYAOB32dlDRIl0c2bpCHI2Sb3IsKFN29DfKSK-e12ijt_hWxAvSwFQDLoRCh0WpLkZ6i8RCYymgrrKuHQa6dbGWBhPEq8hAT5BKzszShkpZP3HAkTZi-HzQ8xYlapz9oBGc8EgzLMk2JgYkjpmt1LfSXX1W4pWC_2Sx6Ie8hm6k-MEF-cY7vWEefa0026YcxvLl6E76aP1DWIyQpQ.XjVhVQ.U9bqMTonHa4-vQPMcj1FAu7yO4U",
                    # "Upgrade-Insecure-Requests": "1"
                }
                help_content = requests.get("http://localhost:5000/friends", headers = newheader)
                print(help_content.text)
                output_str = ""
                for x,y  in zip(json.loads(help_content.text)['friends'],json.loads(help_content.text)['balances']):
                    output_str = output_str + x + "\t" + y + "\n"
                    
            elif(message['content'] == "groups"):

                newheader = {
                    # "Host": "localhost:5000",
                    # "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
                    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    # "Accept-Language": "en-US,en;q=0.5",
                    # "Accept-Encoding": "gzip, deflate",
                    # "Connection": "keep-alive",
                    "Cookie": "__stripe_mid=46f91668-48b6-4449-96cb-cf7bcce6a95c; csrftoken=Q1tTftcuQwjqbaPA1xud8b1gev0bIs8d1gpWqtV0osQBgXP0SDrjJCnqy1SimrUb; _tccl_visitor=22317f10-6470-42de-9e31-0ba89483e2cd; sessionid=xfh43mgvcwks0a806mkxgt06nrc1dmpm; session=.eJxNy8EKgjAYAOB32dlDRIl0c2bpCHI2Sb3IsKFN29DfKSK-e12ijt_hWxAvSwFQDLoRCh0WpLkZ6i8RCYymgrrKuHQa6dbGWBhPEq8hAT5BKzszShkpZP3HAkTZi-HzQ8xYlapz9oBGc8EgzLMk2JgYkjpmt1LfSXX1W4pWC_2Sx6Ie8hm6k-MEF-cY7vWEefa0026YcxvLl6E76aP1DWIyQpQ.XjVhVQ.U9bqMTonHa4-vQPMcj1FAu7yO4U",
                    # "Upgrade-Insecure-Requests": "1"
                }
                help_content = requests.get("http://localhost:5000/groups", headers = newheader)
                print(help_content.text)
                output_str = ""
                for x,y in zip(json.loads(help_content.text)['groups'],json.loads(help_content.text)['balances']):
                    output_str = output_str + x + "\t" +str(y) + "\n"
               
            else:
                help_content = requests.get("http://localhost:5000/help", headers = headers)
                output_str = help_content.text
            bot_handler.send_reply(message, output_str)
        else:
            print("Login")

handler_class = splitBotHandler
