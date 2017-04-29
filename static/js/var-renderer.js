renders = {
    plain: function (name, value) {$('#'+name).text(value);},
    image: function (name, value) {
        $('#'+name).attr("src", "data:image/png;base64, "+value);
    }
};
