// Custom JavaScript for Order Manager
document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Confirm before delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
    
    // Status badge colors
    const statusBadges = document.querySelectorAll('.status-badge');
    statusBadges.forEach(badge => {
        const status = badge.textContent.trim().toLowerCase();
        badge.classList.add(`badge-${status}`);
    });
});