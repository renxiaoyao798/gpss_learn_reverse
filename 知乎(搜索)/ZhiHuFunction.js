//固定值
var string = '6fpLRqJO8M/c3jnYxFkUVC4ZIG12SiH=5v0mXDazWBTsuw7QetbKdoPyAl+hN9rgE';
var h = {};
h.zb = [20, 223, 245, 7, 248, 2, 194, 209, 87, 6, 227, 253, 240, 128, 222, 91, 237, 9, 125, 157, 230, 93, 252, 205, 90, 79, 144, 199, 159, 197, 186, 167, 39, 37, 156, 198, 38, 42, 43, 168, 217, 153, 15, 103, 80, 189, 71, 191, 97, 84, 247, 95, 36, 69, 14, 35, 12, 171, 28, 114, 178, 148, 86, 182, 32, 83, 158, 109, 22, 255, 94, 238, 151, 85, 77, 124, 254, 18, 4, 26, 123, 176, 232, 193, 131, 172, 143, 142, 150, 30, 10, 146, 162, 62, 224, 218, 196, 229, 1, 192, 213, 27, 110, 56, 231, 180, 138, 107, 242, 187, 54, 120, 19, 44, 117, 228, 215, 203, 53, 239, 251, 127, 81, 11, 133, 96, 204, 132, 41, 115, 73, 55, 249, 147, 102, 48, 122, 145, 106, 118, 74, 190, 29, 16, 174, 5, 177, 129, 63, 113, 99, 31, 161, 76, 246, 34, 211, 13, 60, 68, 207, 160, 65, 111, 82, 165, 67, 169, 225, 57, 112, 244, 155, 51, 236, 200, 233, 58, 61, 47, 100, 137, 185, 64, 17, 70, 234, 163, 219, 108, 170, 166, 59, 149, 52, 105, 24, 212, 78, 173, 45, 0, 116, 226, 119, 136, 206, 135, 175, 195, 25, 92, 121, 208, 126, 139, 3, 75, 141, 21, 130, 98, 241, 40, 154, 66, 184, 49, 181, 46, 243, 88, 101, 183, 8, 23, 72, 188, 104, 179, 210, 134, 250, 201, 164, 89, 216, 202, 220, 50, 221, 152, 140, 33, 235, 214];
h.zk = [1170614578, 1024848638, 1413669199, -343334464, -766094290, -1373058082, -143119608, -297228157, 1933479194, -971186181, -406453910, 460404854, -547427574, -1891326262, -1679095901, 2119585428, -2029270069, 2035090028, -1521520070, -5587175, -77751101, -2094365853, -1243052806, 1579901135, 1321810770, 456816404, -1391643889, -229302305, 330002838, -788960546, 363569021, -1947871109];
var param_arr = [48, 53, 57, 48, 53, 51, 102, 55, 100, 49, 53, 101, 48, 49, 100, 55];
var param_arr1 = [0, 8, 16, 24];
var param_index = 0;

function init() {
    param_arr1 = [0, 8, 16, 24];
    param_index = 0;
}

function md5_func(e) {
    function o(e, t) {
        var n = (65535 & e) + (65535 & t);
        return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
    }

    function a(e, t, n, r, i, a) {
        return o((c = o(o(t, e), o(r, a))) << (u = i) | c >>> 32 - u, n);
        var c, u
    }

    function c(e, t, n, r, i, o, c) {
        return a(t & n | ~t & r, e, t, i, o, c)
    }

    function u(e, t, n, r, i, o, c) {
        return a(t & r | n & ~r, e, t, i, o, c)
    }

    function s(e, t, n, r, i, o, c) {
        return a(t ^ n ^ r, e, t, i, o, c)
    }

    function l(e, t, n, r, i, o, c) {
        return a(n ^ (t | ~r), e, t, i, o, c)
    }

    function d(e, t) {
        var n, r, i, a, d;
        e[t >> 5] |= 128 << t % 32,
            e[14 + (t + 64 >>> 9 << 4)] = t;
        var f = 1732584193
            , p = -271733879
            , h = -1732584194
            , b = 271733878;
        for (n = 0; n < e.length; n += 16)
            r = f,
                i = p,
                a = h,
                d = b,
                f = c(f, p, h, b, e[n], 7, -680876936),
                b = c(b, f, p, h, e[n + 1], 12, -389564586),
                h = c(h, b, f, p, e[n + 2], 17, 606105819),
                p = c(p, h, b, f, e[n + 3], 22, -1044525330),
                f = c(f, p, h, b, e[n + 4], 7, -176418897),
                b = c(b, f, p, h, e[n + 5], 12, 1200080426),
                h = c(h, b, f, p, e[n + 6], 17, -1473231341),
                p = c(p, h, b, f, e[n + 7], 22, -45705983),
                f = c(f, p, h, b, e[n + 8], 7, 1770035416),
                b = c(b, f, p, h, e[n + 9], 12, -1958414417),
                h = c(h, b, f, p, e[n + 10], 17, -42063),
                p = c(p, h, b, f, e[n + 11], 22, -1990404162),
                f = c(f, p, h, b, e[n + 12], 7, 1804603682),
                b = c(b, f, p, h, e[n + 13], 12, -40341101),
                h = c(h, b, f, p, e[n + 14], 17, -1502002290),
                f = u(f, p = c(p, h, b, f, e[n + 15], 22, 1236535329), h, b, e[n + 1], 5, -165796510),
                b = u(b, f, p, h, e[n + 6], 9, -1069501632),
                h = u(h, b, f, p, e[n + 11], 14, 643717713),
                p = u(p, h, b, f, e[n], 20, -373897302),
                f = u(f, p, h, b, e[n + 5], 5, -701558691),
                b = u(b, f, p, h, e[n + 10], 9, 38016083),
                h = u(h, b, f, p, e[n + 15], 14, -660478335),
                p = u(p, h, b, f, e[n + 4], 20, -405537848),
                f = u(f, p, h, b, e[n + 9], 5, 568446438),
                b = u(b, f, p, h, e[n + 14], 9, -1019803690),
                h = u(h, b, f, p, e[n + 3], 14, -187363961),
                p = u(p, h, b, f, e[n + 8], 20, 1163531501),
                f = u(f, p, h, b, e[n + 13], 5, -1444681467),
                b = u(b, f, p, h, e[n + 2], 9, -51403784),
                h = u(h, b, f, p, e[n + 7], 14, 1735328473),
                f = s(f, p = u(p, h, b, f, e[n + 12], 20, -1926607734), h, b, e[n + 5], 4, -378558),
                b = s(b, f, p, h, e[n + 8], 11, -2022574463),
                h = s(h, b, f, p, e[n + 11], 16, 1839030562),
                p = s(p, h, b, f, e[n + 14], 23, -35309556),
                f = s(f, p, h, b, e[n + 1], 4, -1530992060),
                b = s(b, f, p, h, e[n + 4], 11, 1272893353),
                h = s(h, b, f, p, e[n + 7], 16, -155497632),
                p = s(p, h, b, f, e[n + 10], 23, -1094730640),
                f = s(f, p, h, b, e[n + 13], 4, 681279174),
                b = s(b, f, p, h, e[n], 11, -358537222),
                h = s(h, b, f, p, e[n + 3], 16, -722521979),
                p = s(p, h, b, f, e[n + 6], 23, 76029189),
                f = s(f, p, h, b, e[n + 9], 4, -640364487),
                b = s(b, f, p, h, e[n + 12], 11, -421815835),
                h = s(h, b, f, p, e[n + 15], 16, 530742520),
                f = l(f, p = s(p, h, b, f, e[n + 2], 23, -995338651), h, b, e[n], 6, -198630844),
                b = l(b, f, p, h, e[n + 7], 10, 1126891415),
                h = l(h, b, f, p, e[n + 14], 15, -1416354905),
                p = l(p, h, b, f, e[n + 5], 21, -57434055),
                f = l(f, p, h, b, e[n + 12], 6, 1700485571),
                b = l(b, f, p, h, e[n + 3], 10, -1894986606),
                h = l(h, b, f, p, e[n + 10], 15, -1051523),
                p = l(p, h, b, f, e[n + 1], 21, -2054922799),
                f = l(f, p, h, b, e[n + 8], 6, 1873313359),
                b = l(b, f, p, h, e[n + 15], 10, -30611744),
                h = l(h, b, f, p, e[n + 6], 15, -1560198380),
                p = l(p, h, b, f, e[n + 13], 21, 1309151649),
                f = l(f, p, h, b, e[n + 4], 6, -145523070),
                b = l(b, f, p, h, e[n + 11], 10, -1120210379),
                h = l(h, b, f, p, e[n + 2], 15, 718787259),
                p = l(p, h, b, f, e[n + 9], 21, -343485551),
                f = o(f, r),
                p = o(p, i),
                h = o(h, a),
                b = o(b, d);
        return [f, p, h, b]
    }

    function f(e) {
        var t, n = "", r = 32 * e.length;
        for (t = 0; t < r; t += 8)
            n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
        return n
    }

    function p(e) {
        var t, n = [];
        for (n[(e.length >> 2) - 1] = void 0,
                 t = 0; t < n.length; t += 1)
            n[t] = 0;
        var r = 8 * e.length;
        for (t = 0; t < r; t += 8)
            n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
        return n
    }

    function h(e) {
        var t, n, r = "";
        for (n = 0; n < e.length; n += 1)
            t = e.charCodeAt(n),
                r += "0123456789abcdef".charAt(t >>> 4 & 15) + "0123456789abcdef".charAt(15 & t);
        return r
    }

    function b(e) {
        return unescape(encodeURIComponent(e))
    }

    function v(e) {
        return function (e) {
            return f(d(p(e), 8 * e.length))
        }(b(e))
    }

    function g(e, t) {
        return function (e, t) {
            var n, r, i = p(e), o = [], a = [];
            for (o[15] = a[15] = void 0,
                 i.length > 16 && (i = d(i, 8 * e.length)),
                     n = 0; n < 16; n += 1)
                o[n] = 909522486 ^ i[n],
                    a[n] = 1549556828 ^ i[n];
            return r = d(o.concat(p(t)), 512 + 8 * t.length),
                f(d(a.concat(r), 640))
        }(b(e), b(t))
    }

    function O(e, t, n) {
        return t ? n ? g(t, e) : h(g(t, e)) : n ? v(e) : h(v(e))
    }

    return h(v(e));
}

function encrypt_param(md5_str) {
    var md5_arr = []
    //md5值轮流 charCodeAt得到一个数组
    for (let i = 0; i < md5_str.length; i++) {
        md5_arr.push(md5_str.charCodeAt(i))
    }

    //开头拼上0
    md5_arr.unshift(0)
    //拼上计算逻辑耗时
    md5_arr.unshift(60)

    //截取前16位
    var md5_arr_16 = md5_arr.slice(0, 16)

    // 计算得到一个新的数组
    var new_md5_arr_16 = []
    for (let i = 0; i < md5_arr_16.length; i++) {
        new_md5_arr_16.push(md5_arr_16[i] ^ param_arr[i] ^ 42)
    }


    function rrr(e) {
        var t = new Array(16)
            , n = new Array(36);
        n[0] = B(e, 0),
            n[1] = B(e, 4),
            n[2] = B(e, 8),
            n[3] = B(e, 12);
        for (var r = 0; r < 32; r++) {
            var o = G(n[r + 1] ^ n[r + 2] ^ n[r + 3] ^ h.zk[r]);
            n[r + 4] = n[r] ^ o
        }
        return i(n[35], t, 0),
            i(n[34], t, 4),
            i(n[33], t, 8),
            i(n[32], t, 12),
            t
    }

    function i(e, t, n) {
        t[n] = 255 & e >>> 24,
            t[n + 1] = 255 & e >>> 16,
            t[n + 2] = 255 & e >>> 8,
            t[n + 3] = 255 & e
    }

    function B(e, t) {
        return (255 & e[t]) << 24 | (255 & e[t + 1]) << 16 | (255 & e[t + 2]) << 8 | 255 & e[t + 3]
    }

    function Q(e, t) {
        return (4294967295 & e) << t | e >>> 32 - t
    }

    function G(e) {
        var t = new Array(4)
            , n = new Array(4);
        i(e, t, 0),
            n[0] = h.zb[255 & t[0]],
            n[1] = h.zb[255 & t[1]],
            n[2] = h.zb[255 & t[2]],
            n[3] = h.zb[255 & t[3]];
        var r = B(n, 0);
        return r ^ Q(r, 2) ^ Q(r, 10) ^ Q(r, 18) ^ Q(r, 24)
    }

    function xxx(e, t) {
        for (var n = [], r = e.length, i = 0; 0 < r; r -= 16) {
            for (var o = e.slice(16 * i, 16 * (i + 1)), a = new Array(16), c = 0; c < 16; c++)
                a[c] = o[c] ^ t[c];
            t = rrr(a),
                n = n.concat(t),
                i++
        }
        return n
    }

//再计算又得到一个新的数组
    new_md5_arr_16 = rrr(new_md5_arr_16)
// console.log('new_md5_arr_16:', new_md5_arr_16)


// console.log(md5_arr.slice(16, 92))


//截取数组 并把新数组放进去 得到一个80位数组
    var arr_80 = xxx(md5_arr.slice(16, 92), new_md5_arr_16);
//新数组 拼接上80位数组 得到一个96位数组
    var result_arr = new_md5_arr_16.concat(arr_80);


    function getParamArr() {
        var result = param_arr1[param_index];
        param_index++;
        if (param_index >= param_arr1.length) {
            param_index = 0;
        }
        return result;
    }

    function encrypt(result_arr) {
        var sinArr = [];
        for (let j = result_arr.length - 1; j > 0; j -= 3) {
            var index = j;

            var num1 = result_arr[j];
            var paramArrNum1 = getParamArr();
            var cal_num1 = num1 ^ ((58 >>> paramArrNum1) & 255);

            var num2 = result_arr[index - 1];
            var paramArrNum2 = getParamArr();
            var cal_num2 = (num2 ^ ((58 >>> paramArrNum2) & 255)) << 8;

            var num3 = result_arr[index - 2];
            var paramArrNum3 = getParamArr();
            var cal_num3 = (num3 ^ ((58 >>> paramArrNum3) & 255)) << 16;

            var res_num = (cal_num1 | cal_num2) | cal_num3;

            sinArr.push(string.charAt(res_num & 63))
            sinArr.push(string.charAt((res_num >>> 6) & 63))
            sinArr.push(string.charAt((res_num >>> 12) & 63))
            sinArr.push(string.charAt((res_num >>> 18) & 63))

        }
        return sinArr.join("");
    }

    return encrypt(result_arr);
}

function skr(str,d_c0){
    var md5_str = md5_func('101_3_3.0+/api/v4/search_v3?'+ str + "+" + d_c0)
// // md5_str = '91ca4aeee4beeb0f81ea5c536dd04029'
console.log(md5_str)
// //加密
console.log(encrypt_param(md5_str))
    return encrypt_param(md5_str)
}



//记得初始化
// param_arr1 = [0, 8, 16, 24];
// //md5
var md5_str = md5_func('101_3_3.0+/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E7%BB%93%E8%B4%A6%E6%97%B6%E5%8F%91%E7%8E%B0%E4%B8%9C%E8%A5%BF%E5%BE%88%E8%B4%B5%E5%92%8B%E5%8A%9E&correction=1&offset=20&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+AMDWa-7nIRePTpKNqMyPT-fcTBwDvAxRMY4=|1690192383')
// // md5_str = '91ca4aeee4beeb0f81ea5c536dd04029'
console.log(md5_str)
// //加密
console.log(encrypt_param(md5_str))

// var result = encrypt_param('{"content":"<div>6666666666666</div>","unfriendly_check":"strict"}')
// console.log(result)
//
// var express = require("express")
// //var sdk = require("./encrypt.js")
// var bodyParser = require('body-parser')
// var api = express()
// api.use(bodyParser.urlencoded({
//     parameterLimit: 50000,
//     limit: '50mb',
//     extended: false
// }));
//
// api.get('/get_token', function (req, res) {
//     init();
//     var result = encrypt_param('{"content":"<div>6666666666666</div>","unfriendly_check":"strict"}')
//     res.send(result)
// });
//
// api.post('/encrypt', function (req, res) {
//     init();
//     var data = req.body.paramsData;
//     console.log(data)
//     var result = encrypt_param(data)
//     res.send(result)
// });
//
// api.post('/encryptByMd5', function (req, res) {
//     init();
//     var data = req.body.paramsData;
//     console.log(data)
//     data = md5_func(data)
//     console.log(data)
//     var result = encrypt_param(data)
//     res.send(result)
// });
//
// var server = api.listen(5555, function () {
//     console.log("启动成功，测试地址为:")
//     console.log("http://127.0.0.1:5555/get_token")
// })

