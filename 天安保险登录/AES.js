var CryptoJS = require('crypto-js')


getAesKey = function(l) {
                l = l || 32;
                for (var n = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", t = n.length, e = "", a = 0; a < l; a++)
                    e += n.charAt(Math.floor(Math.random() * t));
                return e
            }

function aes_decryt(l,key) {
    l = l.replace(/[\r\n]/g, "")
    var n = CryptoJS.enc.Base64.parse(l)
        , t = CryptoJS.enc.Utf8.parse(key)
        , e = CryptoJS.enc.Utf8.parse(key)
        , a = CryptoJS.lib.CipherParams.create({
            ciphertext: n
    });
    return CryptoJS.AES.decrypt(a, t, {
        iv: e,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8)

}


function aes_encryt(l, key) {
    l = JSON.stringify(l)
    var n = CryptoJS.enc.Utf8.parse(key)
      , t = CryptoJS.enc.Utf8.parse(key)
      , e = CryptoJS.enc.Utf8.parse(l)
      , a = CryptoJS.AES.encrypt(e, n, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return CryptoJS.enc.Base64.stringify(a.ciphertext)
}
data = {
    "body": {
        "loginMethod": "1",
        "name": "13599813213",
        "password": "12345678"
    },
    "head": {
        "userCode": null,
        "channelCode": "101",
        "transTime": 1689648799335,
        "transToken": "",
        "customerId": null,
        "transSerialNumber": ""
    }
}
// console.log(aes_decryt('KgZfsAfwsOkwmtdnkfcXiInFSUhkIH5FQr5EPjnkdDtiCUHng7guaa5KSA09rbXG4xSbNJQMWj5lzAGTCRnZ+a/nBUrIzgxLvfPp4QX7TzKgTDj1iqOHDKayGeUfblknARdPVZa1dizOgbi7DrLdccDu2SNFJEngLcORVxAL3zpOeRhi/DT0cEMcN9yKRMck6HposNnqMntMflQKlbm37donJcDAlnxzHUWyo1iLo9XptDcf2lmyzzRxWWCX8ASSAgUdl2KjceXkpkRW1gOW5fGyzXVgY4oV1iT85TMUaptxrWsKNS3nYC9Gop9e3ZFW'))
// console.log(aes_encryt(data))
console.log(getAesKey(16))
