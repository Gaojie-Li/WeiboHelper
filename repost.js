// 转发微博，并评论  
function forwardWeibo(content,retcode) {  
  var Data = new FormData();  
  Data.append('pic_src', '');  
  Data.append('pic_id', '');  
  Data.append('appkey', '');  
  // mid为该微博的id  
  Data.append('mid', '4242262206068056');  
  Data.append('style_type', '2');  
  Data.append('mark', '');  
  //reason为转发内容  
  Data.append('reason', content);  
  Data.append('location', 'page_100505_single_weibo');  
  Data.append('pdetail', '1005052949487607');  
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
  //xhr.open('POST','https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100505&__rnd=1527034289976',true)
  xhr.open('POST', 'https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100206&__rnd=' + new Date().getTime(), true);  
  //xhr.open('POST', 'http://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100206&__rnd=' + new Date().getTime(), true); 

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
var upper_bound = 50;


//Change the following variables if changing tweet to repost
var mid='4242262206068056';
var location='page_100505_single_weibo';
var pdetail='1005052949487607';
var url= 'https://www.weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100505&__rnd=';

var i = setInterval(function(){  
  count ++;
  var str=count + "//@2肉肉的追星小号: #朱正廷#[心]#朱正廷每天给我新鲜感# 谁也不知道下一秒会发生什么，但是我能确信，在上一秒这一秒下一秒，我还是在喜欢你 [兔子][兔子]@THEO-朱正廷";  
  forwardWeibo(str); 
  if (count > upper_bound){
    clearInterval(i)
  } 
}, 10000); 