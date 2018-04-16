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
            if(dat=="OK"){
                alert(dat)
            }else{
                var data = JSON.parse(dat);     //ȡ�������б�
                var data_sum = data.length;     //ȡ���б���
                var data_count = data_sum / 20;     //һҳ��ʾ20�����ݣ���һ�·�ҳ,���������С����Ҳ���Ƿ�ҳ��Ҫ+1
                var data_count_str = data_count.toString();     //�����ת�����ַ���
                var data_count_str_1 = data_count_str.split('.')[0];    //���ַ�����Ƭ��str_1����������
                var data_count_f = parseFloat(data_count_str);  //���ַ������float��������������ͻ�ȥ����.��
                var rep = /\./;                                 //���ʽƥ�䡰.���������ж�����������С��
                if(rep.test(data_count_f)){
                    count = parseInt(data_count_str_1) + 1;  //���data_count_f�С�.������true����ҳ������+1
                }else{
                    count = parseInt(data_count_str_1);      //���򣬾�ʹ�á�data_sum/20���Ľ��
                }
                //���ݷֵ�ҳ������div_1_1��ǩͬ���´������div��ǩ���������أ�idҲ���Զ����ɵ�.
                //���Զ����ɵ�div���ٴ���һ�����id�Զ����ɣ���д���ͷ��
                for(var i= 1;i<count+1;i++){
                    var div_id = 'div_1_1_' + i;
                    var table_id = 'table_1_1_' + i;
                    //����div
                    $('#div_1_1').after('<div id="'+ div_id + '" class="hidden"></div>');
                    //���������ӱ�ͷ
                    $('#'+div_id).append('<table id="'+table_id+'" class="table table-bordered bg-success">'+
                        '<tr class="bg-warning"><th>key_1</th><th>key_2</th><th>key_3</th><th>key_4</th>'+
                        '<th>key_5</th><th>key_6</th><th>key_7</th><th>key_8</th></tr>')
                }
                //����������ɵ����еı�񣬶�����ҳ����Ӻ���Ӧ������
                for(var i=1;i<count+1;i++){
                    var page_num = i;
                    var min_data = (page_num - 1) * 20; //����ҳ���������ݵ���ʼ�����ͽ�������
                    var max_data = page_num * 20;
                    var data_1 = data.slice(min_data,max_data);//����(����id) 0-20(1-20) 20-40(21-40) 40-60(41-60)
                    var table_id = '#table_1_1_' + i;
                    //��������������
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
                //Ҫ��ÿҳ��div�������ҳ�룬���Ҫ������ҳ����ַ���
                var page_sum = '<ul class="pagination"><li><a href="#">&laquo;</a></li>';
                //��forѭ������ҳ��������Ӧ��a��ǩ��a��ǩ��Ҫ��һ�����������ڵ��ĳҳʱ��ʾĳҳ�����ݣ���������ҳ
                for(i=1;i<count+1;i++){
                    var page_id = 'div_1_1_' + i;
                    page_sum = page_sum + '<li><a onclick="display_page_1_1(\''+page_id+'\')">'+i+'</a></li>';
                    //a��ǩ�󶨺���ʱ���ݲ�����func('����')��,���ڲ���Ҫ�ӵ����ţ������ַ���ƴ��ʱ������Ҫת��
                }
                page_sum = page_sum + '<li><a href="#">&raquo;</a></li></ul>';  //�����ķ�ҳҳ���ǩ���ַ���
                //�������ҳ���ַ����ŵ����еķ�ҳ�
                for(i=1;i<count+1;i++){
                    var div_id = '#div_1_1_' + i;
                    $(div_id).append(page_sum)
                }
                document.getElementById('div_1_1_1').classList.remove("hidden"); //����1ҳ��ʾ
                }
            }
        })
    });
//������������Ǹ���������ҳ���ҳ��ʾ�����õĺ���
function display_page_1_1(hide_div_1_1_id){
    for(var i=1;i<count+1;i++){
        var page_id = 'div_1_1_' + i;
        document.getElementById(page_id).classList.add("hidden");
    }
    document.getElementById(hide_div_1_1_id).classList.remove("hidden");
}