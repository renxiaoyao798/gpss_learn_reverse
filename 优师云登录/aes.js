
var CryptoJS = require('crypto-js')


data = {
    "data": {
        "username": "13011111111",
        "password": "123456",
        "redomStr": ""
    },
    "key": "password.yunjy.y",
    "param": [
        "password"
    ]
}

var o = function(t) {
            var e = t.data
              , n = t.type
              , a = t.param
              , r = t.key
              , o = JSON.parse(JSON.stringify(e));
            return "Base64" === n ? a.forEach((function(t) {
                o[t] = btoa(o[t])
            }
            )) : a.forEach((function(t) {
                var e = o[t];
                r = CryptoJS.enc.Latin1.parse(r);
                var n = r
                  , a = CryptoJS.AES.encrypt(e, r, {
                    iv: n,
                    mode: CryptoJS.mode.CBC,
                    padding: CryptoJS.pad.ZeroPadding
                });
                o[t] = a.toString()
            }
            )),
            o
        }

console.log(o(data))