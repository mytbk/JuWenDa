function searchresult() {

    var updateData;
    updateData = appcan.locStorage.val("resultlist");
    updateData = JSON.parse(updateData);
    
    var lv1 = appcan.listview({
        selector : "#listview",
        type : "thickLine",
        hasIcon : true,
        hasAngle : false
    });

    lv1.set(updateData);

    lv1.on('click', function(ele, context, obj, subobj) {
        var question = obj['title'];
        appcan.locStorage('title', obj[title]);
        appcan.openWinWithUrl('details', 'details.html');
    })
}