from datetime import datetime
from sqlalchemy import create_engine
engine = create_engine('postgresql://yugabyte@localhost:5433/bi_automation')
conn = engine.connect()

def id_generate():
    newimport_id = lambda : str(datetime.now().year)+(str(datetime.now().month).zfill(2))+'01'
    getid = 'select max(import_id) from live_data ;'
    new_id = conn.execute(getid)
    for val in new_id:
        new_id = str(val[0])
        if ((new_id[4:6]) == str(datetime.now().month).zfill(2)):
            new_id= int(new_id)+1
        else:
            new_id = newimport_id()
        return new_id



print(id_generate())    


'''
    webhook = 'https://hooks.slack.com/services/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'
    if msgvalues[0]=='success':       
        message=f'**** Report from {date.today()} **** \n\t\tStatus = Success\n\t\tStatus time = {datetime.now()} \n\t\tImportid = {msgvalues[1]}'
        message = {'text':message}
        data =json.dumps(message)
        r= requests.post(webhook,data= data)
        print(r)
    else:
        message=f'**** Report from {date.today()} **** \n\tStatus = Error \n\tStatus time = {datetime.now()}'
        message = {'text':message,'color':'good'}
        data =json.dumps(message)
        r= requests.post(webhook,data= data)
        print(r)
        from slacker import Slacker
from datetime import datetime
import json
slack = Slacker('xoxb-1192530816000-1168703019634-iptS86XpQZ5l9ecHJ3jqKoe8')
message = f'The dataload from this {datetime.now()} is success\n '
slack.chat.post_message('#learning',message)
'''