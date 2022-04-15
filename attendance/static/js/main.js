setInterval('time()',1000);


function time() {
  var now = new Date();
  document.getElementById("time").innerHTML = now.toLocaleString();
}

function decision_alert() {
  window.alert('勤怠を確定させますか？');
}
