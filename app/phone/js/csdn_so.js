function sendRequestWithKey(page, key, listview) {
    username = appcan.locStorage.val("username");
    appcan.request.post(search_answer_url, {
        "title" : key,
        "username" : username
    }, function(data) {
        data = dealwithResult(data);

        appcan.locStorage.val("resultlist", data);
        //listview.set(data);
        //uexLoadingView.close();
        appcan.openWinWithUrl("searchresult", "searchresult.html");
    });
    /*var jsonstr = {
        "x" : 200,
        "y" : 500,
        "w" : 240,
        "h" : 40,
        "style" : {
            "styleId" : 0,
            "pointNum" : 4,
            "pointColor" : ["#ff4444", "#ffbb33", "#99cc00", "#33b5e5"]
        }
    };
    
    uexLoadingView.open(jsonstr);
*/
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
        var text = {
            title : "",
            describe : "",
            id : ""
        };
        text.title = data[i].title;
        text.describe = data[i].summary;
        text.id = data[i].link;
        if (text["id"].search(/http:\/\/blog.csdn.net/) != -1)
            resultData.push(text);
    }
    return resultData;
}

function sendRequestWithDetailPage(link) {
    link = link.replace(/http:\/\/blog.csdn.net/, "");

    appcan.request.post(get_detail_url, {
        "link" : link
    }, function(data) {
        data = JSON.parse(data);
        data = data["iw-response"]["iw-object"]["content"];
        //data = dealwithDetailPage(data.toString());
        appcan.locStorage.val("content", data);
        appcan.openWinWithUrl("details", "details.html");
    });
}

function dealwithDetailPage(data) {
    var len = data.length;
    var i,
        j;
    for ( i = 0; i < len; i++)
        if (data[i] == '<')
            break;
    for ( j = len - 1; j >= 0; j--)
        if (data[j] == '>')
            break;
    data = data.substring(i, j + 1);
    return data;
}