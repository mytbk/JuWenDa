var listview;

function initIndex() {
    appcan.initBounce();

    appcan.button(".btn", "ani-act", function() {
        question = $("#question").val();
        sendRequestWithKey(1, question, listview);
    });

    listview = appcan.listview({
        selector : "#listview",
        type : "thickLine",
        hasIcon : false,
        hasAngle : true,
        hasSubTitle : true,
        multiLine : 1,
    });

    data = [];

    listview.set(data);

    listview.on("click", function(ele, obj, curEle) {
        var url = obj["id"];
        appcan.locStorage.val("title", obj["title"]);
        sendRequestWithDetailPage(url);
    });
}
