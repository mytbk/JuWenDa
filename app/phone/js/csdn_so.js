
function sendRequestWithKey(page, key, listview) {
    page = encodeURIComponent(page);
    key = encodeURIComponent(key);
    var url = "http://app.internetware.cn/jwd/?iw-apikey=123&iw-cmd=search&p=" + page + "&q=" + key;

    var resultData = [];
    appcan.request.get(url, function(data) {
        data = dealwithResult(data);
        listview.set(data);
        
    });
}

function dealwithResult(data) {
    var response,
        object,
        list,
        text = {
        title : "",
        describe : "",
        id : ""
    },
        resultData = [];
    var len = data.length;
    var i,
        j;
    for ( i = 0; i < len; i++)
        if (data[i] == '[')
            break;
    for ( j = len - 1; j >= 0; j--)
        if (data[j] == ']')
            break;
    data = data.substring(i, j + 1);
    var data = eval(data);
    len = data.length;
    for ( i = 0; i < len; i++) {
        var text={title:"",describe:"",id:""};
        text.title = data[i].title;
        text.describe = data[i].summary;
        text.id = data[i].link;
        if (text["id"].search(/http:\/\/blog.csdn.net/) != -1) resultData.push(text);
    }
    return resultData;
}

function sendRequestWithDetailPage(link) {
    var url = "http://app.internetware.cn/jwd/?iw-apikey=123&iw-cmd=resultcontent&iw_ir_1=";
    link = link.replace(/http:\/\/blog.csdn.net/, "");
    url = url + link;
    var resultData;
    appcan.request.get(url, function(data) {
        data = dealwithDetailPage(data);
        data = data.replace(/<[^>]*>/g, "");
        data = data.replace(/&nbsp;/g, " ");
        data = data.replace(/&lt;/g, "<");
        data = data.replace(/&gt;/g, ">");
        data = data.replace(/&amp;/g, "&");
        data = data.replace(/&quot;/g, "\"");
        appcan.locStorage.val("content", data);
        appcan.openWinWithUrl("details","details.html");
    });
}

function dealwithDetailPage(data)
{
    var len=data.length;
    var i,j;
    for(i=0;i<len;i++)
        if(data[i]=='<')
            break;
    for(j=len-1;j>=0;j--)
        if(data[j]=='>')
            break;
    data=data.substring(i,j+1);
    return data;
}