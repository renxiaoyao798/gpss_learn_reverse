window = this;
function H(t, e) {
    // t 滑动距离 e challenge
    // userresponse
    for (var n = e['slice'](-2), r = [], i = 0; i < n['length']; i++) {
        var o = n['charCodeAt'](i);
        r[i] = 57 < o ? o - 87 : o - 48;
    }
    n = 36 * r[0] + r[1];
    var s, a = Math['round'](t) + n, _ = [[], [], [], [], []], c = {}, u = 0;
    i = 0;
    for (var l = (e = e['slice'](0, -2))['length']; i < l; i++)
        c[s = e['charAt'](i)] || (c[s] = 1,
        _[u]['push'](s),
        u = 5 == ++u ? 0 : u);
    var h, f = a, d = 4, p = '', g = [1, 2, 5, 10, 50];
    while (0 < f)
        0 <= f - g[d] ? (h = parseInt(Math['random']() * _[d]['length'], 10),
        p += _[d][h],
        f -= g[d]) : (_['splice'](d, 1),
        g['splice'](d, 1),
        d -= 1);
    return p;
 }
 // console.log(H(31, 'ef8f27d4f2821d8f4de93eeebf148bb56h'))

function ct(t) {

    this['$_BCAc'] = t || [];

}
ct['prototype'] = {
            "\u0024\u005f\u0048\u0042\u004c": function(t) {

                return this[$_BFCFG(474)][t];
            },
            "\u0024\u005f\u0042\u0043\u0043\u004a": function() {

                return this[$_BFCJV(474)][$_BFCJV(159)];
            },
            "\u0024\u005f\u0042\u004a\u0072": function(t, e) {

                return new ct(Q(e) ? this[$_BFDFf(474)][$_BFDFf(195)](t, e) : this[$_BFDER(474)][$_BFDFf(195)](t));
            },
            "\u0024\u005f\u0042\u0043\u0044\u0071": function(t) {

                return this[$_BFDJE(474)][$_BFEAL(105)](t),
                this;
            },
            "\u0024\u005f\u0042\u0043\u0045\u004e": function(t, e) {

                return this[$_BFEEy(474)][$_BFEEy(166)](t, e || 1);
            },
            "\u0024\u005f\u0043\u0042\u0058": function(t) {

                return this[$_BFFAF(474)][$_BFFAF(415)](t);
            },
            "\u0024\u005f\u0042\u0043\u0046\u0061": function(t) {

                return new ct(this[$_BFFEa(474)][$_BFFEa(370)](t));
            },
            "\u0024\u005f\u0043\u0041\u0064": function(t) {

                var e = this['$_BCAc'];
                if (e['map'])
                    return new ct(e['map'](t));
                for (var n = [], r = 0, i = e['length']; r < i; r += 1)
                    n[r] = t(e[r], r, this);
                return new ct(n);
            },
            "\u0024\u005f\u0042\u0043\u0047\u004a": function(t) {

                var e = this[$_BFGEc(474)];
                if (e[$_BFGFv(475)])
                    return new ct(e[$_BFGEc(475)](t));
                for (var n = [], r = 0, i = e[$_BFGEc(159)]; r < i; r += 1)
                    t(e[r], r, this) && n[$_BFGEc(105)](e[r]);
                return new ct(n);
            },
            "\u0024\u005f\u0042\u0043\u0048\u0045": function(t) {

                var e = this[$_BFHAP(474)];
                if (e[$_BFGJj(137)])
                    return e[$_BFHAP(137)](t);
                for (var n = 0, r = e[$_BFGJj(159)]; n < r; n += 1)
                    if (e[n] === t)
                        return n;
                return -1;
            },
            "\u0024\u005f\u0042\u0043\u0049\u0047": function(t) {

                var e = this[$_BFHFA(474)];
                if (!e[$_BFHFA(438)])
                    for (var n = arguments[1], r = 0; r < e[$_BFHFA(159)]; r++)
                        r in e && t[$_BFHEm(375)](n, e[r], r, this);
                return e[$_BFHEm(438)](t);
            }
        },
        ct['$_BBJT'] = function(t) {
            var $_BFHJA = _tkts.$_Ch
              , $_BFHIt = ['$_BFICC'].concat($_BFHJA)
              , $_BFIAk = $_BFHIt[1];
            $_BFHIt.shift();
            var $_BFIBn = $_BFHIt[0];
            return Array[$_BFIAk(473)] ? Array[$_BFHJA(473)](t) : $_BFIAk(463) === Object[$_BFIAk(269)][$_BFIAk(206)][$_BFHJA(375)](t);
        }
get_l_param_one = function(guijie_array) {

                function n(t) {

                            var e = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
                              , n = e['length']
                              , r = ''
                              , i = Math['abs'](t)
                              , o = parseInt(i / n);
                            n <= o && (o = n - 1),
                            o && (r = e['charAt'](o));
                            var s = '';
                            return t < 0 && (s += '!'),
                            r && (s += '$'),
                            s + r + e['charAt'](i %= n);

                }
                var t = function(t) {

                    for (var e, n, r, i = [], o = 0, s = 0, a = t['length'] - 1; s < a; s++)
                        e = Math['round'](t[s + 1][0] - t[s][0]),
                        n = Math['round'](t[s + 1][1] - t[s][1]),
                        r = Math['round'](t[s + 1][2] - t[s][2]),
                        0 == e && 0 == n && 0 == r || (0 == e && 0 == n ? o += r : (i['push']([e, n, r + o]),
                        o = 0));
                    return 0 !== o && i['push']([e, n, o]),
                    i;
                }(guijie_array)
                  , r = []
                  , i = []
                  , o = [];
                return new ct(t)['$_CAd'](function(t) {

                    var e = function(t) {
                        for (var e = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], n = 0, r = e['length']; n < r; n++)
                            if (t[0] == e[n][0] && t[1] == e[n][1])
                                return 'stuvwxyz~'[n];
                        return 0;
                    }(t);
                    e ? i['push'](e) : (r['push'](n(t[0])),
                    i['push'](n(t[1]))),
                    o['push'](n(t[2]));
                }),
                r['join']('') + '!!' + i['join']('') + '!!' + o['join']('');
            }

get_l = function(t, e, n) {

                if (!e || !n)
                    return t;
                var r, i = 0, o = t, s = e[0], a = e[2], _ = e[4];
                while (r = n['substr'](i, 2)) {
                    i += 2;
                    var c = parseInt(r, 16)
                      , u = String['fromCharCode'](c)
                      , l = (s * c * c + a * c + _) % t['length'];
                    o = o['substr'](0, l) + u + o['substr'](l);
                }
                return o;
            }
function bt() {
        }
bt['prototype'] = {
    "\u0024\u005f\u0042\u0047\u0047\u0063": function() {

        return window['performance'] && window['prototype']['timing'] && this['$_BGHY']() || -1;
    },
    "\u0024\u005f\u0042\u0047\u0048\u0059": function() {
        var $_BJBJu = _tkts.$_Ch
          , $_BJBIb = ['$_BJCCh'].concat($_BJBJu)
          , $_BJCAr = $_BJBIb[1];
        $_BJBIb.shift();
        var $_BJCBx = $_BJBIb[0];
        var t = window[$_BJCAr(688)][$_BJBJu(624)];
        return {
            "\u0061": t[$_BJBJu(635)],
            "\u0062": t[$_BJCAr(696)],
            "\u0063": t[$_BJCAr(650)],
            "\u0064": t[$_BJCAr(684)],
            "\u0065": t[$_BJCAr(629)],
            "\u0066": t[$_BJBJu(645)],
            "\u0067": t[$_BJCAr(638)],
            "\u0068": t[$_BJCAr(678)],
            "\u0069": t[$_BJCAr(655)],
            "\u006a": t[$_BJCAr(603)],
            "\u006b": t[$_BJBJu(680)],
            "\u006c": t[$_BJBJu(659)],
            "\u006d": t[$_BJBJu(658)],
            "\u006e": t[$_BJBJu(602)],
            "\u006f": t[$_BJBJu(664)],
            "\u0070": t[$_BJBJu(630)],
            "\u0071": t[$_BJCAr(673)],
            "\u0072": t[$_BJCAr(651)],
            "\u0073": t[$_BJBJu(686)],
            "\u0074": t[$_BJCAr(617)],
            "\u0075": t[$_BJCAr(670)]
        };
    }
};
get_ep = function() {
                wt = {
                    "mouseEvent": true,
                    "touchEvent": false
                }
                return {
                    "\u0076": '7.9.0',
                    "\u0024\u005f\u0042\u0049\u006f": wt['touchEvent'],
                    "\u006d\u0065": wt['mouseEvent'],
                    "\u0074\u006d": new bt()['$_BGGc'](),
                    "\u0074\u0064": this['td'] || -1
                };
            }

guiji = [
    [
        -35,
        -26,
        0
    ],
    [
        0,
        0,
        0
    ],
    [
        0,
        0,
        3
    ],
    [
        1,
        0,
        48
    ],
    [
        2,
        0,
        54
    ],
    [
        3,
        0,
        56
    ],
    [
        4,
        0,
        60
    ],
    [
        5,
        0,
        64
    ],
    [
        7,
        0,
        66
    ],
    [
        8,
        0,
        71
    ],
    [
        10,
        0,
        72
    ],
    [
        12,
        0,
        74
    ],
    [
        14,
        0,
        78
    ],
    [
        16,
        0,
        80
    ],
    [
        17,
        0,
        82
    ],
    [
        19,
        0,
        84
    ],
    [
        21,
        0,
        86
    ],
    [
        22,
        0,
        88
    ],
    [
        24,
        -1,
        90
    ],
    [
        26,
        -1,
        92
    ],
    [
        27,
        -1,
        94
    ],
    [
        29,
        -1,
        96
    ],
    [
        31,
        -1,
        98
    ],
    [
        32,
        -1,
        100
    ],
    [
        34,
        -1,
        103
    ],
    [
        36,
        -1,
        104
    ],
    [
        38,
        -1,
        108
    ],
    [
        40,
        -1,
        110
    ],
    [
        41,
        -1,
        114
    ],
    [
        44,
        -1,
        116
    ],
    [
        45,
        -1,
        119
    ],
    [
        46,
        -1,
        122
    ],
    [
        47,
        -1,
        124
    ],
    [
        50,
        -1,
        126
    ],
    [
        51,
        -1,
        132
    ],
    [
        52,
        -2,
        134
    ],
    [
        53,
        -2,
        137
    ],
    [
        54,
        -2,
        139
    ],
    [
        55,
        -2,
        148
    ],
    [
        56,
        -2,
        199
    ],
    [
        57,
        -2,
        201
    ],
    [
        58,
        -2,
        204
    ],
    [
        59,
        -2,
        210
    ],
    [
        61,
        -2,
        216
    ],
    [
        62,
        -2,
        226
    ],
    [
        63,
        -2,
        235
    ],
    [
        64,
        -2,
        244
    ],
    [
        65,
        -2,
        250
    ],
    [
        66,
        -2,
        410
    ],
    [
        67,
        -2,
        421
    ],
    [
        68,
        -2,
        424
    ],
    [
        69,
        -2,
        428
    ],
    [
        70,
        -2,
        438
    ],
    [
        71,
        -2,
        440
    ],
    [
        72,
        -2,
        442
    ],
    [
        73,
        -2,
        446
    ],
    [
        74,
        -2,
        448
    ],
    [
        75,
        -2,
        452
    ],
    [
        76,
        -2,
        454
    ],
    [
        77,
        -2,
        458
    ],
    [
        78,
        -2,
        460
    ],
    [
        79,
        -1,
        462
    ],
    [
        80,
        -1,
        464
    ],
    [
        81,
        -1,
        466
    ],
    [
        82,
        -1,
        469
    ],
    [
        83,
        -1,
        470
    ],
    [
        84,
        -1,
        472
    ],
    [
        86,
        -1,
        474
    ],
    [
        87,
        -1,
        476
    ],
    [
        89,
        -1,
        480
    ],
    [
        90,
        -1,
        484
    ],
    [
        91,
        -1,
        485
    ],
    [
        92,
        -1,
        486
    ],
    [
        93,
        -1,
        490
    ],
    [
        95,
        -1,
        494
    ],
    [
        97,
        -1,
        503
    ],
    [
        98,
        -1,
        508
    ],
    [
        98,
        -1,
        797
    ]
]
get_aes_params = function (guiji, t,gt, challenge, slice_time, s){
    var ep = {
    "v": "7.9.0",
    "$_BIo": false,
    "me": true,
    "tm": {
        "a": 1694082864383,
        "b": 1694082864697,
        "c": 1694082864706,
        "d": 0,
        "e": 0,
        "f": 1694082864392,
        "g": 1694082864399,
        "h": 1694082864401,
        "i": 1694082864401,
        "j": 1694082864468,
        "k": 1694082864423,
        "l": 1694082864469,
        "m": 1694082864693,
        "n": 1694082864697,
        "o": 1694082864713,
        "p": 1694082864937,
        "q": 1694082864937,
        "r": 1694082864938,
        "s": 1694082866072,
        "t": 1694082866073,
        "u": 1694082866073
    },
    "td": -1
}

    data = {
        'lang': 'zh-cn',
        'userresponse': H(t, challenge),
        'passtime': slice_time,
        'imgload': 30,
        'aa': get_l(get_l_param_one(guiji), [
    12,
    58,
    98,
    36,
    43,
    95,
    62,
    15,
    12
], s), // 后两个参数写死了
        "h9s9": "1816378497",
        "rp": gt + challenge.slice(0,32) + slice_time,
        // 'ep': get_ep()
        'ep': ep
    }
    return data
}
// console.log(get_aes_params(guiji,))

