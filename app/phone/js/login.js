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
            appcan.locStorage.setVal("username", data["username"]);
            appcan.locStorage.setVal("password", data["password"]);
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

function noticing()
{
    $("#register").on("click", function()
    {
        $("#input_exception").attr("class", "uhide");
    })
    $("#forget-password").on("click", function()
    {
        $("#input_exception").attr("class", "uhide");
    })
    $("#password").on("click", function()
    {
        $("#input_exception").attr("class", "uhide");
    })
    $("#username").on("click", function()
    {
        $("#input_exception").attr("class", "uhide");
    })
}

function init() {
    noticing();
    $("#login_form").hide();
    $("#loading_wait").attr("class", ""); // show loading
    
    appcan.initBounce();
    appcan.button("#submit", "ani-act", function() {
        $("form").submit();
    })
    // 初始化提交按钮
    $("form").on('submit', function() {
        
        $("#login_form").hide();// hide
        $("#loading_wait").attr("class", "");//loading
        
        $("#login_form").attr("action", authenticate_user_url);
        appcan.request.postForm($("form"), function(data) {
            data = JSON.parse(data);
            status = data["status"];
            if (status == 0) {
                username = $("#username").attr("value");
                password = $("#password").attr("value");
                appcan.locStorage.val("username", username);
                appcan.locStorage.val("password", password);
                $("#input_exception").attr("class", "uhide");
                enter();
            } else {
                $("#loading_wait").attr("class", "uhide"); //hide loading
                $("#login_form").show();// show the form
                $("#input_exception").attr("class", "ub t-blu umar-t ulev-2");
            }
        });
        return false;
    });
    // 获取设备IMEI
    appcan.device.getInfo(10, function(err, data) {
        if (err) return;
        data = JSON.parse(data);
        imei = data["imei"];
        if (!checkIsCreated(imei))
            createUser(imei);
    });

    username = appcan.locStorage.val("username");
    password = appcan.locStorage.val("password");
    if (username == null || password == null) {
        $("#loading_wait").attr("class", "uhide");
        $("#login_form").show();
    } else {
        appcan.request.post(authenticate_user_url, {
            "username" : username,
            "password" : password
        }, function(data) {
            data = JSON.parse(data);
            status = data["status"];
            if (status == 0)
            {
                $("#input_exception").attr("class", "uhide");
                enter();
            }
            else
            {
                $("#loading_wait").attr("class", "uhide");
                $("#login_form").show();
                $("#input_exception").attr("class", "ub t-blu umar-t ulev-2");
            }
        });
    }
}