var CryptoJS = require('crypto-js')

p = function(e) {
            void 0 === e && (e = 16);
            for (var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""), n = "", r = 0; r < e; r++) {
                n += t[Math.ceil(61 * Math.random())]
            }
            return n
        }
// console.log(p())


l = function(e, t) {
            e = JSON.stringify(e),
            void 0 === e && (e = ""),
            void 0 === t && (t = "");
            var a = 1
              , r = CryptoJS.AES.encrypt(e.toString(), CryptoJS.enc.Utf8.parse('G$$QawckGfaLB97r'), {
                iv: CryptoJS.enc.Utf8.parse(t),
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            });
            return r = r.toString().replace(/\//g, "_").replace(/\+/g, "-").replace(/=/g, "~")
        }
data =     {"encCompanyId":"1nR-298~","positionId":3626,"cityCode":"","sortType":1,"keywordId":"","pageNum":1}
console.log(l(data,'b9QqoMSX7ahOJt3q'))