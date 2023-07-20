var CryptoJS = require('crypto-js')

window = global;
location = {
    href: 'https://music.163.com/#/discover/toplist'
};
document = {
    createElement: function(a) {
        return a}
};

(function() {
    window.NEJ = window.NEJ || {};
    NEJ.O = {};
    NEJ.R = [];
    NEJ.F = function() {
        return !1
    }
    ;
    NEJ.P = function(GI3x) {
        if (!GI3x || !GI3x.length)
            return null;
        var beE2x = window;
        for (var a = GI3x.split("."), l = a.length, i = a[0] == "window" ? 1 : 0; i < l; beE2x = beE2x[a[i]] = beE2x[a[i]] || {},
        i++)
            ;
        return beE2x
    }
    ;
    NEJ.Q = function(bM6G, GI3x) {
        bM6G = bM6G || NEJ.O;
        var bx6r = GI3x.split(".");
        for (var i = 0, l = bx6r.length; i < l; i++) {
            bM6G = bM6G[bx6r[i]];
            if (!bM6G)
                break
        }
        return bM6G
    }
    ;
    NEJ.C = function() {
        var bBJ7C = function() {
            return NEJ.O.toString.call(arguments[0]) != "[object Function]"
        };
        var bBK7D = function(D5I, bD6x) {
            for (var x in bD6x)
                if (D5I == bD6x[x])
                    return x;
            return null
        };
        var bxR7K = {
            cy6s: 0,
            bn5s: 1,
            bC6w: 2,
            bW6Q: 3,
            bK6E: 4,
            fu7n: 5,
            kO8G: 6,
            ez6t: 7
        }
          , xl1x = {
            cC6w: 0,
            bp5u: 1,
            bH6B: 2,
            cg6a: 3,
            bT6N: 4,
            gS7L: 5,
            lZ8R: 6,
            fV7O: 7
        };
        return function() {
            var ga7T = function() {
                this.bCn7g();
                return this.cy6s.apply(this, arguments)
            };
            ga7T.prototype.bCn7g = NEJ.F;
            ga7T.prototype.cy6s = NEJ.F;
            ga7T.M5R = function(Fs3x, bDm7f) {
                if (bBJ7C(Fs3x))
                    return;
                if (bDm7f == null || !!bDm7f)
                    NEJ.X(this, Fs3x, bBJ7C);
                this.cuF0x = Fs3x;
                this.ct6n = Fs3x.prototype;
                var bL6F = function() {};
                bL6F.prototype = Fs3x.prototype;
                this.prototype = new bL6F;
                var Gb3x = this.prototype;
                Gb3x.constructor = this;
                var cl6f;
                for (var x in bxR7K) {
                    cl6f = bBK7D(bxR7K[x], xl1x);
                    if (!cl6f || !this.ct6n[x])
                        continue;
                    Gb3x[x] = function(Z5e) {
                        return function() {
                            this[Z5e].apply(this, arguments)
                        }
                    }(cl6f)
                }
                var Il7e = {};
                for (var x in xl1x) {
                    cl6f = bBK7D(xl1x[x], bxR7K);
                    if (!cl6f || !this.ct6n[cl6f])
                        continue;
                    Il7e[cl6f] = Fs3x;
                    Gb3x[x] = function(Z5e) {
                        return function() {
                            var m5r, bL6F = this.bpQ4U[Z5e], bij2x = bL6F.prototype[Z5e];
                            this.bpQ4U[Z5e] = bL6F.cuF0x || Fs3x;
                            if (!!bij2x)
                                m5r = bij2x.apply(this, arguments);
                            this.bpQ4U[Z5e] = Fs3x;
                            return m5r
                        }
                    }(cl6f)
                }
                Gb3x.bCn7g = function() {
                    this.bpQ4U = NEJ.X({}, Il7e)
                }
                ;
                Gb3x.cQm3x = Gb3x.cC6w;
                return Gb3x
            }
            ;
            return ga7T
        }
    }();
    NEJ.X = function(gG7z, bU6O, eh6b) {
        if (!gG7z || !bU6O)
            return gG7z;
        eh6b = eh6b || NEJ.F;
        for (var x in bU6O) {
            if (bU6O.hasOwnProperty(x) && !eh6b(bU6O[x], x))
                gG7z[x] = bU6O[x]
        }
        return gG7z
    }
    ;
    NEJ.EX = function(gG7z, bU6O) {
        if (!gG7z || !bU6O)
            return gG7z;
        for (var x in gG7z) {
            if (gG7z.hasOwnProperty(x) && bU6O[x] != null)
                gG7z[x] = bU6O[x]
        }
        return gG7z
    }
    ;
    var NZ9Q = Function.prototype;
    NZ9Q.eO7H = function(lF8x, vm1x) {
        var f = NEJ.F
          , vm1x = vm1x || f
          , lF8x = lF8x || f
          , dE6y = this;
        return function() {
            var d5i = {
                args: NEJ.R.slice.call(arguments, 0)
            };
            lF8x(d5i);
            if (!d5i.stopped) {
                d5i.value = dE6y.apply(this, d5i.args);
                vm1x(d5i)
            }
            return d5i.value
        }
    }
    ;
    NZ9Q.f5k = function() {
        var bm5r = arguments
          , gG7z = arguments[0]
          , bkM3x = this;
        return function() {
            var vl1x = NEJ.R.slice.call(bm5r, 1);
            NEJ.R.push.apply(vl1x, arguments);
            return bkM3x.apply(gG7z || window, vl1x)
        }
    }
    ;
    NZ9Q.eP7I = function() {
        var bm5r = arguments
          , gG7z = NEJ.R.shift.call(bm5r)
          , bkM3x = this;
        return function() {
            NEJ.R.push.apply(arguments, bm5r);
            return bkM3x.apply(gG7z || window, arguments)
        }
    }
    ;
    var NZ9Q = String.prototype;
    if (!NZ9Q.trim) {
        NZ9Q.trim = function() {
            var do6i = /(?:^\s+)|(?:\s+$)/g;
            return function() {
                return this.replace(do6i, "")
            }
        }()
    }
    if (!window.MWF)
        window.MWF = NEJ;
    if (!window.mwf)
        window.mwf = NEJ.P("nej");
    if (!window.console) {
        NEJ.P("console").log = NEJ.F;
        NEJ.P("console").error = NEJ.F
    }
    var lt, gt, amp, nbsp, quot, apos, copy, reg
}
)();

(function() {
    var c5h = NEJ.P
      , bd5i = NEJ.O
      , fD7w = NEJ.R
      , bs5x = NEJ.F
      , a5f = c5h("nej.e")
      , bl5q = c5h("nej.h")
      , j5o = c5h("nej.u");
    window.j5o = j5o;
    var Hb3x = function(i5n, t5y) {
        try {
            t5y = t5y.toLowerCase();
            if (i5n === null)
                return t5y == "null";
            if (i5n === undefined)
                return t5y == "undefined";
            return bd5i.toString.call(i5n).toLowerCase() == "[object " + t5y + "]"
        } catch (e) {
            return !1
        }
    };
    j5o.gV7O = function(i5n) {
        return Hb3x(i5n, "function")
    }
    ;
    j5o.fO7H = function(i5n) {
        return Hb3x(i5n, "string")
    }
    ;
    j5o.tT0x = function(i5n) {
        return Hb3x(i5n, "number")
    }
    ;
    j5o.cMi3x = function(i5n) {
        return Hb3x(i5n, "boolean")
    }
    ;
    j5o.DK2x = function(i5n) {
        return Hb3x(i5n, "date")
    }
    ;
    j5o.ec6W = function(i5n) {
        return Hb3x(i5n, "array")
    }
    ;
    j5o.mi8a = function(i5n) {
        return Hb3x(i5n, "object")
    }
    ;
    j5o.fS7L = function() {
        var do6i = /[^\x00-\xfff]/g;
        return function(bq5v) {
            return ("" + (bq5v || "")).replace(do6i, "**").length
        }
    }();
    j5o.dx6r = function(k5p, q5v) {
        var eh6b = j5o.gV7O(q5v) ? q5v : function(D5I) {
            return D5I === q5v
        }
          , r5w = j5o.eV7O(k5p, eh6b);
        return r5w != null ? r5w : -1
    }
    ;
    j5o.cMh3x = function() {
        var bUU7N;
        var VE0x = function(k5p, pT9K, qe9V) {
            if (pT9K > qe9V)
                return -1;
            var Is7l = Math.ceil((pT9K + qe9V) / 2)
              , m5r = bUU7N(k5p[Is7l], Is7l, k5p);
            if (m5r == 0)
                return Is7l;
            if (m5r < 0)
                return VE0x(k5p, pT9K, Is7l - 1);
            return VE0x(k5p, Is7l + 1, qe9V)
        };
        return function(k5p, Mo8g) {
            bUU7N = Mo8g || bs5x;
            return VE0x(k5p, 0, k5p.length - 1)
        }
    }();
    j5o.ox9o = function(k5p, cH6B, O5T) {
        if (!k5p || !k5p.length || !j5o.gV7O(cH6B))
            return null;
        for (var i = k5p.length - 1; i >= 0; i--)
            if (!!cH6B.call(O5T, k5p[i], i, k5p))
                return i;
        return null
    }
    ;
    j5o.bg5l = function(k5p, cH6B, O5T) {
        if (!k5p || !k5p.length || !j5o.gV7O(cH6B))
            return this;
        if (!!k5p.forEach) {
            k5p.forEach(cH6B, O5T);
            return this
        }
        for (var i = 0, l = k5p.length; i < l; i++)
            cH6B.call(O5T, k5p[i], i, k5p);
        return this
    }
    ;
    j5o.eV7O = function(k5p, cH6B, O5T) {
        if (!k5p || !j5o.gV7O(cH6B))
            return null;
        if (k5p.length != null) {
            if (k5p.length > 0)
                for (var i = 0, l = k5p.length; i < l; i++)
                    if (!!cH6B.call(O5T, k5p[i], i, k5p))
                        return i
        }
        if (j5o.mi8a(k5p)) {
            for (var x in k5p)
                if (k5p.hasOwnProperty(x) && !!cH6B.call(O5T, k5p[x], x, k5p))
                    return x
        }
        return null
    }
    ;
    j5o.cxh1x = function(jI8A, cxi1x, e5j) {
        jI8A = jI8A || [];
        e5j = e5j || bd5i;
        var bVt7m = !!e5j.union
          , yJ1x = !!e5j.begin
          , bbj1x = e5j.compare
          , cyn1x = bVt7m && yJ1x ? j5o.ox9o : j5o.bg5l;
        cyn1x(cxi1x, function(q5v) {
            if (!!bbj1x)
                bbj1x = bbj1x.eP7I(q5v);
            var r5w = j5o.dx6r(jI8A, bbj1x || q5v);
            if (r5w >= 0)
                jI8A.splice(r5w, 1);
            if (bVt7m)
                jI8A[yJ1x ? "unshift" : "push"](q5v)
        });
        return jI8A
    }
    ;
    j5o.Dz2x = function(bD6x, bq5v) {
        if (!bD6x || !bq5v || !bq5v.replace)
            return bq5v || "";
        return bq5v.replace(bD6x.r, function($1) {
            var m5r = bD6x[!bD6x.i ? $1.toLowerCase() : $1];
            return m5r != null ? m5r : $1
        })
    }
    ;
    j5o.dN6H = function() {
        var bD6x = {
            r: /\<|\>|\&lt;|\&gt;|\&|\r|\n|\s|\'|\"/g,
            "<": "&lt;",
            ">": "&gt;",
            "&": "&amp;",
            " ": "&nbsp;",
            '"': "&quot;",
            "'": "&#39;",
            "\n": "<br/>",
            "\r": "",
            "&lt;": "&lt;",
            "&gt;": "&gt;"
        };
        return function(bq5v) {
            return j5o.Dz2x(bD6x, bq5v)
        }
    }();
    j5o.AD2x = function() {
        var bD6x = {
            r: /\&(?:lt|gt|amp|nbsp|#39|quot)\;|\<br\/\>/gi,
            "&lt;": "<",
            "&gt;": ">",
            "&amp;": "&",
            "&nbsp;": " ",
            "&#39;": "'",
            "&quot;": '"',
            "<br/>": "\n"
        };
        return function(bq5v) {
            return j5o.Dz2x(bD6x, bq5v)
        }
    }();
    j5o.id7W = function() {
        var bD6x = {
            i: !0,
            r: /\byyyy|yy|MM|cM|eM|M|dd|d|HH|H|mm|ms|ss|m|s|w|ct|et\b/g
        }
          , czg1x = ["上午", "下午"]
          , czm1x = ["A.M.", "P.M."]
          , blr3x = ["日", "一", "二", "三", "四", "五", "六"]
          , czs1x = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
          , czM1x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
        var Vj0x = function(hq7j) {
            hq7j = parseInt(hq7j) || 0;
            return (hq7j < 10 ? "0" : "") + hq7j
        };
        var cAC1x = function(qJ0x) {
            return qJ0x < 12 ? 0 : 1
        };
        return function(bz6t, KK8C, cAI1x) {
            if (!bz6t || !KK8C)
                return "";
            bz6t = j5o.baI1x(bz6t);
            bD6x.yyyy = bz6t.getFullYear();
            bD6x.yy = ("" + bD6x.yyyy).substr(2);
            bD6x.M = bz6t.getMonth() + 1;
            bD6x.MM = Vj0x(bD6x.M);
            bD6x.eM = czM1x[bD6x.M - 1];
            bD6x.cM = czs1x[bD6x.M - 1];
            bD6x.d = bz6t.getDate();
            bD6x.dd = Vj0x(bD6x.d);
            bD6x.H = bz6t.getHours();
            bD6x.HH = Vj0x(bD6x.H);
            bD6x.m = bz6t.getMinutes();
            bD6x.mm = Vj0x(bD6x.m);
            bD6x.s = bz6t.getSeconds();
            bD6x.ss = Vj0x(bD6x.s);
            bD6x.ms = bz6t.getMilliseconds();
            bD6x.w = blr3x[bz6t.getDay()];
            var bXe7X = cAC1x(bD6x.H);
            bD6x.ct = czg1x[bXe7X];
            bD6x.et = czm1x[bXe7X];
            if (!!cAI1x) {
                bD6x.H = bD6x.H % 12
            }
            return j5o.Dz2x(bD6x, KK8C)
        }
    }();
    j5o.baI1x = function(bz6t) {
        var dj6d = bz6t;
        if (j5o.fO7H(bz6t))
            dj6d = new Date(Date.parse(bz6t));
        if (!j5o.DK2x(bz6t))
            dj6d = new Date(bz6t);
        return dj6d
    }
    ;
    j5o.Or9i = function(cCx1x, cDa1x) {
        return (new Number(cCx1x)).toFixed(cDa1x)
    }
    ;
    j5o.bof4j = function() {
        var he7X = /([^\/:])\/.*$/
          , kG8y = /\/[^\/]+$/
          , FC3x = /[#\?]/
          , bos4w = location.href.split(/[?#]/)[0]
          , uf0x = document.createElement("a");
        var bow4A = function(jE8w) {
            return (jE8w || "").indexOf("://") > 0
        };
        var bXw7p = function(jE8w) {
            return (jE8w || "").split(FC3x)[0].replace(kG8y, "/")
        };
        var cDp2x = function(jE8w, gv7o) {
            if (jE8w.indexOf("/") == 0)
                return gv7o.replace(he7X, "$1") + jE8w;
            return bXw7p(gv7o) + jE8w
        };
        bos4w = bXw7p(bos4w);
        return function(jE8w, gv7o) {
            jE8w = (jE8w || "").trim();
            if (!bow4A(gv7o))
                gv7o = bos4w;
            if (!jE8w)
                return gv7o;
            if (bow4A(jE8w))
                return jE8w;
            jE8w = cDp2x(jE8w, gv7o);
            uf0x.href = jE8w;
            jE8w = uf0x.href;
            return bow4A(jE8w) ? jE8w : uf0x.getAttribute("href", 4)
        }
    }();
    j5o.cFo2x = function() {
        var do6i = /^([\w]+?:\/\/.*?(?=\/|$))/i;
        return function(Y5d) {
            if (do6i.test(Y5d || ""))
                return RegExp.$1.toLowerCase();
            return ""
        }
    }();
    j5o.bYP7I = function(K5P, iE7x) {
        if (!K5P)
            return iE7x;
        var Z5e = K5P.tagName.toLowerCase()
          , k5p = a5f.di6c(K5P);
        if (!k5p || !k5p.length) {
            iE7x[Z5e] = K5P.textContent || K5P.text || "";
            return iE7x
        }
        var cl6f = {};
        iE7x[Z5e] = cl6f;
        j5o.bg5l(k5p, function(g5l) {
            j5o.bYP7I(g5l, cl6f)
        });
        return iE7x
    }
    ;
    j5o.cLc3x = function(Fh3x) {
        try {
            return j5o.bYP7I(a5f.bSs6m(Fh3x), {})
        } catch (ex) {
            return null
        }
    }
    ;
    j5o.UR0x = function(iu7n, UP0x) {
        var iE7x = {};
        j5o.bg5l((iu7n || "").split(UP0x), function(Z5e) {
            var bad1x = Z5e.split("=");
            if (!bad1x || !bad1x.length)
                return;
            var J5O = bad1x.shift();
            if (!J5O)
                return;
            iE7x[decodeURIComponent(J5O)] = decodeURIComponent(bad1x.join("="))
        });
        return iE7x
    }
    ;
    j5o.wf1x = function(gG7z, UP0x, cKY3x) {
        if (!gG7z)
            return "";
        var bx6r = [];
        for (var x in gG7z) {
            bx6r.push(encodeURIComponent(x) + "=" + (!!cKY3x ? encodeURIComponent(gG7z[x]) : gG7z[x]))
        }
        return bx6r.join(UP0x || ",")
    }
    ;
    j5o.hi7b = function(bv5A) {
        return j5o.UR0x(bv5A, "&")
    }
    ;
    j5o.cr6l = function(gG7z) {
        return j5o.wf1x(gG7z, "&", !0)
    }
    ;
    j5o.cLa3x = function(gG7z) {
        return bl5q.KS8K(gG7z)
    }
    ;
    j5o.cNQ3x = function(k5p, eh6b) {
        var m5r = {};
        j5o.bg5l(k5p, function(q5v) {
            var J5O = q5v;
            if (!!eh6b) {
                J5O = eh6b(q5v)
            }
            m5r[J5O] = q5v
        });
        return m5r
    }
    ;
    j5o.cLb3x = function(hq7j, gq7j) {
        var cKT3x = ("" + hq7j).length
          , cKQ3x = Math.max(1, parseInt(gq7j) || 0)
          , dA6u = cKQ3x - cKT3x;
        if (dA6u > 0) {
            hq7j = (new Array(dA6u + 1)).join("0") + hq7j
        }
        return "" + hq7j
    }
    ;
    j5o.ZT1x = function(gG7z, Z5e) {
        if (!j5o.ec6W(Z5e)) {
            try {
                delete gG7z[Z5e]
            } catch (e) {
                gG7z[Z5e] = undefined
            }
            return this
        }
        j5o.bg5l(Z5e, j5o.ZT1x.f5k(j5o, gG7z));
        return this
    }
    ;
    j5o.WS0x = function() {
        var cae7X = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
        return function(bt5y) {
            bt5y = bt5y || 10;
            var m5r = [];
            for (var i = 0, cad7W; i < bt5y; ++i) {
                cad7W = Math.floor(Math.random() * cae7X.length);
                m5r.push(cae7X.charAt(cad7W))
            }
            return m5r.join("")
        }
    }();
    j5o.CV2x = function(fU7N, fB7u) {
        return Math.floor(Math.random() * (fB7u - fU7N) + fU7N)
    }
    ;
    j5o.oQ9H = function(bt5y) {
        bt5y = Math.max(0, Math.min(bt5y || 8, 30));
        var fU7N = Math.pow(10, bt5y - 1)
          , fB7u = fU7N * 10;
        return j5o.CV2x(fU7N, fB7u).toString()
    }
    ;
    j5o.btH6B = function(bJ6D) {
        return Object.assign(bJ6D, {
            result: Object.assign(bJ6D.playlist, {
                tracks: bJ6D.playlist.tracks.map(function(track) {
                    return Object.assign(track, {
                        album: track.al,
                        artists: track.ar,
                        position: track.no,
                        duration: track.dt,
                        disc: track.cd,
                        popularity: track.pop,
                        mvid: track.mv,
                        lMusic: track.l ? {
                            bitrate: track.l.br,
                            volumeDelta: track.l.vd,
                            size: track.l.size,
                            dfsId: track.l.fid
                        } : {},
                        mMusic: track.m ? {
                            bitrate: track.m.br,
                            volumeDelta: track.m.vd,
                            size: track.m.size,
                            dfsId: track.m.fid
                        } : {},
                        hMusic: track.h ? {
                            bitrate: track.h.br,
                            volumeDelta: track.h.vd,
                            size: track.h.size,
                            dfsId: track.h.fid
                        } : {}
                    })
                })
            })
        })
    }
    ;
    j5o.ZK1x = function() {
        var gX7Q = +(new Date);
        return function() {
            return "" + gX7Q++
        }
    }()
}
)();

(function() {
    var c5h = NEJ.P
      , bd5i = NEJ.O
      , P5U = c5h("nej.p")
      // , xB1x = window.navigator.platform
      , xB1x = "Win32"
      // , wb1x = window.navigator.userAgent;
      , wb1x = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    var lV8N = {
        mac: xB1x,
        win: xB1x,
        linux: xB1x,
        ipad: wb1x,
        ipod: wb1x,
        iphone: xB1x,
        android: wb1x
    };
    P5U.LN8F = lV8N;
    for (var x in lV8N)
        lV8N[x] = (new RegExp(x,"i")).test(lV8N[x]);
    lV8N.ios = lV8N.ipad || lV8N.iphone || lV8N.ipod;
    lV8N.tablet = lV8N.ipad;
    lV8N.desktop = lV8N.mac || lV8N.win || lV8N.linux && !lV8N.android;
    var iL7E = {
        engine: "unknow",
        release: "unknow",
        browser: "unknow",
        version: "unknow",
        prefix: {
            css: "",
            pro: "",
            clz: ""
        }
    };
    P5U.dB6v = iL7E;
    if (/msie\s+(.*?);/i.test(wb1x) || /trident\/.+rv:([\d\.]+)/i.test(wb1x)) {
        iL7E.engine = "trident";
        iL7E.browser = "ie";
        iL7E.version = RegExp.$1;
        iL7E.prefix = {
            css: "ms",
            pro: "ms",
            clz: "MS",
            evt: "MS"
        };
        var nt9k = {
            6: "2.0",
            7: "3.0",
            8: "4.0",
            9: "5.0",
            10: "6.0",
            11: "7.0"
        };
        iL7E.release = nt9k[document.documentMode] || nt9k[parseInt(iL7E.version)]
    } else if (/webkit\/?([\d.]+?)(?=\s|$)/i.test(wb1x)) {
        iL7E.engine = "webkit";
        iL7E.release = RegExp.$1 || "";
        iL7E.prefix = {
            css: "webkit",
            pro: "webkit",
            clz: "WebKit"
        }
    } else if (/rv\:(.*?)\)\s+gecko\//i.test(wb1x)) {
        iL7E.engine = "gecko";
        iL7E.release = RegExp.$1 || "";
        iL7E.browser = "firefox";
        iL7E.prefix = {
            css: "Moz",
            pro: "moz",
            clz: "Moz"
        };
        if (/firefox\/(.*?)(?=\s|$)/i.test(wb1x))
            iL7E.version = RegExp.$1 || ""
    } else if (/presto\/(.*?)\s/i.test(wb1x)) {
        iL7E.engine = "presto";
        iL7E.release = RegExp.$1 || "";
        iL7E.browser = "opera";
        iL7E.prefix = {
            css: "O",
            pro: "o",
            clz: "O"
        };
        if (/version\/(.*?)(?=\s|$)/i.test(wb1x))
            iL7E.version = RegExp.$1 || ""
    }
    if (iL7E.browser == "unknow") {
        var nt9k = ["chrome", "maxthon", "safari"];
        for (var i = 0, l = nt9k.length, Z5e; i < l; i++) {
            Z5e = nt9k[i] == "safari" ? "version" : nt9k[i];
            if ((new RegExp(Z5e + "/(.*?)(?=\\s|$)","i")).test(wb1x)) {
                iL7E.browser = nt9k[i];
                iL7E.version = RegExp.$1.trim();
                break
            }
        }
    }
    P5U.bDR8J = {};
    var bhS2x = iL7E.engine != "trident";
    P5U.nX9O = {
        gecko: iL7E.engine != "gecko",
        webkit: iL7E.engine != "webkit",
        presto: iL7E.engine != "presto",
        trident0: bhS2x || iL7E.release > "2.0",
        trident1: bhS2x || iL7E.release < "6.0",
        trident2: bhS2x || iL7E.release > "3.0",
        trident: bhS2x || iL7E.release >= "6.0"
    }
}
)();


!function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();

function RSAKeyPair(a, b, c) {
    this.e = biFromHex(a),
    this.d = biFromHex(b),
    this.m = biFromHex(c),
    this.chunkSize = 2 * biHighIndex(this.m),
    this.radix = 16,
    this.barrett = new BarrettMu(this.m)
}
function BigInt(a) {
    this.digits = "boolean" == typeof a && 1 == a ? null : ZERO_ARRAY.slice(0),
    this.isNeg = !1
}
function setMaxDigits(a) {
    maxDigits = a,
    ZERO_ARRAY = new Array(maxDigits);
    for (var b = 0; b < ZERO_ARRAY.length; b++)
        ZERO_ARRAY[b] = 0;
    bigZero = new BigInt,
    bigOne = new BigInt,
    bigOne.digits[0] = 1
}
function biFromHex(a) {
    var d, e, b = new BigInt, c = a.length;
    for (d = c,
    e = 0; d > 0; d -= 4,
    ++e)
        b.digits[e] = hexToDigit(a.substr(Math.max(d - 4, 0), Math.min(d, 4)));
    return b
}
function hexToDigit(a) {
    var d, b = 0, c = Math.min(a.length, 4);
    for (d = 0; c > d; ++d)
        b <<= 4,
        b |= charToHex(a.charCodeAt(d));
    return b
}
function charToHex(a) {
    var h, b = 48, c = b + 9, d = 97, e = d + 25, f = 65, g = 90;
    return h = a >= b && c >= a ? a - b : a >= f && g >= a ? 10 + a - f : a >= d && e >= a ? 10 + a - d : 0
}
function biHighIndex(a) {
    for (var b = a.digits.length - 1; b > 0 && 0 == a.digits[b]; )
        --b;
    return b
}
function BarrettMu(a) {
    this.modulus = biCopy(a),
    this.k = biHighIndex(this.modulus) + 1;
    var b = new BigInt;
    b.digits[2 * this.k] = 1,
    this.mu = biDivide(b, this.modulus),
    this.bkplus1 = new BigInt,
    this.bkplus1.digits[this.k + 1] = 1,
    this.modulo = BarrettMu_modulo,
    this.multiplyMod = BarrettMu_multiplyMod,
    this.powMod = BarrettMu_powMod
}
function biCopy(a) {
    var b = new BigInt(!0);
    return b.digits = a.digits.slice(0),
    b.isNeg = a.isNeg,
    b
}
function biDivide(a, b) {
    return biDivideModulo(a, b)[0]
}
function biDivideModulo(a, b) {
    var f, g, h, i, j, k, l, m, n, o, p, q, r, s, c = biNumBits(a), d = biNumBits(b), e = b.isNeg;
    if (d > c)
        return a.isNeg ? (f = biCopy(bigOne),
        f.isNeg = !b.isNeg,
        a.isNeg = !1,
        b.isNeg = !1,
        g = biSubtract(b, a),
        a.isNeg = !0,
        b.isNeg = e) : (f = new BigInt,
        g = biCopy(a)),
        new Array(f,g);
    for (f = new BigInt,
    g = a,
    h = Math.ceil(d / bitsPerDigit) - 1,
    i = 0; b.digits[h] < biHalfRadix; )
        b = biShiftLeft(b, 1),
        ++i,
        ++d,
        h = Math.ceil(d / bitsPerDigit) - 1;
    for (g = biShiftLeft(g, i),
    c += i,
    j = Math.ceil(c / bitsPerDigit) - 1,
    k = biMultiplyByRadixPower(b, j - h); -1 != biCompare(g, k); )
        ++f.digits[j - h],
        g = biSubtract(g, k);
    for (l = j; l > h; --l) {
        for (m = l >= g.digits.length ? 0 : g.digits[l],
        n = l - 1 >= g.digits.length ? 0 : g.digits[l - 1],
        o = l - 2 >= g.digits.length ? 0 : g.digits[l - 2],
        p = h >= b.digits.length ? 0 : b.digits[h],
        q = h - 1 >= b.digits.length ? 0 : b.digits[h - 1],
        f.digits[l - h - 1] = m == p ? maxDigitVal : Math.floor((m * biRadix + n) / p),
        r = f.digits[l - h - 1] * (p * biRadix + q),
        s = m * biRadixSquared + (n * biRadix + o); r > s; )
            --f.digits[l - h - 1],
            r = f.digits[l - h - 1] * (p * biRadix | q),
            s = m * biRadix * biRadix + (n * biRadix + o);
        k = biMultiplyByRadixPower(b, l - h - 1),
        g = biSubtract(g, biMultiplyDigit(k, f.digits[l - h - 1])),
        g.isNeg && (g = biAdd(g, k),
        --f.digits[l - h - 1])
    }
    return g = biShiftRight(g, i),
    f.isNeg = a.isNeg != e,
    a.isNeg && (f = e ? biAdd(f, bigOne) : biSubtract(f, bigOne),
    b = biShiftRight(b, i),
    g = biSubtract(b, g)),
    0 == g.digits[0] && 0 == biHighIndex(g) && (g.isNeg = !1),
    new Array(f,g)
}
function biNumBits(a) {
    var e, b = biHighIndex(a), c = a.digits[b], d = (b + 1) * bitsPerDigit;
    for (e = d; e > d - bitsPerDigit && 0 == (32768 & c); --e)
        c <<= 1;
    return e
}
bitsPerDigit = 16
biHalfRadix = 32768
function biShiftLeft(a, b) {
    var e, f, g, h, c = Math.floor(b / bitsPerDigit), d = new BigInt;
    for (arrayCopy(a.digits, 0, d.digits, c, d.digits.length - c),
    e = b % bitsPerDigit,
    f = bitsPerDigit - e,
    g = d.digits.length - 1,
    h = g - 1; g > 0; --g,
    --h)
        d.digits[g] = d.digits[g] << e & maxDigitVal | (d.digits[h] & highBitMasks[e]) >>> f;
    return d.digits[0] = d.digits[g] << e & maxDigitVal,
    d.isNeg = a.isNeg,
    d
}
function arrayCopy(a, b, c, d, e) {
    var g, h, f = Math.min(b + e, a.length);
    for (g = b,
    h = d; f > g; ++g,
    ++h)
        c[h] = a[g]
}
maxDigitVal = 65535
highBitMasks = [
    0,
    32768,
    49152,
    57344,
    61440,
    63488,
    64512,
    65024,
    65280,
    65408,
    65472,
    65504,
    65520,
    65528,
    65532,
    65534,
    65535
]
function biMultiplyByRadixPower(a, b) {
    var c = new BigInt;
    return arrayCopy(a.digits, 0, c.digits, b, c.digits.length - b),
    c
}
function biCompare(a, b) {
    if (a.isNeg != b.isNeg)
        return 1 - 2 * Number(a.isNeg);
    for (var c = a.digits.length - 1; c >= 0; --c)
        if (a.digits[c] != b.digits[c])
            return a.isNeg ? 1 - 2 * Number(a.digits[c] > b.digits[c]) : 1 - 2 * Number(a.digits[c] < b.digits[c]);
    return 0
}
biRadix = 65536
biRadixSquared = 4294967296
function biSubtract(a, b) {
    var c, d, e, f;
    if (a.isNeg != b.isNeg)
        b.isNeg = !b.isNeg,
        c = biAdd(a, b),
        b.isNeg = !b.isNeg;
    else {
        for (c = new BigInt,
        e = 0,
        f = 0; f < a.digits.length; ++f)
            d = a.digits[f] - b.digits[f] + e,
            c.digits[f] = 65535 & d,
            c.digits[f] < 0 && (c.digits[f] += biRadix),
            e = 0 - Number(0 > d);
        if (-1 == e) {
            for (e = 0,
            f = 0; f < a.digits.length; ++f)
                d = 0 - c.digits[f] + e,
                c.digits[f] = 65535 & d,
                c.digits[f] < 0 && (c.digits[f] += biRadix),
                e = 0 - Number(0 > d);
            c.isNeg = !a.isNeg
        } else
            c.isNeg = a.isNeg
    }
    return c
}
function biMultiplyDigit(a, b) {
    var c, d, e, f;
    for (result = new BigInt,
    c = biHighIndex(a),
    d = 0,
    f = 0; c >= f; ++f)
        e = result.digits[f] + a.digits[f] * b + d,
        result.digits[f] = e & maxDigitVal,
        d = e >>> biRadixBits;
    return result.digits[1 + c] = d,
    result
}
biRadixBits = 16
function biShiftRight(a, b) {
    var e, f, g, h, c = Math.floor(b / bitsPerDigit), d = new BigInt;
    for (arrayCopy(a.digits, c, d.digits, 0, a.digits.length - c),
    e = b % bitsPerDigit,
    f = bitsPerDigit - e,
    g = 0,
    h = g + 1; g < d.digits.length - 1; ++g,
    ++h)
        d.digits[g] = d.digits[g] >>> e | (d.digits[h] & lowBitMasks[e]) << f;
    return d.digits[d.digits.length - 1] >>>= e,
    d.isNeg = a.isNeg,
    d
}
lowBitMasks = [
    0,
    1,
    3,
    7,
    15,
    31,
    63,
    127,
    255,
    511,
    1023,
    2047,
    4095,
    8191,
    16383,
    32767,
    65535
]
function BarrettMu_modulo(a) {
    var i, b = biDivideByRadixPower(a, this.k - 1), c = biMultiply(b, this.mu), d = biDivideByRadixPower(c, this.k + 1), e = biModuloByRadixPower(a, this.k + 1), f = biMultiply(d, this.modulus), g = biModuloByRadixPower(f, this.k + 1), h = biSubtract(e, g);
    for (h.isNeg && (h = biAdd(h, this.bkplus1)),
    i = biCompare(h, this.modulus) >= 0; i; )
        h = biSubtract(h, this.modulus),
        i = biCompare(h, this.modulus) >= 0;
    return h
}
function BarrettMu_multiplyMod(a, b) {
    var c = biMultiply(a, b);
    return this.modulo(c)
}
function BarrettMu_powMod(a, b) {
    var d, e, c = new BigInt;
    for (c.digits[0] = 1,
    d = a,
    e = b; ; ) {
        if (0 != (1 & e.digits[0]) && (c = this.multiplyMod(c, d)),
        e = biShiftRight(e, 1),
        0 == e.digits[0] && 0 == biHighIndex(e))
            break;
        d = this.multiplyMod(d, d)
    }
    return c
}
function encryptedString(a, b) {
    for (var f, g, h, i, j, k, l, c = new Array, d = b.length, e = 0; d > e; )
        c[e] = b.charCodeAt(e),
        e++;
    for (; 0 != c.length % a.chunkSize; )
        c[e++] = 0;
    for (f = c.length,
    g = "",
    e = 0; f > e; e += a.chunkSize) {
        for (j = new BigInt,
        h = 0,
        i = e; i < e + a.chunkSize; ++h)
            j.digits[h] = c[i++],
            j.digits[h] += c[i++] << 8;
        k = a.barrett.powMod(j, a.e),
        l = 16 == a.radix ? biToHex(k) : biToString(k, a.radix),
        g += l + " "
    }
    return g.substring(0, g.length - 1)
}
function biMultiply(a, b) {
    var d, h, i, k, c = new BigInt, e = biHighIndex(a), f = biHighIndex(b);
    for (k = 0; f >= k; ++k) {
        for (d = 0,
        i = k,
        j = 0; e >= j; ++j,
        ++i)
            h = c.digits[i] + a.digits[j] * b.digits[k] + d,
            c.digits[i] = h & maxDigitVal,
            d = h >>> biRadixBits;
        c.digits[k + e + 1] = d
    }
    return c.isNeg = a.isNeg != b.isNeg,
    c
}
function biDivideByRadixPower(a, b) {
    var c = new BigInt;
    return arrayCopy(a.digits, b, c.digits, 0, c.digits.length - b),
    c
}
function biModuloByRadixPower(a, b) {
    var c = new BigInt;
    return arrayCopy(a.digits, 0, c.digits, 0, b),
    c
}
function biToHex(a) {
    var d, b = "";
    for (biHighIndex(a),
    d = biHighIndex(a); d > -1; --d)
        b += digitToHex(a.digits[d]);
    return b
}
function digitToHex(a) {
    var b = 15
      , c = "";
    for (i = 0; 4 > i; ++i)
        c += hexToChar[a & b],
        a >>>= 4;
    return reverseStr(c)
}
hexToChar = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f"
]
function reverseStr(a) {
    var c, b = "";
    for (c = a.length - 1; c > -1; --c)
        b += a.charAt(c);
    return b
}



Vx0x = {
    "emj": {
        "色": "00e0b",
        "流感": "509f6",
        "这边": "259df",
        "弱": "8642d",
        "嘴唇": "bc356",
        "亲": "62901",
        "开心": "477df",
        "呲牙": "22677",
        "憨笑": "ec152",
        "猫": "b5ff6",
        "皱眉": "8ace6",
        "幽灵": "15bb7",
        "蛋糕": "b7251",
        "发怒": "52b3a",
        "大哭": "b17a8",
        "兔子": "76aea",
        "星星": "8a5aa",
        "钟情": "76d2e",
        "牵手": "41762",
        "公鸡": "9ec4e",
        "爱意": "e341f",
        "禁止": "56135",
        "狗": "fccf6",
        "亲亲": "95280",
        "叉": "104e0",
        "礼物": "312ec",
        "晕": "bda92",
        "呆": "557c9",
        "生病": "38701",
        "钻石": "14af6",
        "拜": "c9d05",
        "怒": "c4f7f",
        "示爱": "0c368",
        "汗": "5b7a4",
        "小鸡": "6bee2",
        "痛苦": "55932",
        "撇嘴": "575cc",
        "惶恐": "e10b4",
        "口罩": "24d81",
        "吐舌": "3cfe4",
        "心碎": "875d3",
        "生气": "e8204",
        "可爱": "7b97d",
        "鬼脸": "def52",
        "跳舞": "741d5",
        "男孩": "46b8e",
        "奸笑": "289dc",
        "猪": "6935b",
        "圈": "3ece0",
        "便便": "462db",
        "外星": "0a22b",
        "圣诞": "8e7",
        "流泪": "01000",
        "强": "1",
        "爱心": "0CoJU",
        "女孩": "m6Qyw",
        "惊恐": "8W8ju",
        "大笑": "d"
    },
    "md": [
        "色",
        "流感",
        "这边",
        "弱",
        "嘴唇",
        "亲",
        "开心",
        "呲牙",
        "憨笑",
        "猫",
        "皱眉",
        "幽灵",
        "蛋糕",
        "发怒",
        "大哭",
        "兔子",
        "星星",
        "钟情",
        "牵手",
        "公鸡",
        "爱意",
        "禁止",
        "狗",
        "亲亲",
        "叉",
        "礼物",
        "晕",
        "呆",
        "生病",
        "钻石",
        "拜",
        "怒",
        "示爱",
        "汗",
        "小鸡",
        "痛苦",
        "撇嘴",
        "惶恐",
        "口罩",
        "吐舌",
        "心碎",
        "生气",
        "可爱",
        "鬼脸",
        "跳舞",
        "男孩",
        "奸笑",
        "猪",
        "圈",
        "便便",
        "外星",
        "圣诞"
    ]
}

var bsk5p = function(cxN1x) {
        var m5r = [];
        window.j5o.bg5l(cxN1x, function(cxM1x) {
            m5r.push(Vx0x.emj[cxM1x])
        });
        return m5r.join("")
    };

data = data = {
    "ids": "[2062885837,]",
    "level": "standard",
    "encodeType": "aac",
    "csrf_token": ""
}
gpss = function (data){
    var a = window.asrsea(JSON.stringify(data), bsk5p(["流泪", "强"]), bsk5p(Vx0x.md), bsk5p(["爱心", "女孩", "惊恐", "大笑"]))
    return a

}
console.log(window.asrsea(JSON.stringify(data), bsk5p(["流泪", "强"]), bsk5p(Vx0x.md), bsk5p(["爱心", "女孩", "惊恐", "大笑"])))
