# mytokencap

网站地址：aHR0cHM6Ly93d3cubXl0b2tlbmNhcC5jb20v

https://github.com/Guapisansan/gpss_learn_reverse 代码在这里，会持续更新逆向案例

![image-20230720184243602](./mytokencap.assets/image-20230720184243602.png)

获取这部分数据

## 分析请求

对页面进行抓包，进行搜索 关键字，发现接口

currencylistforall 里有我们要的数据

![image-20230720184836698](./mytokencap.assets/image-20230720184836698.png)

查看请求参数：

![image-20230720184941859](./mytokencap.assets/image-20230720184941859.png)

这里 大部分参数都好理解， 页数，数量，版本，时间戳

只有code是加密的。

先模拟一下看看能不能顺利请求成功。

![image-20230720185144669](./mytokencap.assets/image-20230720185144669.png)

测试一下发现 站点不需要cookie 和headers

所以只要搞定code因该就没问题了，

### code逆向

尝试搜索code，发现数量太多了

![image-20230720185303225](./mytokencap.assets/image-20230720185303225.png)

还是下xhr断点吧

****

![image-20230720185742736](./mytokencap.assets/image-20230720185742736.png)

这里 是最后发起即将发送的位置，往前跟栈

![image-20230720185936766](./mytokencap.assets/image-20230720185936766.png)

跟栈到这里，异步加载，里面可能会有加密

![image-20230721101403896](./mytokencap.assets/image-20230721101403896.png)

这个 n 和 t

n是Promise 对象 t这个数组有五个函数一个undfiend



![image-20230721102356866](./mytokencap.assets/image-20230721102356866.png)

promise是一个异步编程的解决方案，这里通过

promise.then来对异步状态进行处理，

![image-20230721105709143](./mytokencap.assets/image-20230721105709143.png)

> https://es6.ruanyifeng.com/#docs/promise

感兴趣的可以详细了解一下，

所以t数组里的方法对我们来说就很重要，要跟进去看看，

![image-20230721110005095](./mytokencap.assets/image-20230721110005095.png)

进入t数组的第一个方法，就发现了关于code加密的信息，下断点根植

![image-20230721110243644](./mytokencap.assets/image-20230721110243644.png)

发现 ，由o函数对 时间戳进行加密 o的参数是 时间戳＋9527 + 时间戳前六位

![image-20230721112333267](./mytokencap.assets/image-20230721112333267.png)

跟进o函数看看：

![image-20230721112511676](./mytokencap.assets/image-20230721112511676.png)

仔细分析，

e是传进来的时间戳，n是undefined，

先通过 a函数拿到数组，再通过t.wordsToBytes在生成数组

经过表达式测试最后通过 t.bytesToHe 生成加密字符.

![image-20230721112729953](./mytokencap.assets/image-20230721112729953.png)

### 扣代码

分析好了，接下来就是实现过程，将加密代码扣下来，一个一个扣

先从a开始

![image-20230721113053141](./mytokencap.assets/image-20230721113053141.png)

扣下来，放到node中执行

![image-20230721113241666](./mytokencap.assets/image-20230721113241666.png)

缺少r ，但是主要是缺少r的 r.stringToBytes 方法，我们找到补上再次执行。

![image-20230721113356268](./mytokencap.assets/image-20230721113356268.png)

复制下来

![image-20230721113528582](./mytokencap.assets/image-20230721113528582.png)

发现没有t 

![image-20230721113555299](./mytokencap.assets/image-20230721113555299.png)

将这个函数整理一下，错误换成了缺少另一个函数，

![image-20230721113833565](./mytokencap.assets/image-20230721113833565.png)

找到，补到代码中

![image-20230721113932678](./mytokencap.assets/image-20230721113932678.png)

![image-20230721114027811](./mytokencap.assets/image-20230721114027811.png)

缺少h，再次补一下h

![image-20230721114053914](./mytokencap.assets/image-20230721114053914.png)

![image-20230721114109705](./mytokencap.assets/image-20230721114109705.png)

将这里的代码补一下，再次执行

![image-20230721114152148](./mytokencap.assets/image-20230721114152148.png)

缺少t的endian方法，

![image-20230721114250085](./mytokencap.assets/image-20230721114250085.png)

上面写了t但是明显不是一个对象中，只有单个函数可以改写成

![image-20230721114831065](./mytokencap.assets/image-20230721114831065.png)

![image-20230721114845125](./mytokencap.assets/image-20230721114845125.png)

调用位置也换一下，再次执行

![image-20230721114915690](./mytokencap.assets/image-20230721114915690.png)

缺少n.rotl

补一下

![image-20230721114948175](./mytokencap.assets/image-20230721114948175.png)

再次执行，发现结果已经出现

![image-20230721115034056](./mytokencap.assets/image-20230721115034056.png)

和页面的参数一样

![image-20230721115049988](./mytokencap.assets/image-20230721115049988.png)

a就搞定了，再看 t.wordsToBytes

![image-20230721115138149](./mytokencap.assets/image-20230721115138149.png)

将这个函数复制下来，名字去掉了，t. 这里可以灵活运用，只有执行通过就行

![image-20230721115252536](./mytokencap.assets/image-20230721115252536.png)

这里输出结果也正确，看最后一个

t.bytesToHex

![image-20230721115442431](./mytokencap.assets/image-20230721115442431.png)

直接搬下来，code的加密参数已经得到了。

## 总结

异步定位到加密点，需要一些经验，

扣函数，要灵活运用，只要可以执行通过就可以，不用太纠结函数名称，

封装一下，方便吊用

![image-20230721115923570](./mytokencap.assets/image-20230721115923570.png)

模拟运行一下吧

![image-20230721143250155](./mytokencap.assets/image-20230721143250155.png)