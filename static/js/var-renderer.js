renders = {
    plain_s: function (name, value) {$('#'+name).text(value);},
    image_s: function (name, value) {
        $('#'+name).attr("src", "data:image/png;base64, "+value);
    },
    float_s: function (name, value) {
        var round_to = toc[name].round_to
        if (round_to !== null){value = value.toFixed(round_to)}
        $('#'+name).text(value)
    }
};
