var listview;

function initIndex() {
    appcan.initBounce();

    var listview = appcan.listview({
        selector : "#listview",
        type : "thickLine",
        hasIcon : false,
        hasAngle : true,
        hasSubTitle : true,
        multiLine : 1,
    });

    appcan.button(".btn", "ani-act", function() {
        question = $("#question").val();
        sendRequestWithKey(1, question, listview);
    });

    var data = [{
        title : "Spark如何配置？",
        describe : "",
    }, {
        title : "机器学习如何并行化？",
        describe : "",
    }, {
        title : "路由器如何配置IPV6？",
        describe : "",
    }, {
        title : "程序猿如何找妹子？",
        describe : "",
    }]

    listview.set(data);
    /*var data = appcan.locStorage.val("resultlist");

    listview.set(data);

    listview.on("click", function(ele, obj, curEle) {
    var url = obj["id"];
    appcan.locStorage.val("title", obj["title"]);
    sendRequestWithDetailPage(url);
    });*/
    //Bounce();
}

function Bounce(funcTop, funcBottom) {
    uexWindow.setBounce("1");
    if (!funcTop && !funcBottom) {
        uexWindow.showBounceView("0", "rgba(255,255,255,0)", "0");
        uexWindow.showBounceView("1", "rgba(255,255,255,0)", "0");
        return;
    }
    var top = 0,
        btm = 1;
    uexWindow.onBounceStateChange = function(type, state) {

        if (type == top && state == 2) {//顶部弹动
            funcTop();
            uexWindow.resetBounceView("0");
        }
        if (type == btm && state == 2) {//底部弹动
            funcBottom();
            uexWindow.resetBounceView("1");
        }

    }
    if (funcTop) {
        uexWindow.setBounceParams('0', "{'pullToReloadText':'下拉刷新','releaseToReloadText':'释放刷新','loadingText':'正在刷新，请稍候'}");
        uexWindow.showBounceView(top, "rgba(255,255,255,0)", 1);
        uexWindow.notifyBounceEvent(top, 1);
    }
    if (funcBottom) {
        uexWindow.setBounceParams('1', "{'pullToReloadText':'加载更多','releaseToReloadText':'加载更多','loadingText':'加载中，请稍候'}");
        uexWindow.showBounceView(btm, "rgba(255,255,255,0)", 1);
        //设置弹动位置及效果([1:显示内容;0:不显示])
        uexWindow.notifyBounceEvent(btm, 1);
        //注册接收弹动事件([0:不接收onBounceStateChange方法回调;1:接收])
    }
}