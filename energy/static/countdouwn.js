
var currentdate = document.getElementById("time");
var countDownDate = new Date(
  new Date(currentdate.textContent).getTime() + 60 * 60 * 26 * 1000
);
//+ 60 * 60 * 24 * 1000);
//var countDownDate = new Date(currentdate.textContent).getTime()

var x = setInterval(function () {
  if (! currentdate.textContent) {
    window.location.href = "/new";
  }
  var now = new Date().getTime();

  var distance = countDownDate - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("timer").innerHTML =
    days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

  if (distance < 0) {
    clearInterval(x);
    document.getElementById("timer").innerHTML = "EXPIRED";
  }
}, 1000);
