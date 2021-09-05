// Rounded slider
const span = document.querySelector("#value");
const setValue = function(value, active) {
    document.querySelectorAll("round-slider").forEach(function(el) {
        if (el.value === undefined) return;
        el.value = value;
    });
    //const span = document.querySelector("#value");
    span.innerHTML = value;
    if (active)
        span.style.color = 'red';
    else
        span.style.color = 'black';
}

document.querySelectorAll("round-slider").forEach(function(el) {
    el.addEventListener('value-changed', function(ev) {
        if (ev.detail.value !== undefined)
            setValue(ev.detail.value, false);
        else if (ev.detail.low !== undefined)
            setLow(ev.detail.low, false);
        else if (ev.detail.high !== undefined)
            setHigh(ev.detail.high, false);
    });

    el.addEventListener('value-changing', function(ev) {
        if (span.innerHTML !== ev.detail.value.toString())
            setLight(ev.detail.value);
        if (ev.detail.value !== undefined)
            setValue(ev.detail.value, true);
        else if (ev.detail.low !== undefined)
            setLow(ev.detail.low, true);
        else if (ev.detail.high !== undefined)
            setHigh(ev.detail.high, true);
    });
});

function setLight(percent) {
    fetch("/intensity/".concat(percent)).then(function(response) {
        return response.text();
    }).then(function(data) {
        console.log(data);
    }).catch(function() {
        console.log("error");
    });
}
