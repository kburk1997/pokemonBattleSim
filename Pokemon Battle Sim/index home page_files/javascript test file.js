<script type="text/javascript">
    $(function(){
        $.getJSON('names.json',function(data){
            console.log('success');
            $.each(data.employees,function(i,emp){
                $('ul').append('<li>'+emp.firstName+' '+emp.lastName+'</li>');
            });
        }).error(function(){
            console.log('error');
        });
    });
</script>