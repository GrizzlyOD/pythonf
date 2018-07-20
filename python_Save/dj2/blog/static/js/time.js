/**
 * Created by Administrator on 2018/4/5 0005.
 */
function startime()
{
    var show_day=new Array('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
    var time = new Date()
    var date = time.getDate()
    var d = time.getDay()
    var mo = time.getMonth()+1
    var y = time.getFullYear()
    var h = time.getHours()
    var m = time.getMinutes()
    var s = time.getSeconds()
    m = checktime(m)
    h = checktime(h)
    s = checktime(s)
    document.getElementById('time').innerHTML=(mo+"/"+date+"/"+y+" "+show_day[d]+" "+h+":"+m+":"+s)
    t = setTimeout('startime()',1000)
}
function checktime(x)
{
    if(x<10)
        x = "0"+x
    return x
}