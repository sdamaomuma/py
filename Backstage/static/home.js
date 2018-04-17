/**
 * Created by Administrator on 2018/4/15.
 */
function display_hide_right(hide_div_right_id){
    document.getElementById('hide_div_right_1.1').classList.add("hidden");
    document.getElementById('hide_div_right_2.1').classList.add("hidden");
    document.getElementById('hide_div_right_2.2').classList.add("hidden");
    document.getElementById('hide_div_right_2.3').classList.add("hidden");
    document.getElementById('hide_div_right_3.1').classList.add("hidden");
    document.getElementById('hide_div_right_3.2').classList.add("hidden");
    document.getElementById('hide_div_right_3.3').classList.add("hidden");
    document.getElementById('hide_div_right_3.4').classList.add("hidden");
    document.getElementById('hide_div_right_4.1').classList.add("hidden");
    document.getElementById('hide_div_right_4.2').classList.add("hidden");
    document.getElementById('hide_div_right_4.3').classList.add("hidden");
    document.getElementById('hide_div_right_4.4').classList.add("hidden");
    document.getElementById(hide_div_right_id).classList.remove("hidden");
}
$("#submit_1_1").click(function(){
    $.ajax({
        url: "/home/",
        type:"POST",
        data:{
            'from_page':'1.1',
            'start_time':$('#start_time').val(),
            'end_time':$('#end_time').val(),
            'uin':$('#uin').val(),
            'order_type':$('#order_type').val(),
            'sale_type':$('#sale_type').val(),
            'status':$('#status').val(),
            'payment_type':$('#payment_type').val(),
            'full_network_parment_uin':$('#full_network_parment_uin').val(),
            'proxy_room_id':$('#proxy_room_id').val(),
            'proxy_uin':$('#proxy_uin').val(),
            'order_id':$('#order_id').val()
        },
        success:function(dat){
            if(dat=="date_error"){
                alert('请选择开始日期和结束日期！')
            }
            else if(dat=="date_range_error"){
                alert('开始日期和结束日期范围必须在30天内！')
            }
            else{
                var data = JSON.parse(dat);     //取出数据列表
                var data_sum = data.length;     //取出列表长度
                var data_count = data_sum / 20;     //一页显示20条数据，算一下分页,结果可能是小数，也就是分页数要+1
                var data_count_str = data_count.toString();     //将结果转换成字符串
                var data_count_str_1 = data_count_str.split('.')[0];    //将字符串切片，str_1是整数部分
                var data_count_f = parseFloat(data_count_str);  //将字符串变成float，如果是整数，就会去掉“.”
                var rep = /\./;                                 //表达式匹配“.”，用于判断是整数还是小数
                if(rep.test(data_count_f)){
                    count = parseInt(data_count_str_1) + 1;  //如果data_count_f有“.”就是true，分页数量就+1
                }else{
                    count = parseInt(data_count_str_1);      //否则，就使用“data_sum/20”的结果
                }
                //根据分的页数，在div_1_1标签同级下创建多个div标签，并且隐藏，id也是自动生成的.
                //在自动生成的div下再创建一个表格，id自动生成，并写入表头。
                for(var i= 1;i<count+1;i++){
                    var div_id = 'div_1_1_' + i;
                    var table_id = 'table_1_1_' + i;
                    //创建div
                    $('#div_1_1').after('<div id="'+ div_id + '" class="hidden"></div>');
                    //创建表格，添加表头
                    $('#'+div_id).append('<table id="'+table_id+'" class="table table-bordered bg-success">'+
                        '<tr class="bg-warning"><th>key_1</th><th>key_2</th><th>key_3</th><th>key_4</th>'+
                        '<th>key_5</th><th>key_6</th><th>key_7</th><th>key_8</th></tr>')
                }
                //将上面的生成的所有的表格，都按照页码添加好相应的数据
                for(var i=1;i<count+1;i++){
                    var page_num = i;
                    var min_data = (page_num - 1) * 20; //根据页码计算出数据的起始索引和结束索引
                    var max_data = page_num * 20;
                    var data_1 = data.slice(min_data,max_data);//索引(数据id) 0-20(1-20) 20-40(21-40) 40-60(41-60)
                    var table_id = '#table_1_1_' + i;
                    //往表格里添加数据
                    for(item in data_1){
                        $(table_id).append('<tr>'+
                                '<td>'+data_1[item]['key_1']+'</td>'+
                                '<td>'+data_1[item]['key_2']+'</td>'+
                                '<td>'+data_1[item]['key_3']+'</td>'+
                                '<td>'+data_1[item]['key_4']+'</td>'+
                                '<td>'+data_1[item]['key_5']+'</td>'+
                                '<td>'+data_1[item]['key_6']+'</td>'+
                                '<td>'+data_1[item]['key_7']+'</td>'+
                                '<td>'+data_1[item]['key_8']+'</td>'+
                                '</tr>')
                        }
                }
                //要在每页的div下面添加页码，因此要先生成页码的字符串
                var page_sum = '<ul class="pagination"><li><a href="#">&laquo;</a></li>';
                //用for循环生成页码数量对应的a标签，a标签里要绑定一个函数，用于点击某页时显示某页的数据，隐藏其他页
                for(i=1;i<count+1;i++){
                    var page_id = 'div_1_1_' + i;
                    page_sum = page_sum + '<li><a onclick="display_page_1_1(\''+page_id+'\')">'+i+'</a></li>';
                    //a标签绑定函数时传递参数“func('参数')”,由于参数要加单引号，所以字符串拼接时单引号要转义
                }
                page_sum = page_sum + '<li><a href="#">&raquo;</a></li></ul>';  //完整的分页页码标签的字符串
                //将上面的页码字符串放到所有的分页里。
                for(i=1;i<count+1;i++){
                    var div_id = '#div_1_1_' + i;
                    $(div_id).append(page_sum)
                }
                document.getElementById('div_1_1_1').classList.remove("hidden"); //将第1页显示
                }
            }
        })
    });
//下面这个函数是给订单管理页面分页显示数据用的函数
function display_page_1_1(hide_div_1_1_id){
    for(var i=1;i<count+1;i++){
        var page_id = 'div_1_1_' + i;
        document.getElementById(page_id).classList.add("hidden");
    }
    document.getElementById(hide_div_1_1_id).classList.remove("hidden");
}