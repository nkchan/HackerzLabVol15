# -*- coding: utf-8 -*-
import json
import urllib



def Q12(event, context):
    body = {
        "message": "Your FLAG is HLH = {Leo}",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def Q13(event, context):
    if urllib.parse.parse_qs(event["body"]) == {'id': ['hackerzlab']}:
       body = {"message": "Your FLAG is HLH = {VmlyZ28=}"} 
    else: body = {"message": "Your send param is not correct!"}

    response = {
        "statusCode": 200,
        "body": json.dumps(body,ensure_ascii=False)
    }

    return response

def Q14(event, context):
    if event["body"] is None:
       body = {"message": "please POST in addition to the value id: N"}
    elif urllib.parse.parse_qs(event["body"]) == {'id': ['N']}:
       body = {"message": "please password! passwd is HTTP version that  this connection. for exsample  HTTP/1.0 -> pass: 1.0 You should send value -> id:N, pass: version","input": event}
    elif urllib.parse.parse_qs(event["body"]) == {'id': ['N'],'pass': ['1.1']}:
       body = {"message": "Your FLAG is HLH = {Libra}"}    
    else: body = {"message": "Your send param is not correct!"}

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def Q15(event, context):
    if event["body"] is None:    
       body = {"message": "最後は idが A , passwdを123456 とPOSTしてください"}
    elif urllib.parse.parse_qs(event["body"]) == {'id': ['A'],'passwd': ['123456']}:
       body = {"message": "Your FLAG is HLH = {Scorpius}"}
    else: body = {"message": "Your send param is not correct!"}


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
