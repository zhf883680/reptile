var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var request = require('request')

// 创建 application/x-www-form-urlencoded 编码解析
var urlencodedParser = bodyParser.urlencoded({
    extended: false
})

app.use(express.static('public'));//访问public目录下文件
//路由设置
app.get('/index', function (req, res) {
    res.sendFile( __dirname + "/" + "getrailshutdown.html" );
 })
//获取发来的post请求
app.post('/get', urlencodedParser, function (req, res) {
    res.header("Access-Control-Allow-Origin", "*");//允许跨域访问
    res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'});//设置response编码为utf-8
    //获取传递的值
    var response = {
        "time": req.body.time,
        "beginPlace": req.body.beginPlace,
        "endPlace": req.body.endPlace,
        "railNum": req.body.railNum
    };
    //定义请求头
    var options = {
        url: 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=' + response.time + '&leftTicketDTO.from_station=' + response.beginPlace + '&leftTicketDTO.to_station=' + response.endPlace + '&purpose_codes=ADULT',
        headers: {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Host": "kyfw.12306.cn"
        }
    };
    //发送get请求
    request(options, function (error, response, body) {
        if (!error && response.statusCode == 200) {
            //console.log(body) // 打印google首页
            //转换json
            var jsonData,json,details;
            var isFail = false;//是否找到列车
            try{
                jsonData = JSON.parse(body)
                json = jsonData['data']['result'];
            }
            catch (ex){
                res.write('{\"result\":2,\"msg\":\"信息获取失败,请联系开发者\"}');
                res.end();
            }
            
            //遍历查询到的数据
            json.forEach(element => {
                details = element.split('|')
                //找到此列车
                if (details[3] == response.railNum.toUpperCase()) {
                    isFail = true;
                    if (details[1] == '列车停运') {
                        res.write('{\"result\":1,\"msg\":\"列车停运\"}');
                    } else {
                        res.write('{\"result\":2,\"msg\":\"列车正常运行\"}');
                    }
                }
            });
            //未找到此列车
            if (!isFail) {
                res.write('{\"result\":-1,\"msg\":\"未找到此列车\"}');
            }
        }
        else{
            res.write('{\"result\":-1,\"msg\":\"信息获取失败,请联系开发者\"}');
        }
        res.end();
    })
})
//监听端口
var server = app.listen(8081, function () {
    var host = server.address().address
    var port = server.address().port
})