function sendRequestWithKey(page, key, listview) {
    username = appcan.locStorage.val("username");
    appcan.request.post(search_answer_url, {
        "title" : key,
        "username" : username
    }, function(data) {
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
        data = dealwithDetailPage(data);
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