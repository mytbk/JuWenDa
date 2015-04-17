function enter() {
    appcan.frame.open("index", "index.html", 0, 0);
}

function checkIsCreated(imei) {
    var result;
    $.ajax({
        async : false,
        type : "POST",
        url : is_created_url,
        data : {
            "imei" : imei
        },
        success : function(data) {
            result = data["created"];
        }
    });
    return result == 1;
}

function createUser(imei) {
    $.ajax({
        async : false,
        type : "POST",
        url : create_user_url,
        data : {
            "imei" : imei
        },
        success : function(data) {
            appcan.locStorage.setVal(data);
            appcan.window.confirm({
                title : "修改密码",
                content : "系统已为你随机分配了用户名和密码，如需在其他设备登录请在个人设置中修改用户名和密码",
                buttons : ["进入聚问答"],
                callback : function(err, data, dataType, optId) {
                    enter();
                }
            });
        }
    });
}

function init() {
    $("#login_form").hide();
    appcan.initBounce();
    appcan.button("#submit", "ani-act", function() {
        $("form").submit();
    })
    // 初始化提交按钮
    $("form").on('submit', function() {
        $("#login_form").attr("action", authenticate_user_url);
        appcan.request.postForm($("form"), function(data) {
            data = JSON.parse(data);
            status = data["status"];
            if (status == 0) {
                username = $("#username").attr("value");
                password = $("#password").attr("value");
                appcan.locStorage.val("username", username);
                appcan.locStorage.val("password", password);
                enter();
            } else {
            }
        });
        return false;
    });
    // 获取设备IMEI
    appcan.device.getInfo(11, function(err, data) {
        if (err)
            return;
        imei = data["imei"];
        if (!checkIsCreated(imei))
            createUser();
    });

    username = appcan.locStorage.val("username");
    password = appcan.locStorage.val("password");
    if (username == null || password == null) {
        $("#login_form").show();
    } else {
        appcan.request.post(authenticate_user_url, {
            "username" : username,
            "password" : password
        }, function(data) {
            status = data["status"];
            if (status == 0)
                enter();
            else
                $("#login_form").show();
        });
    }
}