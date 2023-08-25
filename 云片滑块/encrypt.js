var CryptoJS = require('crypto-js')
window = {}
mt_getRandomStr = function(t) {
        for (var e = ""; e.length < t; )
            e += Math.random().toString(36).substr(2);
        return e = e.slice(0, t)
    }
var JSEncrypt = require('jsencrypt')

function JSen(t) {
    let e = new JSEncrypt();
    return e.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDnOWe/gs033L/2/xR3oi6SLAMPBY5VledUqqH6dbCNOdrGX4xW+1x6NUfvmwpHRBA2C7xWDDvOIldTl0rMtERTDy9homrVqEcW6/TY+dSVFL3e2Yg2sVaehHv7FhmATkgfC2FcXt8Wvm99QpKRSrGKpcFYJwOj2F8hJh+rTG0IPQIDAQAB"),
    e.encrypt(t) || ""
}

get_cb = function() {
    return  Math.random().toString(32).replace("0.", "")

}

encrypt = function(e) {

                t = JSON.stringify(e);
                var e = mt_getRandomStr(16)
                  , n = mt_getRandomStr(16);
                return {
                    i: CryptoJS.AES.encrypt(t, CryptoJS.enc.Utf8.parse(e), {
                        iv: CryptoJS.enc.Utf8.parse(n)
                    }).toString(),
                    k: JSen(e + n)
                }
            }

// function locus_encrpt(offsetX, points) {
//     distanceX = (304 - 60) * (offsetX / (304 - 42)) / 304;
//
//     let t = {
//         "points": points,
//         "distanceX": distanceX,
//         "fp": "e935061666a2bf07cf7f977b34f492ba",
//         "address": "https://www.yunpian.com",
//         "yp_riddler_id": "27eb1d66-a41a-4771-ac5c-3e5c6c08ab29"
//     }
//
//     t = JSON.stringify(t);
//     var e = getRandomStr(16)
//         , n = getRandomStr(16);
//
//     return {
//         cb: Math.random().toString(32).replace("0.", ""),
//         i: CryptoJS.AES.encrypt(t, parse(e), {iv: parse(n)}).toString(),
//         k: rsaEncrypt(e + n),
//         captchaId: '974cd565f11545b6a5006d10dc324281'
//     }
// }


console.log(encrypt())