       let countrySelected = $('#id_default_county').val();
        if(!countrySelected) {
            $('#id_default_country').css('color', '#aab7c4');
        };
        $("#id_default_county").change(function(){
            countrySelected = $(this).val();
            if(!countrySelected){
                $(this).css('color', '#aab7c4');
            }
            else {
                $(this).css('color','#000');
            }
        });