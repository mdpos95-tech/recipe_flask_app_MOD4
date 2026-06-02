function confirmDelete() {
    return confirm("Are you sure you want to delete this recipe?");
}

setTimeout(function() {
    let message = document.querySelectorAll('.flash-message');
    message.forEach(function(msg) {
        msg.style.display = 'none';
    }); 
}, 3000);

