// 转发微博，并评论  
function forwardWeibo(content, mid, location, pdetail, url,retcode) {  
  var Data = new FormData();  
  Data.append('pic_src', '');  
  Data.append('pic_id', '');  
  Data.append('appkey', '');  
  // mid为该微博的id  
  Data.append('mid', mid);  
  Data.append('style_type', '2');  
  Data.append('mark', '');  
  //reason为转发内容  
  Data.append('reason', content);  
  Data.append('location', location);  
  Data.append('pdetail', pdetail);  
  Data.append('module', '');  
  Data.append('page_module_id', '');  
  Data.append('refer_sort', '');  
  Data.append('is_comment', '1');  
  Data.append('rank', '0');  
  Data.append('rankid', '');  
  Data.append('_t', '0');  
  Data.append('retcode', retcode || '');  
  
  var xhr = new XMLHttpRequest();  
  xhr.timeout = 3000;  
  xhr.responseType = "text";  
  xhr.open('POST', url + new Date().getTime(), true);  
  xhr.onload = function(e) {  
    if (this.status == 200 || this.status == 304) {  
      var data = JSON.parse(this.responseText);  
      if (data.code == "100000") {  
        // 转发微博成功  
        console.log(content);  
      }else {  
        // 转发微博失败  
        console.log(data);  
      }  
    }  
  };  
  xhr.send(Data);  
}  
//count++解决转发内容相同问题  
var count = 0;  
var upper_bound = 10;


//Change the following variables if changing tweet to repost
var mid="4241543772751117";
var location="page_100505_single_weibo";
var pdetail="1005052949487607";
var url="https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100505&__rnd=";

var i = setInterval(function(){  
  count ++;
  var str=count + "//@2肉肉的追星小号: #朱正廷# [兔子]#朱正廷每天给你新鲜感# 贝贝贝贝我爱你[兔子]新发型超好看！特别帅特别man[兔子]最近行程紧张一定要照顾好自己好好休息[兔子]期待下一次和你的会面@THEO-朱正廷";  
  forwardWeibo(str, mid, location, pdetail, url); 
  if (count == upper_bound){
    clearInterval(i)
  } 
}, 10000); 