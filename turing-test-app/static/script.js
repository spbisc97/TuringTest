$(document).ready(function() {
    $('#choice-form').on('submit', function(e) {
        e.preventDefault();
        var selected = $('input[name="choice"]:checked').val();
        var correct = $('input[name="correct"]').val();
        if (!selected) {
            alert("Please select an option!");
            return;
        }
        $(this).append('<input type="hidden" name="user_choice" value="' + selected + '">');
        this.submit();
    });
});
