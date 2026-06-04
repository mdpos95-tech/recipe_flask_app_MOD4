function confirmDelete() { // Asks the user to confirm before deleting a recipe.
    return confirm("Are you sure you want to delete this recipe?");
}

setTimeout(function() { // Automatically hides flash message after 3 seconds.
    let message = document.querySelectorAll('.flash-message');
    message.forEach(function(msg) {
        msg.style.display = 'none';
    }); 
}, 3000);

document.addEventListener('DOMContentLoaded', function() { // Updates the remaining character count while the user types a comment.
    const commentBox = document.getElementById('comment-box');
    const charCount = document.getElementById('char-count');
    const maxChars = 200;

    if (commentBox && charCount) {
        commentBox.addEventListener('input', function() {
            const remaining = maxChars - commentBox.value.length;
            charCount.textContent = `${remaining} characters remaining`;
        });
    }
});


document.addEventListener('DOMContentLoaded', function() { // Shows or hides extra recipe details when the button is clicked.
    const buttons = document.querySelectorAll('.toggle-details');
    buttons.forEach(function(button) {        button.addEventListener('click', function() {
            const details = this.nextElementSibling;
            if (details.style.display === 'block') {
                details.style.display = 'none';
                this.textContent = 'Show Recipe Details';
            } else {
                details.style.display = 'block';
                this.textContent = 'Hide Recipe Details';
            }     });
    });
});


