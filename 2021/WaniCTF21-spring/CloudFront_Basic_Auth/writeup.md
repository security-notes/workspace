# Writeup

https://cf-basic.web.wanictf.org/admin にアクセスすると、ログインが求められる。ユーザー名とパスワードがわからないので認証できない。

![](img/2021-05-01-14-36-37.png)

与えられたyamlファイルには以下のコメントがある。

```yaml
# "https://${APIID}.execute-api.${AWS::Region}.amazonaws.com/Prod/admin"にGETするとAdminFunctionが動く

# "${CloudFrontDomainName}/admin"に対する通信は"https://${APIID}.execute-api.${AWS::Region}.amazonaws.com/Prod/admin"の結果を利用
```

そのため、`https://${APIID}.execute-api.${AWS::Region}.amazonaws.com/Prod/admin`にGETすることを考えてみる。

前問の[exception](../exception)のときのエラーメッセージを見ると、`${APIID}`と`${AWS::Region}`はそれぞれ`boakqtdih8`,`us-east-1`だということがわかる。

```
{"error_message": ["TypeError: string indices must be integers\n"], "event": {"resource": "/hello", "path": "/hello", "httpMethod": "POST", "headers": {"content-type": "application/json", "Host": "boakqtdih8.execute-api.us-east-1.amazonaws.com", "User-Agent": "Amazon CloudFront", "Via": "2.0 34ad510a1c85545ff0b453b9545fda56.cloudfront.net (CloudFront)", "X-Amz-Cf-Id": "NQQg3PDLCMW8oc85BoCuI43Xyua8pSgmjYNSWHpTGbRcyDEBZ_54gw==", "X-Amzn-Trace-Id": "Root=1-608ce674-45038d900f532f6433ee0b0e", "X-Forwarded-For": "60.110.91.2, 130.176.158.67", "X-Forwarded-Port": "443", "X-Forwarded-Proto": "https"}, "multiValueHeaders": {"content-type": ["application/json"], "Host": ["boakqtdih8.execute-api.us-east-1.amazonaws.com"], "User-Agent": ["Amazon CloudFront"], "Via": ["2.0 34ad510a1c85545ff0b453b9545fda56.cloudfront.net (CloudFront)"], "X-Amz-Cf-Id": ["NQQg3PDLCMW8oc85BoCuI43Xyua8pSgmjYNSWHpTGbRcyDEBZ_54gw=="], "X-Amzn-Trace-Id": ["Root=1-608ce674-45038d900f532f6433ee0b0e"], "X-Forwarded-For": ["60.110.91.2, 130.176.158.67"], "X-Forwarded-Port": ["443"], "X-Forwarded-Proto": ["https"]}, "queryStringParameters": null, "multiValueQueryStringParameters": null, "pathParameters": null, "stageVariables": null, "requestContext": {"resourcePath": "/hello", "httpMethod": "POST", "extendedRequestId": "eojyMG5foAMFZFA=", "requestTime": "01/May/2021:05:26:12 +0000", "path": "/Prod/hello", "protocol": "HTTP/1.1", "stage": "Prod", "domainPrefix": "boakqtdih8", "requestTimeEpoch": 1619846772396, "requestId": "36c956fc-25a9-4a0b-9317-f8fb15db267e", "identity": {"cognitoIdentityPoolId": null, "accountId": null, "cognitoIdentityId": null, "caller": null, "sourceIp": "60.110.91.2", "principalOrgId": null, "accessKey": null, "cognitoAuthenticationType": null, "cognitoAuthenticationProvider": null, "userArn": null, "userAgent": "Amazon CloudFront", "user": null}, "domainName": "boakqtdih8.execute-api.us-east-1.amazonaws.com", "apiId": "boakqtdih8"}, "body": "\"name\"", "isBase64Encoded": false}, "flag": "FLAG{b4d_excep7ion_handl1ng}"}
```

curlコマンドでGETしたところ、フラグが得られた。

```bash
$ curl https://boakqtdih8.execute-api.us-east-1.amazonaws.com/Prod/admin -X GET
FLAG{ap1_g4teway_acc3ss_con7rol} 
```

<!-- FLAG{ap1_g4teway_acc3ss_con7rol} -->