window = {}
var JSEncrypt = require('jsencrypt')

function JSen(t, public_key) {
    let e = new JSEncrypt();
    return e.setPublicKey(public_key),
    e.encrypt(t) || ""
}
// console.log(JSen('{"inviteMethod":"","businessClassfication":"","mc":"","lx":"ZBGG","dwmc":"","pageIndex":1,"sign":"c9931b3d8f222bbcebfacde8fdd0fa60","timestamp":1694507673944}', 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtY9Gv1uE9Hq7+FxknrdrOlmNSaoGuDoVjVhz+rrtwDKhbcLJkK3A85DDPed3Usq/wDlMfVKwftw5c8sMiZ9ffcYBwjafN11fgn3cZDEJfgRal/x/fSOYYNLlSXP9QksSPrsM379pq14gOl1Mlke0mPeYJrppljg1idFzocyFGUwIDAQAB'))

function w(A) {
            var e, t, n = "", r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", a = "=";
            for (e = 0; e + 3 <= A.length; e += 3)
                t = parseInt(A.substring(e, e + 3), 16),
                n += r.charAt(t >> 6) + r.charAt(63 & t);
            e + 1 == A.length ? (t = parseInt(A.substring(e, e + 1), 16),
            n += r.charAt(t << 2)) : e + 2 == A.length && (t = parseInt(A.substring(e, e + 2), 16),
            n += r.charAt(t >> 2) + r.charAt((3 & t) << 4));
            while ((3 & n.length) > 0)
                n += a;
            return n
        }

encryptLong = function(A, public_key) {
            let rsa = new JSEncrypt();
            rsa.setPublicKey(public_key)
            var e = rsa.getKey()
              , t = (e.n.bitLength() + 7 >> 3) - 11;
            try {
                var n = ""
                  , r = "";
                if (A.length > t)
                    return n = A.match(/.{1,50}/g),
                    n.forEach((function(A) {
                        var t = e.encrypt(A);
                        r += t
                    }
                    )),
                    w(r);
                var a = rsa.encrypt(A)
                  , s = w(a);
                return s
            } catch (i) {
                return i
            }
        }
console.log(encryptLong('{"inviteMethod":"","businessClassfication":"","mc":"","lx":"ZBGG","dwmc":"","pageIndex":1,"sign":"c9931b3d8f222bbcebfacde8fdd0fa60","timeStamp":1694514297902}',
    'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtY9Gv1uE9Hq7+FxknrdrOlmNSaoGuDoVjVhz+rrtwDKhbcLJkK3A85DDPed3Usq/wDlMfVKwftw5c8sMiZ9ffcYBwjafN11fgn3cZDEJfgRal/x/fSOYYNLlSXP9QksSPrsM379pq14gOl1Mlke0mPeYJrppljg1idFzocyFGUwIDAQAB'))

