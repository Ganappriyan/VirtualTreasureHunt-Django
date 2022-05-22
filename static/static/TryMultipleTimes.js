count = 0
function check() {
  if(count > 5) {
    document.forms[0].submit();
  }
  document.getElementById('cmt').innerHTML = 'Wrong Password, TRY AGAIN!'
  count += 1
}