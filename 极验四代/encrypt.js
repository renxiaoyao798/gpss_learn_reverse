const CryptoJS = require("crypto-js");
aes_encrypt = function(e, s) {


                t = CryptoJS.enc.Utf8.parse(s)
                n = CryptoJS.enc.Utf8.parse('0000000000000000')
                aes_data = CryptoJS.AES.encrypt(e,t, {
                        iv: n,
                        mode: CryptoJS.mode.CBC,
                        padding:CryptoJS.pad.Pkcs7
                    })
                for (r = aes_data['ciphertext']['words'], i = aes_data['ciphertext']['sigBytes'], o = [], a = 0; a < i; a++) {
                                    var u = r[a >>> 2] >>> 24 - a % 4 * 8 & 255;
                                    o['push'](u);
                }
                return arrayTohex(o)
            }
arrayTohex = function w(e) {

    for (var t = [], n = 0, s = 0; s < 2 * e['length']; s += 2)
        t[s >>> 3] |= parseInt(e[n], 10) << 24 - s % 8 * 4,
        n++;
    for (var r = [], i = 0; i < e['length']; i++) {
        var o = t[i >>> 2] >>> 24 - i % 4 * 8 & 255;
        r['push']((o >>> 4)['toString'](16)),
        r['push']((15 & o)['toString'](16));
    }
    return r['join']('');
}
window = this;
navigator = {
    'appName': 'Netscape',
}
var r = function() {
    function n() {

                this['i'] = 0,
                this['j'] = 0,
                this['S'] = [];
    }
    n['prototype']['init'] = function C(e) {

        var t, n, s;
        for (t = 0; t < 256; ++t)
            this['S'][t] = t;
        for (t = n = 0; t < 256; ++t)
            n = n + this['S'][t] + e[t % e['length']] & 255,
            s = this['S'][t],
            this['S'][t] = this['S'][n],
            this['S'][n] = s;
        this['i'] = 0,
        this['j'] = 0;
    }
    ,
    n['prototype']['next'] = function E() {

        var e;
        return this['i'] = this['i'] + 1 & 255,
        this['j'] = this['j'] + this['S'][this['i']] & 255,
        e = this['S'][this['i']],
        this['S'][this['i']] = this['S'][this['j']],
        this['S'][this['j']] = e,
        this['S'][e + this['S'][this['i']] & 255];
    }
    ;
    var s, r, i, t, o = 256;
    if (null == r) {
        var a;
        if (r = [],
        i = 0,
        window['crypto'] && window['crypto']['getRandomValues']) {
            var u = new Uint32Array(256);
            for (window['crypto']['getRandomValues'](u),
            a = 0; a < u['length']; ++a)
                r[i++] = 255 & u[a];
        }
        var c = 0
          , _ = function _(t) {
            if (256 <= (c = c || 0) || o <= i)
                window['removeEventListener'] ? (c = 0,
                window['removeEventListener']('mousemove', _, !1)) : window['detachEvent'] && (c = 0,
                window['detachEvent']('onmousemove', _));
            else
                try {
                    var n = t['x'] + t['y'];
                    r[i++] = 255 & n,
                    c += 1;
                } catch (e) {}
        };
        window['addEventListener'] ? window['addEventListener']('mousemove', _, !1) : window['attachEvent'] && window['attachEvent']('onmousemove', _);
    }
    function h() {
            s = function t() {

                return new n();
            }();
            while (i < o) {
                var e = Math['floor'](65536 * Math['random']());
                r[i++] = 255 & e;
            }
            for (s['init'](r),
            i = 0; i < r['length']; ++i)
                r[i] = 0;
            i = 0;
            return s['next']();


    }
    function l() {
    }
    l['prototype']['nextBytes'] = function A(e) {

        var t;
        for (t = 0; t < e['length']; ++t)
            e[t] = h();
    }
    ;
    function b(e, t, n) {
        null != e && ('number' == typeof e ? this['fromNumber'](e, t, n) : null == t && 'string' != typeof e ? this['fromString'](e, 256) : this['fromString'](e, t));
    }
    function w() {
        return new b(null);
    }
    t = 'Microsoft Internet Explorer' == navigator['appName'] ? (b['prototype']['am'] = function B(e, t, n, s, r, i) {
        var o = 32767 & t
          , a = t >> 15;
        while (0 <= --i) {
            var u = 32767 & this[e]
              , c = this[e++] >> 15
              , _ = a * u + c * o;
            r = ((u = o * u + ((32767 & _) << 15) + n[s] + (1073741823 & r)) >>> 30) + (_ >>> 15) + a * c + (r >>> 30),
            n[s++] = 1073741823 & u;
        }
        return r;
    }
    ,
    30) : 'Netscape' != navigator['appName'] ? (b['prototype']['am'] = function S(e, t, n, s, r, i) {

        while (0 <= --i) {
            var o = t * this[e++] + n[s] + r;
            r = Math[$_DJADo(590)](o / 67108864),
            n[s++] = 67108863 & o;
        }
        return r;
    }
    ,
    26) : (b['prototype']['am'] = function D(e, t, n, s, r, i) {

        var o = 16383 & t
          , a = t >> 14;
        while (0 <= --i) {
            var u = 16383 & this[e]
              , c = this[e++] >> 14
              , _ = a * u + c * o;
            r = ((u = o * u + ((16383 & _) << 14) + n[s] + r) >> 28) + (_ >> 14) + a * c,
            n[s++] = 268435455 & u;
        }
        return r;
    }
    ,
    28),
    b['prototype']['DB'] = t,
    b['prototype']['DM'] = (1 << t) - 1,
    b['prototype']['DV'] = 1 << t;
    b['prototype']['FV'] = Math['pow'](2, 52),
    b['prototype']['F1'] = 52 - t,
    b['prototype']['F2'] = 2 * t - 52;
    var p, f, d = '0123456789abcdefghijklmnopqrstuvwxyz', g = [];
    for (p = '0'['charCodeAt'](0),
    f = 0; f <= 9; ++f)
        g[p++] = f;
    for (p = 'a'['charCodeAt'](0),
    f = 10; f < 36; ++f)
        g[p++] = f;
    for (p = 'A'['charCodeAt'](0),
    f = 10; f < 36; ++f)
        g[p++] = f;
    function m(e) {
        return d['charAt'](e);
    }
    function v(e) {

        var t = w();

        return t['fromInt'](e),
        t;



    }
    function y(e) {

        var t, n = 1;
        return 0 != (t = e >>> 16) && (e = t,
        n += 16),
        0 != (t = e >> 8) && (e = t,
        n += 8),
        0 != (t = e >> 4) && (e = t,
        n += 4),
        0 != (t = e >> 2) && (e = t,
        n += 2),
        0 != (t = e >> 1) && (e = t,
        n += 1),
        n;

    }
    function x(e) {
        this['m'] = e;
    }
    function k(e) {

        this['m'] = e,
        this['mp'] = e['invDigit'](),
        this['mpl'] = 32767 & this['mp'],
        this['mph'] = this['mp'] >> 15,
        this['um'] = (1 << e['DB'] - 15) - 1,
        this['mt2'] = 2 * e['t'];

    }
    function T() {

                this['n'] = null,
                this['e'] = 0,
                this['d'] = null,
                this['p'] = null,
                this['q'] = null,
                this['dmp1'] = null,
                this['dmq1'] = null,
                this['coeff'] = null;
                this['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');

    }
    return x['prototype']['convert'] = function z(e) {

        return e[$_DJBCG(47)] < 0 || 0 <= e[$_DJBDa(1316)](this[$_DJBCG(6)]) ? e[$_DJBCG(1376)](this[$_DJBDa(6)]) : e;
    }
    ,
    x['prototype']['revert'] = function F(e) {
        return e;
    }
    ,
    x['prototype']['reduce'] = function M(e) {
        e[$_DJCDI(1380)](this[$_DJCDI(6)], null, e);
    }
    ,
    x['prototype']['mulTo'] = function O(e, t, n) {

        e[$_DJCIO(1361)](t, n),
        this[$_DJCHQ(893)](n);
    }
    ,
    x['prototype']['sqrTo'] = function R(e, t) {

        e[$_DJDDh(1338)](t),
        this[$_DJDCV(893)](t);
    }
    ,
    k['prototype']['convert'] = function I(e) {
        var t = w();
        return e['abs']()['dlShiftTo'](this['m']['t'], t),
        t['divRemTo'](this['m'], null, t),
        e['s'] < 0 && 0 < t['compareTo'](b['ZERO']) && this['m']['subTo'](t, t),
        t;
    }
    ,
    k['prototype']['revert'] = function P(e) {

        var t = w();
        return e['copyTo'](t),
        this['reduce'](t),
        t;
    }
    ,
    k['prototype']['reduce'] = function j(e) {

        while (e['t'] <= this['mt2'])
            e[e['t']++] = 0;
        for (var t = 0; t < this['m']['t']; ++t) {
            var n = 32767 & e[t]
              , s = n * this['mpl'] + ((n * this['mph'] + (e[t] >> 15) * this['mpl'] & this['um']) << 15) & e['DM'];
            e[n = t + this['m']['t']] += this['m']['am'](0, s, e, t, 0, this['m']['t']);
            while (e[n] >= e['DV'])
                e[n] -= e['DV'],
                e[++n]++;
        }
        e['clamp'](),
        e['drShiftTo'](this['m']['t'], e),
        0 <= e['compareTo'](this['m']) && e['subTo'](this['m'], e);
    }
    ,
    k['prototype']['mulTo'] = function N(e, t, n) {
        e['multiplyTo'](t, n),
        this['reduce'](n);
    }
    ,
    k['prototype']['sqrTo'] = function L(e, t) {

        e['squareTo'](t),
        this['reduce'](t);
    }
    ,
    b['prototype']['copyTo'] = function q(e) {

        for (var t = this['t'] - 1; 0 <= t; --t)
            e[t] = this[t];
        e['t'] = this['t'],
        e['s'] = this['s'];
    }
    ,
    b['prototype']['fromInt'] = function H(e) {

        this['t'] = 1,
        this['s'] = e < 0 ? -1 : 0,
        0 < e ? this[0] = e : e < -1 ? this[0] = e + this['DV'] : this['t'] = 0;
    }
    ,
    b['prototype']['fromString'] = function U(e, t) {

        var n;
        if (16 == t)
            n = 4;
        else if (8 == t)
            n = 3;
        else if (256 == t)
            n = 8;
        else if (2 == t)
            n = 1;
        else if (32 == t)
            n = 5;
        else {
            if (4 != t)
                return void this[$_DJHCI(1346)](e, t);
            n = 2;
        }
        this['t'] = 0,
        this['s'] = 0;
        var s, r, i = e['length'], o = !1, a = 0;
        while (0 <= --i) {
            var u = 8 == n ? 255 & e[i] : (s = i,
            null == (r = g[e['charCodeAt'](s)]) ? -1 : r);
            u < 0 ? '-' == e['charAt'](i) && (o = !0) : (o = !1,
            0 == a ? this[this['t']++] = u : a + n > this['DB'] ? (this[this['t'] - 1] |= (u & (1 << this['DB'] - a) - 1) << a,
            this[this['t']++] = u >> this['DB'] - a) : this[this['t'] - 1] |= u << a,
            (a += n) >= this['DB'] && (a -= this['DB']));
        }
        8 == n && 0 != (128 & e[0]) && (this['s'] = -1,
        0 < a && (this[this['t'] - 1] |= (1 << this['DB'] - a) - 1 << a)),
        this['clamp'](),
        o && b['ZERO']['subTo'](this, this);
    }
    ,
    b['prototype']['clamp'] = function V() {

        var e = this['s'] & this['DM'];
        while (0 < this['t'] && this[this['t'] - 1] == e)
            --this['t'];
    }
    ,
    b['prototype']['dlShiftTo'] = function $(e, t) {

        var n;
        for (n = this['t'] - 1; 0 <= n; --n)
            t[n + e] = this[n];
        for (n = e - 1; 0 <= n; --n)
            t[n] = 0;
        t['t'] = this['t'] + e,
        t['s'] = this['s'];
    }
    ,
    b['prototype']['drShiftTo'] = function X(e, t) {

        for (var n = e; n < this['t']; ++n)
            t[n - e] = this[n];
        t['t'] = Math['max'](this['t'] - e, 0),
        t['s'] = this['s'];
    }
    ,
    b['prototype']['lShiftTo'] = function G(e, t) {

        var n, s = e % this['DB'], r = this['DB'] - s, i = (1 << r) - 1, o = Math['floor'](e / this['DB']), a = this['s'] << s & this['DM'];
        for (n = this['t'] - 1; 0 <= n; --n)
            t[n + o + 1] = this[n] >> r | a,
            a = (this[n] & i) << s;
        for (n = o - 1; 0 <= n; --n)
            t[n] = 0;
        t[o] = a,
        t['t'] = this['t'] + o + 1,
        t['s'] = this['s'],
        t['clamp']();
    }
    ,
    b['prototype']['rShiftTo'] = function W(e, t) {

        t['s'] = this['s'];
        var n = Math['floor'](e / this['DB']);
        if (n >= this['t'])
            t['t'] = 0;
        else {
            var s = e % this['DB']
              , r = this['DB'] - s
              , i = (1 << s) - 1;
            t[0] = this[n] >> s;
            for (var o = n + 1; o < this['t']; ++o)
                t[o - n - 1] |= (this[o] & i) << r,
                t[o - n] = this[o] >> s;
            0 < s && (t[this['t'] - n - 1] |= (this['s'] & i) << r),
            t['t'] = this['t'] - n,
            t['clamp']();
        }
    }
    ,
    b['prototype']['subTo'] = function Z(e, t) {
        var n = 0
          , s = 0
          , r = Math['min'](e['t'], this['t']);
        while (n < r)
            s += this[n] - e[n],
            t[n++] = s & this['DM'],
            s >>= this['DB'];
        if (e['t'] < this['t']) {
            s -= e['s'];
            while (n < this['t'])
                s += this[n],
                t[n++] = s & this['DM'],
                s >>= this['DB'];
            s += this['s'];
        } else {
            s += this['s'];
            while (n < e['t'])
                s -= e[n],
                t[n++] = s & this['DM'],
                s >>= this['DB'];
            s -= e['s'];
        }
        t['s'] = s < 0 ? -1 : 0,
        s < -1 ? t[n++] = this['DV'] + s : 0 < s && (t[n++] = s),
        t['t'] = n,
        t['clamp']();
    }
    ,
    b['prototype']['multiplyTo'] = function K(e, t) {
        var n = this['abs']()
          , s = e['abs']()
          , r = n['t'];
        t['t'] = r + s['t'];
        while (0 <= --r)
            t[r] = 0;
        for (r = 0; r < s['t']; ++r)
            t[r + n['t']] = n['am'](0, s[r], t, r, 0, n['t']);
        t['s'] = 0,
        t['clamp'](),
        this['s'] != e['s'] && b['ZERO']['subTo'](t, t);
    }
    ,
    b['prototype']['squareTo'] = function Y(e) {
        var t = this['abs']()
          , n = e['t'] = 2 * t['t'];
        while (0 <= --n)
            e[n] = 0;
        for (n = 0; n < t['t'] - 1; ++n) {
            var s = t['am'](n, t[n], e, 2 * n, 0, 1);
            (e[n + t['t']] += t['am'](n + 1, 2 * t[n], e, 2 * n + 1, s, t['t'] - n - 1)) >= t['DV'] && (e[n + t['t']] -= t['DV'],
            e[n + t['t'] + 1] = 1);
        }
        0 < e['t'] && (e[e['t'] - 1] += t['am'](n, t[n], e, 2 * n, 0, 1)),
        e['s'] = 0,
        e['clamp']();
    }
    ,
    b['prototype']['divRemTo'] = function Q(e, t, n) {
        var s = e['abs']();
        if (!(s['t'] <= 0)) {
            var r = this['abs']();
            if (r['t'] < s['t'])
                return null != t && t['fromInt'](0),
                void (null != n && this['copyTo'](n));
            null == n && (n = w());
            var i = w()
              , o = this['s']
              , a = e['s']
              , u = this['DB'] - y(s[s['t'] - 1]);
            0 < u ? (s['lShiftTo'](u, i),
            r['lShiftTo'](u, n)) : (s['copyTo'](i),
            r['copyTo'](n));
            var c = i['t']
              , _ = i[c - 1];
            if (0 != _) {
                var h = _ * (1 << this['F1']) + (1 < c ? i[c - 2] >> this['F2'] : 0)
                  , l = this['FV'] / h
                  , p = (1 << this['F1']) / h
                  , f = 1 << this['F2']
                  , d = n['t']
                  , g = d - c
                  , m = null == t ? w() : t;
                i['dlShiftTo'](g, m),
                0 <= n['compareTo'](m) && (n[n['t']++] = 1,
                n['subTo'](m, n)),
                b['ONE']['dlShiftTo'](c, m),
                m['subTo'](i, i);
                while (i['t'] < c)
                    i[i['t']++] = 0;
                while (0 <= --g) {
                    var v = n[--d] == _ ? this['DM'] : Math['floor'](n[d] * l + (n[d - 1] + f) * p);
                    if ((n[d] += i['am'](0, v, n, g, 0, c)) < v) {
                        i['dlShiftTo'](g, m),
                        n['subTo'](m, n);
                        while (n[d] < --v)
                            n['subTo'](m, n);
                    }
                }
                null != t && (n['drShiftTo'](c, t),
                o != a && b['ZERO']['subTo'](t, t)),
                n['t'] = c,
                n['clamp'](),
                0 < u && n['rShiftTo'](u, n),
                o < 0 && b['ZERO']['subTo'](n, n);
            }
        }
    }
    ,
    b['prototype']['invDigit'] = function J() {

        if (this['t'] < 1)
            return 0;
        var e = this[0];
        if (0 == (1 & e))
            return 0;
        var t = 3 & e;
        return 0 < (t = (t = (t = (t = t * (2 - (15 & e) * t) & 15) * (2 - (255 & e) * t) & 255) * (2 - ((65535 & e) * t & 65535)) & 65535) * (2 - e * t % this['DV']) % this['DV']) ? this['DV'] - t : -t;
    }
    ,
    b['prototype']['isEven'] = function ee() {

        return 0 == (0 < this['t'] ? 1 & this[0] : this['s']);
    }
    ,
    b['prototype']['exp'] = function te(e, t) {
        if (4294967295 < e || e < 1)
            return b[$_EADDO(1362)];
        var n = w()
          , s = w()
          , r = t['convert'](this)
          , i = y(e) - 1;
        r['copyTo'](n);
        while (0 <= --i)
            if (t['sqrTo'](n, s),
            0 < (e & 1 << i))
                t['mulTo'](s, r, n);
            else {
                var o = n;
                n = s,
                s = o;
            }
        return t['revert'](n);
    }
    ,
    b['prototype']['toString'] = function ne(e) {
        if (this['s'] < 0)
            return '-' + this['negate']()['toString'](e);
        var t;
        if (16 == e)
            t = 4;
        else if (8 == e)
            t = 3;
        else if (2 == e)
            t = 1;
        else if (32 == e)
            t = 5;
        else {
            if (4 != e)
                return this['toRadix'](e);
            t = 2;
        }
        var n, s = (1 << t) - 1, r = !1, i = '', o = this['t'], a = this['DB'] - o * this['DB'] % t;
        if (0 < o--) {
            a < this['DB'] && 0 < (n = this[o] >> a) && (r = !0,
            i = m(n));
            while (0 <= o)
                a < t ? (n = (this[o] & (1 << a) - 1) << t - a,
                n |= this[--o] >> (a += this['DB'] - t)) : (n = this[o] >> (a -= t) & s,
                a <= 0 && (a += this['DB'],
                --o)),
                0 < n && (r = !0),
                r && (i += m(n));
        }
        return r ? i : '0';
    }
    ,
    b['prototype']['negate'] = function se() {
        var e = w();
        return b[$_EAEDP(1364)][$_EAECw(1329)](this, e),
        e;
    }
    ,
    b['prototype']['abs'] = function re() {
        return this['s'] < 0 ? this['negate']() : this;
    }
    ,
    b['prototype']['compareTo'] = function ie(e) {
        var t = this['s'] - e['s'];
        if (0 != t)
            return t;
        var n = this['t'];
        if (0 != (t = n - e['t']))
            return this['s'] < 0 ? -t : t;
        while (0 <= --n)
            if (0 != (t = this[n] - e[n]))
                return t;
        return 0;
    }
    ,
    b['prototype']['bitLength'] = function oe() {

        return this['t'] <= 0 ? 0 : this['DB'] * (this['t'] - 1) + y(this[this['t'] - 1] ^ this['s'] & this['DM']);
    }
    ,
    b['prototype']['mod'] = function ae(e) {
        var t = w();
        return this[$_EAGDw(661)]()[$_EAGDw(1380)](e, null, t),
        this[$_EAGCV(47)] < 0 && 0 < t[$_EAGCV(1316)](b[$_EAGCV(1364)]) && e[$_EAGDw(1329)](t, t),
        t;
    }
    ,
    b['prototype']['modPowInt'] = function ue(e, t) {
        var n;
        return n = e < 256 || t['isEven']() ? new x(t) : new k(t),
        this['exp'](e, n);
    }
    ,
    b['ZERO'] = v(0),
    b['ONE'] = v(1),
    T['prototype']['doPublic'] = function ce(e) {

        return e['modPowInt'](this['e'], this['n']);
    }
    ,
    T['prototype']['setPublic'] = function $_CEE(e, t) {

        null != e && null != t && 0 < e['length'] && 0 < t['length'] ? (this['n'] = function n(e, t) {

            return new b(e,t);
        }(e, 16),
        this['e'] = parseInt(t, 16)) : console && console['error'] && console['error']('Invalid RSA public key');
    }
    ,
    T['prototype']['encrypt'] = function he(e) {
        var t = function a(e, t) {
            if (t < e['length'] + 11)
                return console && console['error'] && console['error']('Message too long for RSA'),
                null;
            var n = []
              , s = e['length'] - 1;
            while (0 <= s && 0 < t) {
                var r = e['charCodeAt'](s--);
                r < 128 ? n[--t] = r : 127 < r && r < 2048 ? (n[--t] = 63 & r | 128,
                n[--t] = r >> 6 | 192) : (n[--t] = 63 & r | 128,
                n[--t] = r >> 6 & 63 | 128,
                n[--t] = r >> 12 | 224);

            }
            n[--t] = 0;
            var i = new l()
              , o = [];
            while (2 < t) {
                o[0] = 0;
                while (0 == o[0])
                    i['nextBytes'](o);
                n[--t] = o[0];
            }
            return n[--t] = 2,
            n[--t] = 0,
            new b(n);
        }(e, this['n']['bitLength']() + 7 >> 3);
        if (null == t)
            return null;
        var n = this['doPublic'](t);
        if (null == n)
            return null;
        var s = n['toString'](16);
        return 0 == (1 & s['length']) ? s : '0' + s;
    }
    ,
    T;
}();
window.r = r
rsa_encrypt = function (s){
    xxx = new window.r()
    return xxx.encrypt(s)
}
e = '{"setLeft":42,"passtime":285,"userresponse":43.75171645945445,"device_id":"5d25317d91fd2c612ee3c2ec316f90b0","lot_number":"464cd61f510b4b8c8d9db9f48f1c5b1e","pow_msg":"1|0|md5|2023-09-04T20:33:48.626884+08:00|54088bb07d2df3c46b79f80300b0abbe|464cd61f510b4b8c8d9db9f48f1c5b1e||b330602732e91368","pow_sign":"7c253d8a5b2ce7b361513c75a140dd8b","geetest":"captcha","lang":"zh","ep":"123","biht":"1426265548","O00n":"WNu0","em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}'

get_s = function (){
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);

}

get_w = function (e){
    s = get_s() + get_s() + get_s() + get_s()
    return aes_encrypt(e,s) + rsa_encrypt(s)
}
// console.log(get_w(e))
console.log(rsa_encrypt('1231231233'))


